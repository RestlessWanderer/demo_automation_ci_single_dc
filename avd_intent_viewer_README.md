# AVD Intent Viewer

An amplification calculator for Arista AVD — shows how a small amount of YAML data model input produces a large amount of EOS configuration output. Generates a self-contained HTML report you can open in any browser, email, or share in Slack.

## What It Does

AVD Intent Viewer scans your AVD repository, counts lines across all data model input files (group_vars, global_vars) and all generated EOS config files, and produces a clean HTML report showing:

- **Amplification factor** — the ratio of config output to data model input (e.g., 3x, 10x, 50x)
- **Input file tree** — all YAML data model files with their directory locations and line counts
- **Output file tree** — all generated EOS `.cfg` files with line counts

No builds are run — it reads existing files on disk. Runs instantly.

## Quick Start

```bash
# From inside any AVD repository with configs already built:
python avd_intent_viewer.py

# Open the generated report
open avd_intent_report.html
```

## Requirements

- **Python 3.9+**
- **PyYAML** (included in any AVD environment)
- A working AVD repository with generated configs in `intended/configs/`

No Ansible or AVD collection needed to run the tool — it only reads files.

## Installation

Copy `avd_intent_viewer.py` into your AVD repository or anywhere on your PATH:

```bash
# Option 1: Copy to your repo
cp avd_intent_viewer.py /path/to/your/avd-repo/

# Option 2: Make it globally available
cp avd_intent_viewer.py /usr/local/bin/avd-intent-viewer
chmod +x /usr/local/bin/avd-intent-viewer
```

## Usage

```
avd-intent-viewer [REPO_PATH] [OPTIONS]

positional arguments:
  REPO_PATH             Path to AVD repository (default: current directory)

options:
  -s, --site SITE       Site name to analyze (auto-detected if only one)
  -o, --output FILE     Output HTML file (default: avd_intent_report.html)
```

### Examples

```bash
# Analyze the current repo
python avd_intent_viewer.py

# Analyze a specific repo
python avd_intent_viewer.py /path/to/avd-repo

# Multi-site repo — specify which site
python avd_intent_viewer.py -s dc2

# Custom output file
python avd_intent_viewer.py -o demo_report.html
```

## How It Works

1. **Auto-discovers** the repo structure:
   - Parses `ansible.cfg` to find global_vars paths
   - Scans for sites with `inventory.yml` + `group_vars/`
   - Locates generated configs in `intended/configs/`

2. **Counts lines** in all input YAML files and output `.cfg` files

3. **Generates a self-contained HTML report** with the amplification factor, input file tree, and output file tree

## Supported Repo Structures

```
# Multi-site (most common)
repo/
  ansible.cfg
  global_vars/
  sites/dc1/
    inventory.yml
    group_vars/
    intended/configs/

# Flat structure
repo/
  ansible.cfg
  inventory.yml
  group_vars/
  intended/configs/
```

## Output

The HTML file is fully self-contained — all CSS is embedded inline. No external dependencies, works offline, print-friendly.

## Playbook Integration

You can also add the amplification factor directly to your AVD build playbook output. Add these three tasks at the end of your build playbook:

```yaml
    - name: Count input lines (data model)
      ansible.builtin.shell: "grep -c '' {{ inventory_dir }}/group_vars/*.yml {{ inventory_dir }}/../../global_vars/*.yml 2>/dev/null | awk -F: '{s+=$NF} END{print s}'"
      register: input_lines
      run_once: true
      changed_when: false

    - name: Count output lines (generated configs)
      ansible.builtin.shell: "grep -c '' {{ inventory_dir }}/intended/configs/*.cfg 2>/dev/null | awk -F: '{s+=$NF} END{print s}'"
      register: output_lines
      run_once: true
      changed_when: false

    - name: AVD Amplification Factor
      ansible.builtin.debug:
        msg: "{{ input_lines.stdout | int }} lines of input -> {{ output_lines.stdout | int }} lines of config = {{ (output_lines.stdout | int / input_lines.stdout | int) | round(0) | int }}x amplification"
      run_once: true
```

## License

MIT
