#!/usr/bin/env python3
"""AVD Intent Viewer — amplification calculator for AVD data model vs. EOS config output.

Reads AVD input YAML files and generated EOS configs, then produces a
self-contained HTML report showing the amplification factor.
"""

import argparse
import configparser
import sys
from dataclasses import dataclass, field
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required. Install with: pip install pyyaml")


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class FileInfo:
    path: Path
    relative_path: str
    line_count: int = 0


# ---------------------------------------------------------------------------
# AVDRepo — auto-discover repo structure
# ---------------------------------------------------------------------------

class AVDRepo:
    def __init__(self, repo_path: Path):
        self.repo_path = repo_path.resolve()
        self.ansible_cfg_path = None
        self.global_vars_paths = []
        self.sites = []

    def discover(self):
        self._find_ansible_cfg()
        self._find_global_vars()
        self._find_sites()

    def _find_ansible_cfg(self):
        cfg = self.repo_path / "ansible.cfg"
        if cfg.exists():
            self.ansible_cfg_path = cfg
        else:
            for parent in [self.repo_path] + list(self.repo_path.parents)[:3]:
                candidate = parent / "ansible.cfg"
                if candidate.exists():
                    self.ansible_cfg_path = candidate
                    break

    def _find_global_vars(self):
        if not self.ansible_cfg_path:
            return
        config = configparser.ConfigParser()
        config.read(str(self.ansible_cfg_path))
        if config.has_section("vars_global_vars") and config.has_option("vars_global_vars", "paths"):
            raw = config.get("vars_global_vars", "paths")
            for p in raw.split(","):
                p = p.strip()
                resolved = (self.ansible_cfg_path.parent / p).resolve()
                if resolved.is_dir():
                    self.global_vars_paths.append(resolved)
        if not self.global_vars_paths:
            candidate = self.repo_path / "global_vars"
            if candidate.is_dir():
                self.global_vars_paths.append(candidate)

    def _find_sites(self):
        sites_dir = self.repo_path / "sites"
        if sites_dir.is_dir():
            for child in sorted(sites_dir.iterdir()):
                if child.is_dir() and (child / "inventory.yml").exists() and (child / "group_vars").is_dir():
                    self.sites.append(child)
        if not self.sites:
            if (self.repo_path / "inventory.yml").exists() and (self.repo_path / "group_vars").is_dir():
                self.sites.append(self.repo_path)

    def get_site(self, site_name=None):
        if not self.sites:
            raise RuntimeError("No AVD sites found in this repository.")
        if site_name:
            for s in self.sites:
                if s.name == site_name:
                    return s
            raise RuntimeError(f"Site '{site_name}' not found. Available: {[s.name for s in self.sites]}")
        if len(self.sites) == 1:
            return self.sites[0]
        raise RuntimeError(f"Multiple sites found: {[s.name for s in self.sites]}. Use --site to specify one.")

    def get_fabric_name(self, site_path: Path):
        inv = site_path / "inventory.yml"
        if inv.exists():
            with open(inv) as f:
                data = yaml.safe_load(f)
            if isinstance(data, dict):
                keys = list(data.keys())
                if keys:
                    return keys[0]
        return site_path.name

    def get_input_files(self, site_path: Path):
        files = []
        gv = site_path / "group_vars"
        if gv.is_dir():
            for f in sorted(gv.glob("*.yml")):
                lines = len(f.read_text().splitlines())
                files.append(FileInfo(
                    path=f,
                    relative_path=str(f.relative_to(self.repo_path)),
                    line_count=lines,
                ))
        for gvp in self.global_vars_paths:
            for f in sorted(gvp.glob("*.yml")):
                lines = len(f.read_text().splitlines())
                files.append(FileInfo(
                    path=f,
                    relative_path=str(f.relative_to(self.repo_path)),
                    line_count=lines,
                ))
        return files

    def get_output_files(self, site_path: Path):
        files = []
        for config_dir in [site_path / "intended" / "configs", site_path / "configs"]:
            if config_dir.is_dir():
                for f in sorted(config_dir.glob("*.cfg")):
                    lines = len(f.read_text().splitlines())
                    files.append(FileInfo(
                        path=f,
                        relative_path=str(f.relative_to(self.repo_path)),
                        line_count=lines,
                    ))
                break
        return files


