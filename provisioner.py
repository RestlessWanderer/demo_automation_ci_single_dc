#!/usr/bin/env python3

import base64
import ipaddress
import os
import sys

import requests

REPO_OWNER = "RestlessWanderer"
REPO_NAME = "demo_automation_ci_single_dc"
BASE_BRANCH = "main"
NETWORK_SERVICES_PATH = "sites/dc1/group_vars/dc1_network_services.yml"
API_BASE = "https://api.github.com"


def get_token():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Error: GITHUB_TOKEN environment variable is not set.")
        print("Export a GitHub Personal Access Token with repo scope:")
        print("  export GITHUB_TOKEN=ghp_xxxxxxxxxxxx")
        sys.exit(1)
    return token


def api_headers(token):
    return {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }


def api_request(method, endpoint, token, **kwargs):
    url = f"{API_BASE}/repos/{REPO_OWNER}/{REPO_NAME}{endpoint}"
    resp = requests.request(method, url, headers=api_headers(token), **kwargs)
    if not resp.ok:
        print(f"GitHub API error ({resp.status_code}): {resp.json().get('message', resp.text)}")
        sys.exit(1)
    return resp.json()


def prompt_vlan_info():
    print("\n=== VLAN Provisioning ===\n")

    while True:
        vlan_id_str = input("VLAN ID: ").strip()
        try:
            vlan_id = int(vlan_id_str)
            if not 1 <= vlan_id <= 4094:
                print("VLAN ID must be between 1 and 4094.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    vlan_name = input("VLAN Name (e.g. DC1_DATA_30): ").strip()
    if not vlan_name:
        print("VLAN name cannot be empty.")
        sys.exit(1)

    while True:
        subnet_str = input("Subnet (CIDR notation, e.g. 10.1.30.0/24): ").strip()
        try:
            network = ipaddress.ip_network(subnet_str, strict=False)
            hosts = list(network.hosts())
            if len(hosts) < 3:
                print("Subnet too small — need at least 3 usable host addresses.")
                continue
            break
        except ValueError:
            print("Invalid subnet. Use CIDR notation (e.g. 10.1.30.0/24).")

    return vlan_id, vlan_name, network, hosts


def calculate_ips(network, hosts):
    prefix_len = network.prefixlen
    virtual_router = str(hosts[0])
    spine1_ip = f"{hosts[1]}/{prefix_len}"
    spine2_ip = f"{hosts[2]}/{prefix_len}"
    return virtual_router, spine1_ip, spine2_ip


def build_svi_yaml_block(vlan_id, vlan_name, virtual_router, spine1_ip, spine2_ip):
    return (
        f"          - id: {vlan_id}\n"
        f"            name: '{vlan_name}'\n"
        f"            enabled: true\n"
        f"            ip_virtual_router_addresses:\n"
        f"              - {virtual_router}\n"
        f"            nodes:\n"
        f"              - node: spine-1\n"
        f"                ip_address: {spine1_ip}\n"
        f"              - node: spine-2\n"
        f"                ip_address: {spine2_ip}\n"
    )


def create_branch(token, branch_name):
    print(f"\nCreating branch '{branch_name}'...")
    ref_data = api_request("GET", f"/git/ref/heads/{BASE_BRANCH}", token)
    sha = ref_data["object"]["sha"]
    api_request("POST", "/git/refs", token, json={
        "ref": f"refs/heads/{branch_name}",
        "sha": sha,
    })
    print(f"  Branch '{branch_name}' created.")


def update_network_services(token, branch_name, svi_yaml_block, commit_message):
    print(f"Fetching {NETWORK_SERVICES_PATH}...")
    file_data = api_request("GET", f"/contents/{NETWORK_SERVICES_PATH}?ref={branch_name}", token)
    file_sha = file_data["sha"]
    content = base64.b64decode(file_data["content"]).decode("utf-8")

    updated_content = content.rstrip("\n") + "\n" + svi_yaml_block
    encoded = base64.b64encode(updated_content.encode("utf-8")).decode("utf-8")

    print(f"Committing updated {NETWORK_SERVICES_PATH}...")
    api_request("PUT", f"/contents/{NETWORK_SERVICES_PATH}", token, json={
        "message": commit_message,
        "content": encoded,
        "sha": file_sha,
        "branch": branch_name,
    })
    print("  Committed.")


def open_pull_request(token, branch_name, vlan_id, vlan_name):
    print("Opening pull request...")
    pr = api_request("POST", "/pulls", token, json={
        "title": f"Add VLAN {vlan_id} ({vlan_name})",
        "head": branch_name,
        "base": BASE_BRANCH,
        "body": f"Automated VLAN provisioning request.\n\n"
                f"- **VLAN ID:** {vlan_id}\n"
                f"- **Name:** {vlan_name}\n"
                f"- **Branch:** {branch_name}\n",
    })
    print(f"  PR created: {pr['html_url']}")
    return pr["html_url"]


def provision_vlan():
    token = get_token()
    vlan_id, vlan_name, network, hosts = prompt_vlan_info()
    virtual_router, spine1_ip, spine2_ip = calculate_ips(network, hosts)

    print(f"\n  Virtual Router: {virtual_router}")
    print(f"  Spine-1:        {spine1_ip}")
    print(f"  Spine-2:        {spine2_ip}")

    branch_name = vlan_name
    svi_block = build_svi_yaml_block(vlan_id, vlan_name, virtual_router, spine1_ip, spine2_ip)

    create_branch(token, branch_name)
    update_network_services(token, branch_name, svi_block, f"Add VLAN {vlan_id} ({vlan_name})")
    pr_url = open_pull_request(token, branch_name, vlan_id, vlan_name)

    print(f"\nDone! PR: {pr_url}")


def main():
    print("=== Network Provisioning Tool ===")
    print("\n1) Add VLAN")
    print()

    choice = input("Select an option: ").strip()
    if choice == "1":
        provision_vlan()
    else:
        print("Invalid option.")
        sys.exit(1)


if __name__ == "__main__":
    main()
