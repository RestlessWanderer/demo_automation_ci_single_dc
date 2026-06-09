# leaf-1b

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
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | 172.31.0.23/23 | - |

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
   ip address 172.31.0.23/23
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

## MLAG

### MLAG Summary

| Domain-id | Local-interface | Peer-address | Peer-link |
| --------- | --------------- | ------------ | --------- |
| DC1-LEAF1 | Vlan4094 | 10.253.1.0 | Port-Channel47 |

Dual primary detection is disabled.

### MLAG Device Configuration

```eos
!
mlag configuration
   domain-id DC1-LEAF1
   local-interface Vlan4094
   peer-address 10.253.1.0
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
| 110 | DC1_DATA_110 | - |
| 120 | DC1_DATA_120 | - |
| 130 | DC1_DATA_130 | - |
| 131 | DC1_DATA_131 | - |
| 132 | DC1_DATA_132 | - |
| 133 | DC1_DATA_133 | - |
| 134 | DC1_DATA_134 | - |
| 135 | DC1_DATA_135 | - |
| 136 | DC1_DATA_136 | - |
| 137 | DC1_DATA_137 | - |
| 138 | DC1_DATA_138 | - |
| 139 | DC1_DATA_139 | - |
| 140 | DC1_DATA_140 | - |
| 141 | DC1_DATA_141 | - |
| 142 | DC1_DATA_142 | - |
| 143 | DC1_DATA_143 | - |
| 144 | DC1_DATA_144 | - |
| 145 | DC1_DATA_145 | - |
| 146 | DC1_DATA_146 | - |
| 147 | DC1_DATA_147 | - |
| 148 | DC1_DATA_148 | - |
| 149 | DC1_DATA_149 | - |
| 150 | DC1_DATA_150 | - |
| 151 | DC1_DATA_151 | - |
| 152 | DC1_DATA_152 | - |
| 153 | DC1_DATA_153 | - |
| 154 | DC1_DATA_154 | - |
| 155 | DC1_DATA_155 | - |
| 156 | DC1_DATA_156 | - |
| 157 | DC1_DATA_157 | - |
| 158 | DC1_DATA_158 | - |
| 159 | DC1_DATA_159 | - |
| 160 | DC1_DATA_160 | - |
| 161 | DC1_DATA_161 | - |
| 162 | DC1_DATA_162 | - |
| 163 | DC1_DATA_163 | - |
| 164 | DC1_DATA_164 | - |
| 165 | DC1_DATA_165 | - |
| 166 | DC1_DATA_166 | - |
| 167 | DC1_DATA_167 | - |
| 168 | DC1_DATA_168 | - |
| 169 | DC1_DATA_169 | - |
| 170 | DC1_DATA_170 | - |
| 171 | DC1_DATA_171 | - |
| 172 | DC1_DATA_172 | - |
| 173 | DC1_DATA_173 | - |
| 174 | DC1_DATA_174 | - |
| 175 | DC1_DATA_175 | - |
| 176 | DC1_DATA_176 | - |
| 177 | DC1_DATA_177 | - |
| 178 | DC1_DATA_178 | - |
| 179 | DC1_DATA_179 | - |
| 180 | DC1_DATA_180 | - |
| 181 | DC1_DATA_181 | - |
| 182 | DC1_DATA_182 | - |
| 183 | DC1_DATA_183 | - |
| 184 | DC1_DATA_184 | - |
| 185 | DC1_DATA_185 | - |
| 186 | DC1_DATA_186 | - |
| 187 | DC1_DATA_187 | - |
| 188 | DC1_DATA_188 | - |
| 189 | DC1_DATA_189 | - |
| 190 | DC1_DATA_190 | - |
| 191 | DC1_DATA_191 | - |
| 192 | DC1_DATA_192 | - |
| 193 | DC1_DATA_193 | - |
| 194 | DC1_DATA_194 | - |
| 195 | DC1_DATA_195 | - |
| 196 | DC1_DATA_196 | - |
| 197 | DC1_DATA_197 | - |
| 198 | DC1_DATA_198 | - |
| 199 | DC1_DATA_199 | - |
| 200 | DC1_DATA_200 | - |
| 4094 | MLAG | MLAG |

### VLANs Device Configuration

```eos
!
vlan 110
   name DC1_DATA_110
!
vlan 120
   name DC1_DATA_120
!
vlan 130
   name DC1_DATA_130
!
vlan 131
   name DC1_DATA_131
!
vlan 132
   name DC1_DATA_132
!
vlan 133
   name DC1_DATA_133
!
vlan 134
   name DC1_DATA_134
!
vlan 135
   name DC1_DATA_135
!
vlan 136
   name DC1_DATA_136
!
vlan 137
   name DC1_DATA_137
!
vlan 138
   name DC1_DATA_138
!
vlan 139
   name DC1_DATA_139
!
vlan 140
   name DC1_DATA_140
