# AVD Intent Report

An Ansible role that calculates the amplification factor of your Arista AVD data model — how many lines of EOS configuration are generated from your YAML input. Displays the result during the play and generates a Markdown report.

## What It Does

After your AVD build completes, this role:

1. Counts lines across all data model input files (`group_vars/*.yml` and `global_vars/*.yml`)
2. Counts lines across all generated EOS config files (`intended/configs/*.cfg`)
3. Displays the amplification factor in the play output
4. Generates a Markdown report (`avd_intent_report.md`) with file-level detail

### Example Play Output

```
TASK [avd_intent_report : AVD Amplification Factor] ****************************
ok: [spine-1] => {
    "msg": "225 lines of input -> 3,626 lines of config = 16x amplification"
}
```

### Example Report

The generated Markdown includes:

- Centered amplification stats (input lines, output lines, Nx factor)
- Side-by-side file trees showing each input and output file with line counts
- Renders on GitHub, MkDocs, or any Markdown viewer that supports inline HTML

## Requirements

- Ansible with the `arista.avd` collection (you already have this if you're running AVD)
- The `community.general` collection

No Python dependencies beyond what AVD already requires.

## Installation

Copy the `avd_intent_report` directory into your AVD repository's `roles/` directory:

```bash
cp -r avd_intent_report /path/to/your/avd-repo/roles/
```

Ensure your `ansible.cfg` includes the local roles path:

```ini
[defaults]
roles_path = ./roles
```

## Usage

Add the role to the end of your AVD build playbook:

```yaml
---
- name: Build Fabric Switch Configuration
  hosts: "{{ target_fabric }}"
  gather_facts: false

  tasks:
    - name: Generate Structured Variables per Device
      ansible.builtin.import_role:
        name: arista.avd.eos_designs

    - name: Generate Intended Config and Documentation
      ansible.builtin.import_role:
        name: arista.avd.eos_cli_config_gen

    - name: Generate AVD Amplification Report
      ansible.builtin.import_role:
        name: avd_intent_report
```

Then run your build as usual:

```bash
ansible-playbook playbooks/build.yml -i sites/dc1/inventory.yml -e "target_fabric=dc1"
```

The amplification factor will display during the play, and `avd_intent_report.md` will be generated in your repository root.

## Supported Repo Structures

The role expects the standard AVD directory layout:

```
repo/
  ansible.cfg
  global_vars/
    *.yml
  roles/
    avd_intent_report/
  sites/<site>/
    inventory.yml
    group_vars/
      *.yml
    intended/
      configs/
        *.cfg
```

The role uses `inventory_dir` to locate `group_vars/` and `intended/configs/`, and resolves `global_vars/` relative to the repository root via `inventory_dir/../../global_vars/`.

## Output

The report is written to `avd_intent_report.md` in the repository root. It is self-contained Markdown with embedded HTML for the side-by-side layout — no external dependencies, works offline.

## License

MIT
