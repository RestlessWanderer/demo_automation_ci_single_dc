# spine-1

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [IP Name Servers](#ip-name-servers)
  - [Domain Lookup](#domain-lookup)
  - [Clock Settings](#clock-settings)
  - [NTP](#ntp)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [Enable Password](#enable-password)
  - [RADIUS Server](#radius-server)
  - [IP RADIUS Source Interfaces](#ip-radius-source-interfaces)
  - [AAA Server Groups](#aaa-server-groups)
  - [AAA Authentication](#aaa-authentication)
  - [AAA Accounting](#aaa-accounting)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Device Configuration](#internal-vlan-allocation-policy-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
- [802.1X Port Security](#8021x-port-security)
  - [802.1X Summary](#8021x-summary)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | 172.31.0.27/23 | 172.31.0.5 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | OOB_MANAGEMENT | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description OOB_MANAGEMENT
   no shutdown
   vrf MGMT
   ip address 172.31.0.27/23
```

### IP Name Servers

#### IP Name Servers Summary

| Name Server | VRF | Priority |
| ----------- | --- | -------- |
| 1.1.1.1 | MGMT | - |

#### IP Name Servers Device Configuration

```eos
ip name-server vrf MGMT 1.1.1.1
```

### Domain Lookup

#### DNS Domain Lookup Summary

| Source interface | vrf |
| ---------------- | --- |
| Management1 | MGMT |

#### DNS Domain Lookup Device Configuration

```eos
ip domain lookup vrf MGMT source-interface Management1
```

### Clock Settings

#### Clock Timezone Settings

Clock Timezone is set to **America/Detroit**.

#### Clock Device Configuration

```eos
!
clock timezone America/Detroit
```

### NTP

#### NTP Summary

##### NTP Local Interface

| Interface | VRF |
| --------- | --- |
| Management1 | MGMT |

##### NTP Servers

NTP servers VRF: MGMT

| Server | Preferred | Burst | iBurst | Version | Min Poll | Max Poll | Local-interface | Key |
| ------ | --------- | ----- | ------ | ------- | -------- | -------- | --------------- | --- |
| 129.6.15.28 | True | - | - | - | - | - | - | - |
| 129.6.15.29 | - | - | - | - | - | - | - | - |

#### NTP Device Configuration

```eos
!
ntp local-interface vrf MGMT Management1
ntp server vrf MGMT 129.6.15.28 prefer
ntp server vrf MGMT 129.6.15.29
```

### Management API HTTP

#### Management API HTTP Summary

| HTTP | HTTPS | UNIX-Socket | Default Services |
| ---- | ----- | ----------- | ---------------- |
| False | True | - | - |

#### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| default | - | - |
| MGMT | - | - |

#### Management API HTTP Device Configuration

```eos
!
management api http-commands
   no shutdown
   !
   vrf MGMT
      no shutdown
   !
   vrf default
      no shutdown
```

## Authentication

### Local Users

#### Local Users Summary

| User | Privilege | Role | Disabled | Shell |
| ---- | --------- | ---- | -------- | ----- |
| cvpadmin | 15 | network-admin | False | - |

#### Local Users Device Configuration

```eos
!
username cvpadmin privilege 15 role network-admin secret sha512 <removed>
```

### Enable Password

Enable password has been disabled

### RADIUS Server

#### RADIUS Server Hosts

| VRF | RADIUS Servers | TLS | TLS Port | SSL Profile | Timeout | Retransmit |
| --- | -------------- | --- | ---- | ----------- | ------- | ---------- |
| MGMT | 1.1.1.1 | - | - | - | - | - |

#### RADIUS Server Device Configuration

```eos
!
radius-server host 1.1.1.1 vrf MGMT key 7 <removed>
```

### IP RADIUS Source Interfaces

#### IP RADIUS Source Interfaces

| VRF | Source Interface Name |
| --- | --------------- |
| MGMT | Management1 |

#### IP SOURCE Source Interfaces Device Configuration

```eos
!
ip radius vrf MGMT source-interface Management1
```

### AAA Server Groups

#### AAA Server Groups Summary

| Server Group Name | Type | VRF | IP address |
| ----------------- | ---- | --- | ---------- |
| DOT1X | radius | MGMT | 1.1.1.1 |

#### AAA Server Groups Device Configuration

```eos
!
aaa group server radius DOT1X
   server 1.1.1.1 vrf MGMT
```

### AAA Authentication

#### AAA Authentication Summary

| Type | Sub-type | User Stores |
| ---- | -------- | ---------- |

#### AAA Authentication Device Configuration

```eos
aaa authentication dot1x default group DOT1X
!
```

### AAA Accounting

#### AAA Accounting Summary

| Type | Commands | Record type | Groups | Logging |
| ---- | -------- | ----------- | ------ | ------- |
| Dot1x - Default | - | start-stop | radius(multicast) | False |

#### AAA Accounting Device Configuration

```eos
aaa accounting dot1x default start-stop group radius
```

## Monitoring

### TerminAttr Daemon

#### TerminAttr Daemon Summary

| CV Compression | CloudVision Servers | VRF | Authentication | Smash Excludes | Ingest Exclude | Bypass AAA |
| -------------- | ------------------- | --- | -------------- | -------------- | -------------- | ---------- |
| gzip | 172.31.0.5:9910 | MGMT | token,/tmp/token | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | True |

#### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvaddr=172.31.0.5:9910 -cvauth=token,/tmp/token -cvvrf=MGMT -disableaaa -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -taillogs -cvsourceintf=Management1
   no shutdown
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **none**

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode none
```

## Internal VLAN Allocation Policy

### Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ----------------- | --------------- | ------------ |
| ascending | 1006 | 1199 |

### Internal VLAN Allocation Policy Device Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

<<<<<<< HEAD
=======
## VLANs

### VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 20 | DC1_DATA_20 | - |
| 21 | DC1_DATA_21 | - |
| 22 | DC1_DATA_22 | - |
| 23 | DC1_DATA_23 | - |
| 25 | v25 | - |
| 999 | BLACKHOLE | - |
| 4093 | MLAG_L3 | MLAG |
| 4094 | MLAG | MLAG |

### VLANs Device Configuration

```eos
!
vlan 20
   name DC1_DATA_20
!
vlan 21
   name DC1_DATA_21
!
vlan 22
   name DC1_DATA_22
!
vlan 23
   name DC1_DATA_23
!
vlan 25
   name v25
!
vlan 999
   name BLACKHOLE
!
vlan 4093
   name MLAG_L3
   trunk group MLAG
!
vlan 4094
   name MLAG
   trunk group MLAG
```

>>>>>>> 7ba9e166a0e0222f43d0e392344107259f94e422
## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
<<<<<<< HEAD
=======
| Ethernet1 | L2_leaf-1a_Ethernet1 | *trunk | *20-23,25,999 | *- | *- | 1 |
| Ethernet2 | L2_leaf-1b_Ethernet1 | *trunk | *20-23,25,999 | *- | *- | 1 |
| Ethernet3 | L2_leaf-2a_Ethernet1 | *trunk | *20-23,25,999 | *- | *- | 3 |
| Ethernet4 | L2_leaf-2b_Ethernet1 | *trunk | *20-23,25,999 | *- | *- | 3 |
| Ethernet47 | MLAG_spine-2_Ethernet47 | *trunk | *- | *- | *MLAG | 47 |
| Ethernet48 | MLAG_spine-2_Ethernet48 | *trunk | *- | *- | *MLAG | 47 |
>>>>>>> 7ba9e166a0e0222f43d0e392344107259f94e422

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF | MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | --- | --- | -------- | ------ | ------- |
| Ethernet1 | P2P_leaf-1a_Ethernet1 | - | 100.100.1.0/31 | default | 1500 | False | - | - |
| Ethernet2 | P2P_leaf-1b_Ethernet1 | - | 100.100.1.4/31 | default | 1500 | False | - | - |
| Ethernet3 | P2P_leaf-2a_Ethernet1 | - | 100.100.1.8/31 | default | 1500 | False | - | - |
| Ethernet4 | P2P_leaf-2b_Ethernet1 | - | 100.100.1.12/31 | default | 1500 | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_leaf-1a_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 100.100.1.0/31
!
interface Ethernet2
   description P2P_leaf-1b_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 100.100.1.4/31
!
interface Ethernet3
   description P2P_leaf-2a_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 100.100.1.8/31
!
interface Ethernet4
   description P2P_leaf-2b_Ethernet1
   no shutdown
<<<<<<< HEAD
   mtu 1500
   no switchport
   ip address 100.100.1.12/31
=======
   channel-group 47 mode active
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | --------------------- | ------------------ | ------- | -------- |
| Port-Channel1 | L2_DC1-LEAF1_Port-Channel1 | trunk | 20-23,25,999 | - | - | - | - | 1 | - |
| Port-Channel3 | L2_DC1-LEAF2_Port-Channel1 | trunk | 20-23,25,999 | - | - | - | - | 3 | - |
| Port-Channel47 | MLAG_spine-2_Port-Channel47 | trunk | - | - | MLAG | - | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel1
   description L2_DC1-LEAF1_Port-Channel1
   no shutdown
   switchport trunk allowed vlan 20-23,25,999
   switchport mode trunk
   switchport
   mlag 1
!
interface Port-Channel3
   description L2_DC1-LEAF2_Port-Channel1
   no shutdown
   switchport trunk allowed vlan 20-23,25,999
   switchport mode trunk
   switchport
   mlag 3
!
interface Port-Channel47
   description MLAG_spine-2_Port-Channel47
   no shutdown
   switchport mode trunk
   switchport trunk group MLAG
   switchport
>>>>>>> 7ba9e166a0e0222f43d0e392344107259f94e422
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | ROUTER_ID | default | 10.252.1.1/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | ROUTER_ID | default | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description ROUTER_ID
   no shutdown
   ip address 10.252.1.1/32
<<<<<<< HEAD
=======
   ip ospf area 0.0.0.0
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF | MTU | Shutdown |
| --------- | ----------- | --- | --- | -------- |
| Vlan20 | DC1_DATA_20 | default | - | False |
| Vlan21 | DC1_DATA_21 | default | - | False |
| Vlan22 | DC1_DATA_22 | default | - | False |
| Vlan23 | DC1_DATA_23 | default | - | False |
| Vlan25 | v25 | default | - | False |
| Vlan999 | BLACKHOLE | default | - | False |
| Vlan4093 | MLAG_L3 | default | 1500 | False |
| Vlan4094 | MLAG | default | 1500 | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan20 | default | 10.1.20.2/24 | - | 10.1.20.1 | - | - |
| Vlan21 | default | 10.1.21.2/24 | - | 10.1.21.1 | - | - |
| Vlan22 | default | 10.1.22.2/24 | - | 10.1.22.1 | - | - |
| Vlan23 | default | 10.1.23.2/24 | - | 10.1.23.1 | - | - |
| Vlan25 | default | 10.25.25.2/24 | - | 10.25.25.1 | - | - |
| Vlan999 | default | 10.200.34.2/24 | - | 10.200.34.1 | - | - |
| Vlan4093 | default | 10.253.1.2/31 | - | - | - | - |
| Vlan4094 | default | 10.253.1.0/31 | - | - | - | - |

##### OSPF

| Interface | OSPF Network Point to Point | OSPF Area | OSPF Cost | OSPF Authentication | IPv6 OSPF Process ID | IPv6 OSPF Area | IPv6 OSPF Network Point to Point |
| --------- | --------------------------- | --------- | --------- | ------------------- | -------------------- | -------------- | -------------------------------- |
| Vlan4093 | True | 0.0.0.0 | - | - | - | - | - |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan20
   description DC1_DATA_20
   no shutdown
   ip address 10.1.20.2/24
   ip virtual-router address 10.1.20.1
!
interface Vlan21
   description DC1_DATA_21
   no shutdown
   ip address 10.1.21.2/24
   ip virtual-router address 10.1.21.1
!
interface Vlan22
   description DC1_DATA_22
   no shutdown
   ip address 10.1.22.2/24
   ip virtual-router address 10.1.22.1
!
interface Vlan23
   description DC1_DATA_23
   no shutdown
   ip address 10.1.23.2/24
   ip virtual-router address 10.1.23.1
!
interface Vlan25
   description v25
   no shutdown
   ip address 10.25.25.2/24
   ip virtual-router address 10.25.25.1
!
interface Vlan999
   description BLACKHOLE
   no shutdown
   ip address 10.200.34.2/24
   ip virtual-router address 10.200.34.1
!
interface Vlan4093
   description MLAG_L3
   no shutdown
   mtu 1500
   ip address 10.253.1.2/31
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
!
interface Vlan4094
   description MLAG
   no shutdown
   mtu 1500
   no autostate
   ip address 10.253.1.0/31
>>>>>>> 7ba9e166a0e0222f43d0e392344107259f94e422
```

## Routing

### Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| MGMT | False |

#### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| MGMT | false |

### Static Routes

#### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP | Exit interface | Administrative Distance | Tag | Route Name | Metric |
| --- | ------------------ | ----------- | -------------- | ----------------------- | --- | ---------- | ------ |
| MGMT | 0.0.0.0/0 | 172.31.0.5 | - | 1 | - | - | - |

#### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 172.31.0.5
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65100 | 10.252.1.1 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| maximum-paths 4 |

#### Router BGP Peer Groups

##### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Next-hop unchanged | True |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 3 |
| Send community | all |
| Maximum routes | 0 (no limit) |

##### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 256000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 10.252.1.3 | 65101 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.252.1.4 | 65101 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.252.1.5 | 65102 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.252.1.6 | 65102 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 100.100.1.1 | 65101 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 100.100.1.5 | 65101 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 100.100.1.9 | 65102 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 100.100.1.13 | 65102 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | Peer-tag In | Peer-tag Out | Encapsulation | Next-hop-self Source Interface |
| ---------- | -------- | ------------ | ------------- | ----------- | ------------ | ------------- | ------------------------------ |
| EVPN-OVERLAY-PEERS | True | - | - | - | - | default | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65100
   router-id 10.252.1.1
   no bgp default ipv4-unicast
   maximum-paths 4
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS next-hop-unchanged
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 256000
   neighbor 10.252.1.3 peer group EVPN-OVERLAY-PEERS
   neighbor 10.252.1.3 remote-as 65101
   neighbor 10.252.1.3 description leaf-1a_Loopback0
   neighbor 10.252.1.4 peer group EVPN-OVERLAY-PEERS
   neighbor 10.252.1.4 remote-as 65101
   neighbor 10.252.1.4 description leaf-1b_Loopback0
   neighbor 10.252.1.5 peer group EVPN-OVERLAY-PEERS
   neighbor 10.252.1.5 remote-as 65102
   neighbor 10.252.1.5 description leaf-2a_Loopback0
   neighbor 10.252.1.6 peer group EVPN-OVERLAY-PEERS
   neighbor 10.252.1.6 remote-as 65102
   neighbor 10.252.1.6 description leaf-2b_Loopback0
   neighbor 100.100.1.1 peer group IPv4-UNDERLAY-PEERS
   neighbor 100.100.1.1 remote-as 65101
   neighbor 100.100.1.1 description leaf-1a_Ethernet1
   neighbor 100.100.1.5 peer group IPv4-UNDERLAY-PEERS
   neighbor 100.100.1.5 remote-as 65101
   neighbor 100.100.1.5 description leaf-1b_Ethernet1
   neighbor 100.100.1.9 peer group IPv4-UNDERLAY-PEERS
   neighbor 100.100.1.9 remote-as 65102
   neighbor 100.100.1.9 description leaf-2a_Ethernet1
   neighbor 100.100.1.13 peer group IPv4-UNDERLAY-PEERS
   neighbor 100.100.1.13 remote-as 65102
   neighbor 100.100.1.13 description leaf-2b_Ethernet1
   redistribute connected route-map RM-CONN-2-BGP
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
```

## BFD

### Router BFD

#### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 300 | 300 | 3 |

#### Router BFD Device Configuration

```eos
!
router bfd
   multihop interval 300 min-rx 300 multiplier 3
```

## Filters

### Prefix-lists

#### Prefix-lists Summary

##### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 10.252.1.0/24 eq 32 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 10.252.1.0/24 eq 32
```

### Route-maps

#### Route-maps Summary

##### RM-CONN-2-BGP

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY | - | - | - |

#### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
```

## 802.1X Port Security

### 802.1X Summary

#### 802.1X Global

| System Auth Control | Protocol LLDP Bypass | Dynamic Authorization | Dropped Packets Statistics |
| ------------------- | -------------------- | --------------------- | -------------------------- |
| True | True | True | - |

#### Dot1x Configuration

```eos
!
dot1x system-auth-control
dot1x protocol lldp bypass
dot1x protocol bpdu bypass
dot1x dynamic-authorization
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
```
