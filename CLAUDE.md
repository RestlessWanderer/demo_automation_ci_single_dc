# CLAUDE.md

## Project Overview

Single-datacenter L2LS (Layer 2 Leaf-Spine) network automation repo using Arista AVD 6.0.0.

- **Topology:** 6 Arista switches — 2x 7280R3 L3 spines + 4x 7050SX3 L2 leafs, all MLAG-paired
  - DC1-SPINES: spine-1, spine-2
  - DC1-LEAF1: leaf-1a, leaf-1b
  - DC1-LEAF2: leaf-2a, leaf-2b
- **Network services:** 4 data VLANs (20-23) with SVIs on spines as L3 gateways
- **Underlay:** OSPF on spines, 802.1X/RADIUS ready (endpoint port profiles commented out)
- **Tooling:** pyavd 6.0.0, ANTA 1.7.0, CloudVision (CVaaS prod, on-prem ACT digital twin)

## Key File Locations

- `sites/dc1/group_vars/dc1_network_services.yml` — tenant VLANs/SVIs
- `sites/dc1/group_vars/dc1_spines.yml` — spine node definitions, MLAG, loopbacks
- `sites/dc1/group_vars/dc1_leafs.yml` — leaf node definitions, uplinks, MLAG
- `sites/dc1/group_vars/dc1_fabric.yml` — fabric name, underlay protocol, dot1x, RADIUS
- `sites/dc1/group_vars/dc1_endpoints.yml` — connected endpoint port profiles (commented out)
- `sites/dc1/inventory.yml` — production inventory (172.31.0.x)
- `sites/dc1/inventory_act.yml` — ACT digital twin inventory (10.18.174.x)
- `global_vars/management.yml` — shared vars (AAA, NTP, CVaaS, management)
- `playbooks/` — build/deploy/validate playbooks for prod and digital twin
- `sites/dc1/intended/` — generated EOS configs and structured YAML
- `sites/dc1/digital_twin/` — parallel generated configs for ACT

## CI/CD Pipeline

1. **PR opened** → `pr_test_and_build.yml` builds configs, auto-commits back to PR branch
2. **PR merged** → `deploy_digital_twin.yml` deploys to ACT, runs ANTA validation, triggers docs
3. **Release published** → `deploy_prod.yml` deploys to CVaaS, runs ANTA validation, triggers docs
4. **Docs** → `build_mkdocs.yml` generates MkDocs site, deploys to GitHub Pages

## Common Commands

- `make build-dc1` — build both digital twin and production configs
- `make deploy-dc1` / `make deploy-dc1_dt` — deploy to prod / digital twin
- `make validate-dc1` / `make validate-dc1_dt` — ANTA validation against prod / digital twin

## Environment

- Runs in a devcontainer (`ghcr.io/aristanetworks/avd/universal:python3.13-avd-v6.0.0`)
- All memory/context should live in-repo (not in `~/.claude/`) since this reopens in a devcontainer
- Secrets: `CV_TOKEN` (prod CVaaS), `ACT_CV_TOKEN` (digital twin CloudVision at 10.18.174.105)
