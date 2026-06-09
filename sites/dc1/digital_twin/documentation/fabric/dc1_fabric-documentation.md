# dc1_fabric

## Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| dc1_fabric | l2leaf | leaf-1a | 172.31.0.22/23 | vEOS-lab | Provisioned | - |
| dc1_fabric | l2leaf | leaf-1b | 172.31.0.23/23 | vEOS-lab | Provisioned | - |
| dc1_fabric | l2leaf | leaf-2a | 172.31.0.20/23 | vEOS-lab | Provisioned | - |
| dc1_fabric | l2leaf | leaf-2b | 172.31.0.21/23 | vEOS-lab | Provisioned | - |
| dc1_fabric | l3spine | spine-1 | 172.31.0.27/23 | vEOS-lab | Provisioned | - |
| dc1_fabric | l3spine | spine-2 | 172.31.0.28/23 | vEOS-lab | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l2leaf | leaf-1a | Ethernet1 | l3spine | spine-1 | Ethernet1 |
| l2leaf | leaf-1a | Ethernet2 | l3spine | spine-2 | Ethernet1 |
| l2leaf | leaf-1a | Ethernet47 | mlag_peer | leaf-1b | Ethernet47 |
| l2leaf | leaf-1a | Ethernet48 | mlag_peer | leaf-1b | Ethernet48 |
| l2leaf | leaf-1b | Ethernet1 | l3spine | spine-1 | Ethernet2 |
| l2leaf | leaf-1b | Ethernet2 | l3spine | spine-2 | Ethernet2 |
| l2leaf | leaf-2a | Ethernet1 | l3spine | spine-1 | Ethernet3 |
| l2leaf | leaf-2a | Ethernet2 | l3spine | spine-2 | Ethernet3 |
| l2leaf | leaf-2a | Ethernet23 | mlag_peer | leaf-2b | Ethernet23 |
| l2leaf | leaf-2a | Ethernet24 | mlag_peer | leaf-2b | Ethernet24 |
| l2leaf | leaf-2b | Ethernet1 | l3spine | spine-1 | Ethernet4 |
| l2leaf | leaf-2b | Ethernet2 | l3spine | spine-2 | Ethernet4 |
| l3spine | spine-1 | Ethernet47 | mlag_peer | spine-2 | Ethernet47 |
| l3spine | spine-1 | Ethernet48 | mlag_peer | spine-2 | Ethernet48 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.252.1.0/24 | 256 | 2 | 0.79 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| dc1_fabric | spine-1 | 10.252.1.1/32 |
| dc1_fabric | spine-2 | 10.252.1.2/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------ | ------------------- | ------------------ | ------------------ |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
