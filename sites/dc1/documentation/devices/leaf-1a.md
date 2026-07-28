# leaf-1a

Serial Number: JMX2322A52C

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
  - [VLAN Interfaces](#vlan-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
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
| Management1 | OOB_MANAGEMENT | oob | MGMT | 172.31.0.22/23 | - |

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
   ip address 172.31.0.22/23
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
| DC1-LEAF1 | Vlan4094 | 10.253.1.1 | Port-Channel47 |

Dual primary detection is disabled.

### MLAG Device Configuration

```eos
!
mlag configuration
   domain-id DC1-LEAF1
   local-interface Vlan4094
   peer-address 10.253.1.1
   peer-link Port-Channel47
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

- Spanning Tree disabled for VLANs: **4094**

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
no spanning-tree vlan-id 4094
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
| 4094 | MLAG | MLAG |

### VLANs Device Configuration

```eos
!
vlan 20
   name DC1_DATA_20
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
| Ethernet1 | L2_spine-1_Ethernet1 | *trunk | *20 | *- | *- | 1 |
| Ethernet2 | L2_spine-2_Ethernet1 | *trunk | *20 | *- | *- | 1 |
| Ethernet3 | - | trunk | 20 | - | - | - |
| Ethernet4 | - | trunk | 20 | - | - | - |
| Ethernet5 | - | trunk | 20 | - | - | - |
| Ethernet6 | - | trunk | 20 | - | - | - |
| Ethernet7 | - | trunk | 20 | - | - | - |
| Ethernet8 | - | trunk | 20 | - | - | - |
| Ethernet9 | - | trunk | 20 | - | - | - |
| Ethernet10 | - | trunk | 20 | - | - | - |
| Ethernet11 | - | trunk | 20 | - | - | - |
| Ethernet12 | - | trunk | 20 | - | - | - |
| Ethernet13 | - | trunk | 20 | - | - | - |
| Ethernet14 | - | trunk | 20 | - | - | - |
| Ethernet15 | - | trunk | 20 | - | - | - |
| Ethernet16 | - | trunk | 20 | - | - | - |
| Ethernet17 | - | trunk | 20 | - | - | - |
| Ethernet18 | - | trunk | 20 | - | - | - |
| Ethernet19 | - | trunk | 20 | - | - | - |
| Ethernet20 | - | trunk | 20 | - | - | - |
| Ethernet21 | - | trunk | 20 | - | - | - |
| Ethernet22 | - | trunk | 20 | - | - | - |
| Ethernet23 | - | trunk | 20 | - | - | - |
| Ethernet24 | - | trunk | 20 | - | - | - |
| Ethernet25 | - | trunk | 20 | - | - | - |
| Ethernet26 | - | trunk | 20 | - | - | - |
| Ethernet27 | - | trunk | 20 | - | - | - |
| Ethernet28 | - | trunk | 20 | - | - | - |
| Ethernet29 | - | trunk | 20 | - | - | - |
| Ethernet30 | - | trunk | 20 | - | - | - |
| Ethernet31 | - | trunk | 20 | - | - | - |
| Ethernet32 | - | trunk | 20 | - | - | - |
| Ethernet33 | - | trunk | 20 | - | - | - |
| Ethernet34 | - | trunk | 20 | - | - | - |
| Ethernet35 | - | trunk | 20 | - | - | - |
| Ethernet36 | - | trunk | 20 | - | - | - |
| Ethernet37 | - | trunk | 20 | - | - | - |
| Ethernet38 | - | trunk | 20 | - | - | - |
| Ethernet39 | - | trunk | 20 | - | - | - |
| Ethernet40 | - | trunk | 20 | - | - | - |
| Ethernet41 | - | trunk | 20 | - | - | - |
| Ethernet42 | - | trunk | 20 | - | - | - |
| Ethernet43 | - | trunk | 20 | - | - | - |
| Ethernet44 | - | trunk | 20 | - | - | - |
| Ethernet45 | - | trunk | 20 | - | - | - |
| Ethernet46 | - | trunk | 20 | - | - | - |
| Ethernet47 | MLAG_leaf-1b_Ethernet47 | *trunk | *- | *- | *MLAG | 47 |
| Ethernet48 | MLAG_leaf-1b_Ethernet48 | *trunk | *- | *- | *MLAG | 47 |

*Inherited from Port-Channel Interface

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description L2_spine-1_Ethernet1
   no shutdown
   channel-group 1 mode active
!
interface Ethernet2
   description L2_spine-2_Ethernet1
   no shutdown
   channel-group 1 mode active
!
interface Ethernet3
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet8
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet9
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet10
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet11
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet12
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet13
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet14
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet15
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet16
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet17
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet18
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet19
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet20
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet21
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet22
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet23
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet24
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet25
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet26
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet27
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet28
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet29
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet30
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet31
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet32
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet33
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet34
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet35
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet36
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet37
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet38
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet39
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet40
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet41
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet42
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet43
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet44
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet45
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet46
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   spanning-tree portfast
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 999
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet47
   description MLAG_leaf-1b_Ethernet47
   no shutdown
   channel-group 47 mode active
!
interface Ethernet48
   description MLAG_leaf-1b_Ethernet48
   no shutdown
   channel-group 47 mode active
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | --------------------- | ------------------ | ------- | -------- |
| Port-Channel1 | L2_DC1-SPINES_Port-Channel1 | trunk | 20 | - | - | - | - | 1 | - |
| Port-Channel47 | MLAG_leaf-1b_Port-Channel47 | trunk | - | - | MLAG | - | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel1
   description L2_DC1-SPINES_Port-Channel1
   no shutdown
   switchport trunk allowed vlan 20
   switchport mode trunk
   switchport
   mlag 1
!
interface Port-Channel47
   description MLAG_leaf-1b_Port-Channel47
   no shutdown
   switchport mode trunk
   switchport trunk group MLAG
   switchport
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF | MTU | Shutdown |
| --------- | ----------- | --- | --- | -------- |
| Vlan4094 | MLAG | default | 1500 | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan4094 | default | 10.253.1.0/31 | - | - | - | - |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan4094
   description MLAG
   no shutdown
   mtu 1500
   no autostate
   ip address 10.253.1.0/31
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
| default | False |
| MGMT | False |

#### IP Routing Device Configuration

```eos
no ip routing vrf MGMT
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| MGMT | false |

## Multicast

### IP IGMP Snooping

#### IP IGMP Snooping Summary

| IGMP Snooping | Fast Leave | Interface Restart Query | Proxy | Restart Query Interval | Robustness Variable |
| ------------- | ---------- | ----------------------- | ----- | ---------------------- | ------------------- |
| Enabled | - | - | - | - | - |

#### IP IGMP Snooping Device Configuration

```eos
```

## 802.1X Port Security

### 802.1X Summary

#### 802.1X Global

| System Auth Control | Protocol LLDP Bypass | Dynamic Authorization | Dropped Packets Statistics |
| ------------------- | -------------------- | --------------------- | -------------------------- |
| True | True | True | - |

#### 802.1X Interfaces

| Interface | PAE Mode | Supplicant Profile | State | Phone Force Authorized | Reauthentication | Auth Failure Action | Host Mode | Mac Based Auth | Eapol |
| --------- | -------- | ------------------ | ----- | ---------------------- | ---------------- | ------------------- | --------- | -------------- | ----- |
| Ethernet3 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet4 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet5 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet6 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet7 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet8 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet9 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet10 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet11 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet12 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet13 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet14 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet15 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet16 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet17 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet18 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet19 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet20 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet21 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet22 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet23 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet24 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet25 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet26 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet27 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet28 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet29 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet30 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet31 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet32 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet33 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet34 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet35 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet36 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet37 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet38 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet39 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet40 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet41 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet42 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet43 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet44 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet45 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |
| Ethernet46 | authenticator | - | auto | - | True | allow vlan 999 | multi-host | True | - |

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