!
vlan 141
   name DC1_DATA_141
!
vlan 142
   name DC1_DATA_142
!
vlan 143
   name DC1_DATA_143
!
vlan 144
   name DC1_DATA_144
!
vlan 145
   name DC1_DATA_145
!
vlan 146
   name DC1_DATA_146
!
vlan 147
   name DC1_DATA_147
!
vlan 148
   name DC1_DATA_148
!
vlan 149
   name DC1_DATA_149
!
vlan 150
   name DC1_DATA_150
!
vlan 151
   name DC1_DATA_151
!
vlan 152
   name DC1_DATA_152
!
vlan 153
   name DC1_DATA_153
!
vlan 154
   name DC1_DATA_154
!
vlan 155
   name DC1_DATA_155
!
vlan 156
   name DC1_DATA_156
!
vlan 157
   name DC1_DATA_157
!
vlan 158
   name DC1_DATA_158
!
vlan 159
   name DC1_DATA_159
!
vlan 160
   name DC1_DATA_160
!
vlan 161
   name DC1_DATA_161
!
vlan 162
   name DC1_DATA_162
!
vlan 163
   name DC1_DATA_163
!
vlan 164
   name DC1_DATA_164
!
vlan 165
   name DC1_DATA_165
!
vlan 166
   name DC1_DATA_166
!
vlan 167
   name DC1_DATA_167
!
vlan 168
   name DC1_DATA_168
!
vlan 169
   name DC1_DATA_169
!
vlan 170
   name DC1_DATA_170
!
vlan 171
   name DC1_DATA_171
!
vlan 172
   name DC1_DATA_172
!
vlan 173
   name DC1_DATA_173
!
vlan 174
   name DC1_DATA_174
!
vlan 175
   name DC1_DATA_175
!
vlan 176
   name DC1_DATA_176
!
vlan 177
   name DC1_DATA_177
!
vlan 178
   name DC1_DATA_178
!
vlan 179
   name DC1_DATA_179
!
vlan 180
   name DC1_DATA_180
!
vlan 181
   name DC1_DATA_181
!
vlan 182
   name DC1_DATA_182
!
vlan 183
   name DC1_DATA_183
!
vlan 184
   name DC1_DATA_184
!
vlan 185
   name DC1_DATA_185
!
vlan 186
   name DC1_DATA_186
!
vlan 187
   name DC1_DATA_187
!
vlan 188
   name DC1_DATA_188
!
vlan 189
   name DC1_DATA_189
!
vlan 190
   name DC1_DATA_190
!
vlan 191
   name DC1_DATA_191
!
vlan 192
   name DC1_DATA_192
!
vlan 193
   name DC1_DATA_193
!
vlan 194
   name DC1_DATA_194
!
vlan 195
   name DC1_DATA_195
!
vlan 196
   name DC1_DATA_196
!
vlan 197
   name DC1_DATA_197
!
vlan 198
   name DC1_DATA_198
!
vlan 199
   name DC1_DATA_199
!
vlan 200
   name DC1_DATA_200
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
| Ethernet1 | L2_spine-1_Ethernet2 | *trunk | *110,120,130-200 | *- | *- | 1 |
| Ethernet2 | L2_spine-2_Ethernet2 | *trunk | *110,120,130-200 | *- | *- | 1 |
| Ethernet47 | MLAG_leaf-1a_Ethernet47 | *trunk | *- | *- | *MLAG | 47 |
| Ethernet48 | MLAG_leaf-1a_Ethernet48 | *trunk | *- | *- | *MLAG | 47 |

*Inherited from Port-Channel Interface

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description L2_spine-1_Ethernet2
   no shutdown
   channel-group 1 mode active
!
interface Ethernet2
   description L2_spine-2_Ethernet2
   no shutdown
   channel-group 1 mode active
!
interface Ethernet47
   description MLAG_leaf-1a_Ethernet47
   no shutdown
   channel-group 47 mode active
!
interface Ethernet48
   description MLAG_leaf-1a_Ethernet48
   no shutdown
   channel-group 47 mode active
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | --------------------- | ------------------ | ------- | -------- |
| Port-Channel1 | L2_DC1-SPINES_Port-Channel1 | trunk | 110,120,130-200 | - | - | - | - | 1 | - |
| Port-Channel47 | MLAG_leaf-1a_Port-Channel47 | trunk | - | - | MLAG | - | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel1
   description L2_DC1-SPINES_Port-Channel1
   no shutdown
   switchport trunk allowed vlan 110,120,130-200
   switchport mode trunk
   switchport
   mlag 1
!
interface Port-Channel47
   description MLAG_leaf-1a_Port-Channel47
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
| Vlan4094 | default | 10.253.1.1/31 | - | - | - | - |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan4094
   description MLAG
   no shutdown
   mtu 1500
   no autostate
   ip address 10.253.1.1/31
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
