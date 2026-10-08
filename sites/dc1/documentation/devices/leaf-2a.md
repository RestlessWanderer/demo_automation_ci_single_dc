# leaf-2a

Serial Number: HBG25390SS3

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [IP Name Servers](#ip-name-servers)
  - [Domain Lookup](#domain-lookup)
  - [Clock Settings](#clock-settings)
  - [NTP](#ntp)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Enable Password](#enable-password)
  - [RADIUS Server](#radius-server)
  - [IP RADIUS Source Interfaces](#ip-radius-source-interfaces)
  - [AAA Server Groups](#aaa-server-groups)
  - [AAA Authentication](#aaa-authentication)
  - [AAA Accounting](#aaa-accounting)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
- [MLAG](#mlag)
  - [MLAG Summary](#mlag-summary)
  - [MLAG Device Configuration](#mlag-device-configuration)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Device Configuration](#internal-vlan-allocation-policy-device-configuration)
- [VLANs](#vlans)
  - [VLANs Summary](#vlans-summary)
  - [VLANs Device Configuration](#vlans-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
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
| Management1 | OOB_MANAGEMENT | oob | MGMT | 172.31.0.20/23 | 172.31.0.5 |

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
   ip address 172.31.0.20/23
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
| MGMT | - | - |

#### Management API HTTP Device Configuration

```eos
!
management api http-commands
   no shutdown
   !
   vrf MGMT
      no shutdown
```

## Authentication

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
| gzip | apiserver.cv-staging.corp.arista.io:443 | MGMT | token-secure,/tmp/cv-onboarding-token | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | True |

#### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvaddr=apiserver.cv-staging.corp.arista.io:443 -cvauth=token-secure,/tmp/cv-onboarding-token -cvvrf=MGMT -disableaaa -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -taillogs -cvsourceintf=Management1
   no shutdown
```

## MLAG

### MLAG Summary

| Domain-id | Local-interface | Peer-address | Peer-link |
| --------- | --------------- | ------------ | --------- |
| DC1-LEAF2 | Vlan4094 | 10.253.1.1 | Port-Channel23 |

Dual primary detection is disabled.

### MLAG Device Configuration

```eos
!
mlag configuration
   domain-id DC1-LEAF2
   local-interface Vlan4094
   peer-address 10.253.1.1
   peer-link Port-Channel23
   reload-delay mlag 300
   reload-delay non-mlag 330
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **mstp**

#### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 16384 |

#### Global Spanning-Tree Settings

- Spanning Tree disabled for VLANs: **4093-4094**

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
no spanning-tree vlan-id 4093-4094
spanning-tree mst 0 priority 16384
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

## VLANs

### VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 20 | DC1_DATA_20 | - |
| 21 | DC1_DATA_21 | - |
| 22 | DC1_DATA_22 | - |
| 23 | DC1_DATA_23 | - |
| 25 | v25 | - |
| 33 | v33 | - |
| 999 | BLACKHOLE | - |
| 3009 | MLAG_L3_VRF_OVERLAY | MLAG |
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
vlan 33
   name v33
!
vlan 999
   name BLACKHOLE
!
vlan 3009
   name MLAG_L3_VRF_OVERLAY
   trunk group MLAG
!
vlan 4093
   name MLAG_L3
   trunk group MLAG
!
vlan 4094
   name MLAG
   trunk group MLAG
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet3 | SERVER_host1-11 | access | 21 | - | - | - |
| Ethernet23 | MLAG_leaf-2b_Ethernet23 | *trunk | *- | *- | *MLAG | 23 |
| Ethernet24 | MLAG_leaf-2b_Ethernet24 | *trunk | *- | *- | *MLAG | 23 |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF | MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | --- | --- | -------- | ------ | ------- |
| Ethernet1 | P2P_spine-1_Ethernet3 | - | 100.100.1.9/31 | default | 1500 | False | - | - |
| Ethernet2 | P2P_spine-2_Ethernet3 | - | 100.100.1.11/31 | default | 1500 | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_spine-1_Ethernet3
   no shutdown
   mtu 1500
   no switchport
   ip address 100.100.1.9/31
!
interface Ethernet2
   description P2P_spine-2_Ethernet3
   no shutdown
   mtu 1500
   no switchport
   ip address 100.100.1.11/31
!
interface Ethernet3
   description SERVER_host1-11
   no shutdown
   switchport access vlan 21
   switchport mode access
   switchport
!
interface Ethernet23
   description MLAG_leaf-2b_Ethernet23
   no shutdown
   channel-group 23 mode active
!
interface Ethernet24
   description MLAG_leaf-2b_Ethernet24
   no shutdown
   channel-group 23 mode active
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | --------------------- | ------------------ | ------- | -------- |
| Port-Channel23 | MLAG_leaf-2b_Port-Channel23 | trunk | - | - | MLAG | - | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel23
   description MLAG_leaf-2b_Port-Channel23
   no shutdown
   switchport mode trunk
   switchport trunk group MLAG
   switchport
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | ROUTER_ID | default | 10.252.1.5/32 |
| Loopback1 | VXLAN_TUNNEL_SOURCE | default | 10.254.1.5/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | ROUTER_ID | default | - |
| Loopback1 | VXLAN_TUNNEL_SOURCE | default | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description ROUTER_ID
   no shutdown
   ip address 10.252.1.5/32
!
interface Loopback1
   description VXLAN_TUNNEL_SOURCE
   no shutdown
   ip address 10.254.1.5/32
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF | MTU | Shutdown |
| --------- | ----------- | --- | --- | -------- |
| Vlan20 | DC1_DATA_20 | OVERLAY | - | False |
| Vlan21 | DC1_DATA_21 | OVERLAY | - | False |
| Vlan22 | DC1_DATA_22 | OVERLAY | - | False |
| Vlan23 | DC1_DATA_23 | OVERLAY | - | False |
| Vlan25 | v25 | OVERLAY | - | False |
| Vlan33 | v33 | OVERLAY | - | False |
| Vlan999 | BLACKHOLE | OVERLAY | - | False |
| Vlan3009 | MLAG_L3_VRF_OVERLAY | OVERLAY | 1500 | False |
| Vlan4093 | MLAG_L3 | default | 1500 | False |
| Vlan4094 | MLAG | default | 1500 | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan20 | OVERLAY | - | - | - | - | - |
| Vlan21 | OVERLAY | - | - | - | - | - |
| Vlan22 | OVERLAY | - | - | - | - | - |
| Vlan23 | OVERLAY | - | - | - | - | - |
| Vlan25 | OVERLAY | - | - | - | - | - |
| Vlan33 | OVERLAY | - | - | - | - | - |
| Vlan999 | OVERLAY | - | - | - | - | - |
| Vlan3009 | OVERLAY | 10.250.1.0/31 | - | - | - | - |
| Vlan4093 | default | 10.250.1.0/31 | - | - | - | - |
| Vlan4094 | default | 10.253.1.0/31 | - | - | - | - |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan20
   description DC1_DATA_20
   no shutdown
   vrf OVERLAY
!
interface Vlan21
   description DC1_DATA_21
   no shutdown
   vrf OVERLAY
!
interface Vlan22
   description DC1_DATA_22
   no shutdown
   vrf OVERLAY
!
interface Vlan23
   description DC1_DATA_23
   no shutdown
   vrf OVERLAY
!
interface Vlan25
   description v25
   no shutdown
   vrf OVERLAY
!
interface Vlan33
   description v33
   no shutdown
   vrf OVERLAY
!
interface Vlan999
   description BLACKHOLE
   no shutdown
   vrf OVERLAY
!
interface Vlan3009
   description MLAG_L3_VRF_OVERLAY
   no shutdown
   mtu 1500
   vrf OVERLAY
   ip address 10.250.1.0/31
!
interface Vlan4093
   description MLAG_L3
   no shutdown
   mtu 1500
   ip address 10.250.1.0/31
!
interface Vlan4094
   description MLAG
   no shutdown
   mtu 1500
   no autostate
   ip address 10.253.1.0/31
```

### VXLAN Interface

#### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Loopback1 |
| UDP port | 4789 |
| EVPN MLAG Shared Router MAC | mlag-system-id |

##### VLAN to VNI, Flood List and Multicast Group Mappings

| VLAN | VNI | Flood List | Multicast Group |
| ---- | --- | ---------- | --------------- |
| 20 | 10020 | - | - |
| 21 | 10021 | - | - |
| 22 | 10022 | - | - |
| 23 | 10023 | - | - |
| 25 | 10025 | - | - |
| 33 | 10033 | - | - |
| 999 | 10999 | - | - |

##### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Overlay Multicast Group to Encap Mappings |
| --- | --- | ----------------------------------------- |
| OVERLAY | 10 | - |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description leaf-2a_VTEP
   vxlan source-interface Loopback1
   vxlan virtual-router encapsulation mac-address mlag-system-id
   vxlan udp-port 4789
   vxlan vlan 20 vni 10020
   vxlan vlan 21 vni 10021
   vxlan vlan 22 vni 10022
   vxlan vlan 23 vni 10023
   vxlan vlan 25 vni 10025
   vxlan vlan 33 vni 10033
   vxlan vlan 999 vni 10999
   vxlan vrf OVERLAY vni 10
```

## Routing

### Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

### Virtual Router MAC Address

#### Virtual Router MAC Address Summary

Virtual Router MAC Address: 00:1c:73:00:00:99

#### Virtual Router MAC Address Device Configuration

```eos
!
ip virtual-router mac-address 00:1c:73:00:00:99
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| MGMT | False |
| OVERLAY | True |

#### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
ip routing vrf OVERLAY
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| MGMT | false |
| OVERLAY | false |

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
| 65102 | 10.252.1.5 |

| BGP Tuning |
| ---------- |
| update wait-install |
| no bgp default ipv4-unicast |
| maximum-paths 4 |

#### Router BGP Peer Groups

##### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
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

##### MLAG-IPv4-UNDERLAY-PEER

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65102 |
| Next-hop self | True |
| Send community | all |
| Maximum routes | 256000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 10.250.1.1 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | default | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |
| 10.252.1.1 | 65100 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.252.1.2 | 65100 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 100.100.1.8 | 65100 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 100.100.1.10 | 65100 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 10.250.1.1 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | OVERLAY | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | Peer-tag In | Peer-tag Out | Encapsulation | Next-hop-self Source Interface |
| ---------- | -------- | ------------ | ------------- | ----------- | ------------ | ------------- | ------------------------------ |
| EVPN-OVERLAY-PEERS | True | - | - | - | - | default | - |

#### Router BGP VLANs

| VLAN | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute |
| ---- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ |
| 20 | 10.252.1.5:10020 | 10020:10020 | - | - | learned<br>dot1x |
| 21 | 10.252.1.5:10021 | 10021:10021 | - | - | learned<br>dot1x |
| 22 | 10.252.1.5:10022 | 10022:10022 | - | - | learned<br>dot1x |
| 23 | 10.252.1.5:10023 | 10023:10023 | - | - | learned<br>dot1x |
| 25 | 10.252.1.5:10025 | 10025:10025 | - | - | learned<br>dot1x |
| 33 | 10.252.1.5:10033 | 10033:10033 | - | - | learned<br>dot1x |
| 999 | 10.252.1.5:10999 | 10999:10999 | - | - | learned<br>dot1x |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute | Graceful Restart |
| --- | ------------------- | ------------ | ---------------- |
| OVERLAY | 10.252.1.5:10 | connected | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65102
   router-id 10.252.1.5
   update wait-install
   no bgp default ipv4-unicast
   maximum-paths 4
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 256000
   neighbor MLAG-IPv4-UNDERLAY-PEER peer group
   neighbor MLAG-IPv4-UNDERLAY-PEER remote-as 65102
   neighbor MLAG-IPv4-UNDERLAY-PEER next-hop-self
   neighbor MLAG-IPv4-UNDERLAY-PEER description leaf-2b
   neighbor MLAG-IPv4-UNDERLAY-PEER route-map RM-MLAG-PEER-IN in
   neighbor MLAG-IPv4-UNDERLAY-PEER send-community
   neighbor MLAG-IPv4-UNDERLAY-PEER maximum-routes 256000
   neighbor 10.250.1.1 peer group MLAG-IPv4-UNDERLAY-PEER
   neighbor 10.250.1.1 description leaf-2b_Vlan4093
   neighbor 10.252.1.1 peer group EVPN-OVERLAY-PEERS
   neighbor 10.252.1.1 remote-as 65100
   neighbor 10.252.1.1 description spine-1_Loopback0
   neighbor 10.252.1.2 peer group EVPN-OVERLAY-PEERS
   neighbor 10.252.1.2 remote-as 65100
   neighbor 10.252.1.2 description spine-2_Loopback0
   neighbor 100.100.1.8 peer group IPv4-UNDERLAY-PEERS
   neighbor 100.100.1.8 remote-as 65100
   neighbor 100.100.1.8 description spine-1_Ethernet3
   neighbor 100.100.1.10 peer group IPv4-UNDERLAY-PEERS
   neighbor 100.100.1.10 remote-as 65100
   neighbor 100.100.1.10 description spine-2_Ethernet3
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan 20
      rd 10.252.1.5:10020
      route-target both 10020:10020
      redistribute dot1x
      redistribute learned
   !
   vlan 21
      rd 10.252.1.5:10021
      route-target both 10021:10021
      redistribute dot1x
      redistribute learned
   !
   vlan 22
      rd 10.252.1.5:10022
      route-target both 10022:10022
      redistribute dot1x
      redistribute learned
   !
   vlan 23
      rd 10.252.1.5:10023
      route-target both 10023:10023
      redistribute dot1x
      redistribute learned
   !
   vlan 25
      rd 10.252.1.5:10025
      route-target both 10025:10025
      redistribute dot1x
      redistribute learned
   !
   vlan 33
      rd 10.252.1.5:10033
      route-target both 10033:10033
      redistribute dot1x
      redistribute learned
   !
   vlan 999
      rd 10.252.1.5:10999
      route-target both 10999:10999
      redistribute dot1x
      redistribute learned
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
      neighbor MLAG-IPv4-UNDERLAY-PEER activate
   !
   vrf OVERLAY
      rd 10.252.1.5:10
      route-target import evpn 10:10
      route-target export evpn 10:10
      router-id 10.252.1.5
      update wait-install
      neighbor 10.250.1.1 peer group MLAG-IPv4-UNDERLAY-PEER
      neighbor 10.250.1.1 description leaf-2b_Vlan3009
      redistribute connected route-map RM-CONN-2-BGP-VRFS
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

## Multicast

### IP IGMP Snooping

#### IP IGMP Snooping Summary

| IGMP Snooping | Fast Leave | Interface Restart Query | Proxy | Restart Query Interval | Robustness Variable |
| ------------- | ---------- | ----------------------- | ----- | ---------------------- | ------------------- |
| Enabled | - | - | - | - | - |

#### IP IGMP Snooping Device Configuration

```eos
```

## Filters

### Prefix-lists

#### Prefix-lists Summary

##### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 10.252.1.0/24 eq 32 |
| 20 | permit 10.254.1.0/24 eq 32 |

##### PL-MLAG-PEER-VRFS

| Sequence | Action |
| -------- | ------ |
| 10 | permit 10.250.1.0/31 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 10.252.1.0/24 eq 32
   seq 20 permit 10.254.1.0/24 eq 32
!
ip prefix-list PL-MLAG-PEER-VRFS
   seq 10 permit 10.250.1.0/31
```

### Route-maps

#### Route-maps Summary

##### RM-CONN-2-BGP

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY | - | - | - |

##### RM-CONN-2-BGP-VRFS

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | deny | ip address prefix-list PL-MLAG-PEER-VRFS | - | - | - |
| 20 | permit | - | - | - | - |

##### RM-MLAG-PEER-IN

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | - | origin incomplete | - | - |

#### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
!
route-map RM-CONN-2-BGP-VRFS deny 10
   match ip address prefix-list PL-MLAG-PEER-VRFS
!
route-map RM-CONN-2-BGP-VRFS permit 20
!
route-map RM-MLAG-PEER-IN permit 10
   description Make routes learned over MLAG Peer-link less preferred on spines to ensure optimal routing
   set origin incomplete
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
| OVERLAY | enabled |

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
!
vrf instance OVERLAY
```