# ---------------------------------------------------------------------------
# Renderer
# ---------------------------------------------------------------------------

class Renderer:

    @staticmethod
    def _group_files(files):
        groups = {}
        for f in files:
            parts = f.relative_path.rsplit("/", 1)
            if len(parts) == 2:
                directory, filename = parts
            else:
                directory, filename = ".", parts[0]
            groups.setdefault(directory, []).append((filename, f.line_count))
        return groups

    def render(self, input_files: list, output_files: list, repo_path: Path, site_name: str):
        total_input = sum(f.line_count for f in input_files)
        total_output = sum(f.line_count for f in output_files)
        ratio = f"{total_output / total_input:.0f}x" if total_input else "N/A"

        input_groups = self._group_files(input_files)
        output_groups = self._group_files(output_files)

        input_table = self._build_table(input_groups)
        output_table = self._build_table(output_groups)

        return f"""# AVD Input vs. Configuration Output

<div align="center">

| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| <h2>{total_input:,}</h2> | | <h2>{total_output:,}</h2> | | <h2>{ratio}</h2> |
| **Lines of Input** | &xrarr; | **Lines of Config** | = | **Amplification** |

</div>

<div align="center">
<table>
<tr>
<td width="50%" valign="top">

### Data Model Input

*{total_input:,} total lines*

{input_table}

</td>
<td width="50%" valign="top">

### Configuration Output

*{total_output:,} total lines*

{output_table}

</td>
</tr>
</table>
</div>

---
*Generated by **avd-intent-viewer***
"""

    @staticmethod
    def _build_table(groups):
        lines = []
        lines.append("| File | Lines |")
        lines.append("|------|------:|")
        for directory in sorted(groups.keys()):
            dir_total = sum(lc for _, lc in groups[directory])
            lines.append(f"| **`{directory}/`** | **{dir_total:,}** |")
            for filename, line_count in groups[directory]:
                lines.append(f"| &nbsp;&nbsp;&nbsp;&nbsp;`{filename}` | {line_count:,} |")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        prog="avd-intent-viewer",
        description="AVD amplification calculator — compare data model input vs. config output.",
    )
    parser.add_argument("repo_path", nargs="?", default=".", help="Path to AVD repository (default: current directory)")
    parser.add_argument("-s", "--site", help="Site name to analyze (auto-detected if only one)")
    parser.add_argument("-o", "--output", default="avd_intent_report.md", help="Output markdown file (default: avd_intent_report.md)")
    args = parser.parse_args()

    repo_path = Path(args.repo_path).resolve()
    print(f"AVD Intent Viewer")
    print(f"{'=' * 50}")
    print(f"Repository: {repo_path}")

    repo = AVDRepo(repo_path)
    repo.discover()

    site_path = repo.get_site(args.site)
    site_name = repo.get_fabric_name(site_path)
    print(f"Site: {site_path.name} (fabric: {site_name})")

    input_files = repo.get_input_files(site_path)
    output_files = repo.get_output_files(site_path)

    total_input = sum(f.line_count for f in input_files)
    total_output = sum(f.line_count for f in output_files)
    ratio = f"{total_output / total_input:.0f}x" if total_input else "N/A"

    print(f"\nInput files ({len(input_files)}):")
    for f in input_files:
        print(f"  {f.relative_path} ({f.line_count:,} lines)")

    print(f"\nOutput files ({len(output_files)}):")
    for f in output_files:
        print(f"  {f.relative_path} ({f.line_count:,} lines)")

    print(f"\n{total_input:,} input lines -> {total_output:,} output lines = {ratio} amplification")

    print(f"\nGenerating report...")
    renderer = Renderer()
    html_content = renderer.render(input_files, output_files, repo_path, site_name)
    output_path = Path(args.output)
    output_path.write_text(html_content)
    size_kb = output_path.stat().st_size / 1024
    print(f"Report saved to: {output_path.resolve()} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()
