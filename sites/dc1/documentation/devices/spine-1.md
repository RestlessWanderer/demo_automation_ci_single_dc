# spine-1

Serial Number: JPN2429P0ZZ

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
  - [Local Users](#local-users)
  - [Enable Password](#enable-password)
  - [AAA Authorization](#aaa-authorization)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
- [Hardware TCAM Profile](#hardware-tcam-profile)
  - [Hardware TCAM Device Configuration](#hardware-tcam-device-configuration)
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
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Router OSPF](#router-ospf)
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
| Management1 | OOB_MANAGEMENT | oob | MGMT | 172.31.0.27/23 | - |

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

### Local Users

#### Local Users Summary

| User | Privilege | Role | Disabled | Shell |
| ---- | --------- | ---- | -------- | ----- |
| admin | 15 | network-admin | False | - |
| service | 15 | network-admin | False | /bin/bash |

#### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin secret sha512 <removed>
username service privilege 15 role network-admin shell /bin/bash secret sha512 <removed>
```

### Enable Password

Enable password has been disabled

### AAA Authorization

#### AAA Authorization Summary

| Type | User Stores |
| ---- | ----------- |
| Exec | local |

Authorization for configuration commands is disabled.

#### AAA Authorization Device Configuration

```eos
aaa authorization exec default local
!
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

## Hardware TCAM Profile

TCAM profile **`vxlan-routing`** is active

### Hardware TCAM Device Configuration

```eos
!
hardware tcam
   system profile vxlan-routing
```

## MLAG

### MLAG Summary

| Domain-id | Local-interface | Peer-address | Peer-link |
| --------- | --------------- | ------------ | --------- |
| DC1-SPINES | Vlan4094 | 10.253.1.1 | Port-Channel47 |

Dual primary detection is disabled.

### MLAG Device Configuration

```eos
!
mlag configuration
   domain-id DC1-SPINES
   local-interface Vlan4094
   peer-address 10.253.1.1
   peer-link Port-Channel47
   reload-delay mlag 900
   reload-delay non-mlag 1020
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **mstp**

#### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 4096 |

#### Global Spanning-Tree Settings

- Spanning Tree disabled for VLANs: **4093-4094**

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
no spanning-tree vlan-id 4093-4094
spanning-tree mst 0 priority 4096
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
| 201 | DC1_DATA_201 | - |
| 202 | DC1_DATA_202 | - |
| 203 | DC1_DATA_203 | - |
| 204 | DC1_DATA_204 | - |
| 205 | DC1_DATA_205 | - |
| 206 | DC1_DATA_206 | - |
| 207 | DC1_DATA_207 | - |
| 208 | DC1_DATA_208 | - |
| 209 | DC1_DATA_209 | - |
| 210 | DC1_DATA_210 | - |
| 211 | DC1_DATA_211 | - |
| 212 | DC1_DATA_212 | - |
| 213 | DC1_DATA_213 | - |
| 214 | DC1_DATA_214 | - |
| 215 | DC1_DATA_215 | - |
| 216 | DC1_DATA_216 | - |
| 217 | DC1_DATA_217 | - |
| 218 | DC1_DATA_218 | - |
| 219 | DC1_DATA_219 | - |
| 220 | DC1_DATA_220 | - |
| 221 | DC1_DATA_221 | - |
| 222 | DC1_DATA_222 | - |
| 223 | DC1_DATA_223 | - |
| 224 | DC1_DATA_224 | - |
| 225 | DC1_DATA_225 | - |
| 226 | DC1_DATA_226 | - |
| 227 | DC1_DATA_227 | - |
| 228 | DC1_DATA_228 | - |
| 229 | DC1_DATA_229 | - |
| 230 | DC1_DATA_230 | - |
| 231 | DC1_DATA_231 | - |
| 232 | DC1_DATA_232 | - |
| 233 | DC1_DATA_233 | - |
| 234 | DC1_DATA_234 | - |
| 235 | DC1_DATA_235 | - |
| 236 | DC1_DATA_236 | - |
| 237 | DC1_DATA_237 | - |
| 238 | DC1_DATA_238 | - |
| 239 | DC1_DATA_239 | - |
| 240 | DC1_DATA_240 | - |
| 241 | DC1_DATA_241 | - |
| 242 | DC1_DATA_242 | - |
| 243 | DC1_DATA_243 | - |
| 244 | DC1_DATA_244 | - |
| 245 | DC1_DATA_245 | - |
| 246 | DC1_DATA_246 | - |
| 247 | DC1_DATA_247 | - |
| 248 | DC1_DATA_248 | - |
| 249 | DC1_DATA_249 | - |
| 250 | DC1_DATA_250 | - |
| 251 | DC1_DATA_251 | - |
| 252 | DC1_DATA_252 | - |
| 253 | DC1_DATA_253 | - |
| 254 | DC1_DATA_254 | - |
| 255 | DC1_DATA_255 | - |
| 256 | DC1_DATA_256 | - |
| 257 | DC1_DATA_257 | - |
| 258 | DC1_DATA_258 | - |
| 259 | DC1_DATA_259 | - |
| 260 | DC1_DATA_260 | - |
| 261 | DC1_DATA_261 | - |
| 262 | DC1_DATA_262 | - |
| 263 | DC1_DATA_263 | - |
| 264 | DC1_DATA_264 | - |
| 265 | DC1_DATA_265 | - |
| 266 | DC1_DATA_266 | - |
| 267 | DC1_DATA_267 | - |
| 268 | DC1_DATA_268 | - |
| 269 | DC1_DATA_269 | - |
| 270 | DC1_DATA_270 | - |
| 271 | DC1_DATA_271 | - |
| 272 | DC1_DATA_272 | - |
| 273 | DC1_DATA_273 | - |
| 274 | DC1_DATA_274 | - |
| 275 | DC1_DATA_275 | - |
| 276 | DC1_DATA_276 | - |
| 277 | DC1_DATA_277 | - |
| 278 | DC1_DATA_278 | - |
| 279 | DC1_DATA_279 | - |
| 280 | DC1_DATA_280 | - |
| 281 | DC1_DATA_281 | - |
| 282 | DC1_DATA_282 | - |
| 283 | DC1_DATA_283 | - |
| 284 | DC1_DATA_284 | - |
| 285 | DC1_DATA_285 | - |
| 286 | DC1_DATA_286 | - |
| 287 | DC1_DATA_287 | - |
| 288 | DC1_DATA_288 | - |
| 289 | DC1_DATA_289 | - |
| 290 | DC1_DATA_290 | - |
| 291 | DC1_DATA_291 | - |
| 292 | DC1_DATA_292 | - |
| 293 | DC1_DATA_293 | - |
| 294 | DC1_DATA_294 | - |
| 295 | DC1_DATA_295 | - |
| 296 | DC1_DATA_296 | - |
| 297 | DC1_DATA_297 | - |
| 298 | DC1_DATA_298 | - |
| 299 | DC1_DATA_299 | - |
| 4093 | MLAG_L3 | MLAG |
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
vlan 201
   name DC1_DATA_201
!
vlan 202
   name DC1_DATA_202
!
vlan 203
   name DC1_DATA_203
!
vlan 204
   name DC1_DATA_204
!
vlan 205
   name DC1_DATA_205
!
vlan 206
   name DC1_DATA_206
!
vlan 207
   name DC1_DATA_207
!
vlan 208
   name DC1_DATA_208
!
vlan 209
   name DC1_DATA_209
!
vlan 210
   name DC1_DATA_210
!
vlan 211
   name DC1_DATA_211
!
vlan 212
   name DC1_DATA_212
!
vlan 213
   name DC1_DATA_213
!
vlan 214
   name DC1_DATA_214
!
vlan 215
   name DC1_DATA_215
!
vlan 216
   name DC1_DATA_216
!
vlan 217
   name DC1_DATA_217
!
vlan 218
   name DC1_DATA_218
!
vlan 219
   name DC1_DATA_219
!
vlan 220
   name DC1_DATA_220
!
vlan 221
   name DC1_DATA_221
!
vlan 222
   name DC1_DATA_222
!
vlan 223
   name DC1_DATA_223
!
vlan 224
   name DC1_DATA_224
!
vlan 225
   name DC1_DATA_225
!
vlan 226
   name DC1_DATA_226
!
vlan 227
   name DC1_DATA_227
!
vlan 228
   name DC1_DATA_228
!
vlan 229
   name DC1_DATA_229
!
vlan 230
   name DC1_DATA_230
!
vlan 231
   name DC1_DATA_231
!
vlan 232
   name DC1_DATA_232
!
vlan 233
   name DC1_DATA_233
!
vlan 234
   name DC1_DATA_234
!
vlan 235
   name DC1_DATA_235
!
vlan 236
   name DC1_DATA_236
!
vlan 237
   name DC1_DATA_237
!
vlan 238
   name DC1_DATA_238
!
vlan 239
   name DC1_DATA_239
!
vlan 240
   name DC1_DATA_240
!
vlan 241
   name DC1_DATA_241
!
vlan 242
   name DC1_DATA_242
!
vlan 243
   name DC1_DATA_243
!
vlan 244
   name DC1_DATA_244
!
vlan 245
   name DC1_DATA_245
!
vlan 246
   name DC1_DATA_246
!
vlan 247
   name DC1_DATA_247
!
vlan 248
   name DC1_DATA_248
!
vlan 249
   name DC1_DATA_249
!
vlan 250
   name DC1_DATA_250
!
vlan 251
   name DC1_DATA_251
!
vlan 252
   name DC1_DATA_252
!
vlan 253
   name DC1_DATA_253
!
vlan 254
   name DC1_DATA_254
!
vlan 255
   name DC1_DATA_255
!
vlan 256
   name DC1_DATA_256
!
vlan 257
   name DC1_DATA_257
!
vlan 258
   name DC1_DATA_258
!
vlan 259
   name DC1_DATA_259
!
vlan 260
   name DC1_DATA_260
!
vlan 261
   name DC1_DATA_261
!
vlan 262
   name DC1_DATA_262
!
vlan 263
   name DC1_DATA_263
!
vlan 264
   name DC1_DATA_264
!
vlan 265
   name DC1_DATA_265
!
vlan 266
   name DC1_DATA_266
!
vlan 267
   name DC1_DATA_267
!
vlan 268
   name DC1_DATA_268
!
vlan 269
   name DC1_DATA_269
!
vlan 270
   name DC1_DATA_270
!
vlan 271
   name DC1_DATA_271
!
vlan 272
   name DC1_DATA_272
!
vlan 273
   name DC1_DATA_273
!
vlan 274
   name DC1_DATA_274
!
vlan 275
   name DC1_DATA_275
!
vlan 276
   name DC1_DATA_276
!
vlan 277
   name DC1_DATA_277
!
vlan 278
   name DC1_DATA_278
!
vlan 279
   name DC1_DATA_279
!
vlan 280
   name DC1_DATA_280
!
vlan 281
   name DC1_DATA_281
!
vlan 282
   name DC1_DATA_282
!
vlan 283
   name DC1_DATA_283
!
vlan 284
   name DC1_DATA_284
!
vlan 285
   name DC1_DATA_285
!
vlan 286
   name DC1_DATA_286
!
vlan 287
   name DC1_DATA_287
!
vlan 288
   name DC1_DATA_288
!
vlan 289
   name DC1_DATA_289
!
vlan 290
   name DC1_DATA_290
!
vlan 291
   name DC1_DATA_291
!
vlan 292
   name DC1_DATA_292
!
vlan 293
   name DC1_DATA_293
!
vlan 294
   name DC1_DATA_294
!
vlan 295
   name DC1_DATA_295
!
vlan 296
   name DC1_DATA_296
!
vlan 297
   name DC1_DATA_297
!
vlan 298
   name DC1_DATA_298
!
vlan 299
   name DC1_DATA_299
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
| Ethernet1 | L2_leaf-1a_Ethernet1 | *trunk | *110,120,130-299 | *- | *- | 1 |
| Ethernet2 | L2_leaf-1b_Ethernet1 | *trunk | *110,120,130-299 | *- | *- | 1 |
| Ethernet3 | L2_leaf-2a_Ethernet1 | *trunk | *110,120,130-299 | *- | *- | 3 |
| Ethernet4 | L2_leaf-2b_Ethernet1 | *trunk | *110,120,130-299 | *- | *- | 3 |
| Ethernet47 | MLAG_spine-2_Ethernet47 | *trunk | *- | *- | *MLAG | 47 |
| Ethernet48 | MLAG_spine-2_Ethernet48 | *trunk | *- | *- | *MLAG | 47 |

*Inherited from Port-Channel Interface

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description L2_leaf-1a_Ethernet1
   no shutdown
   channel-group 1 mode active
!
interface Ethernet2
   description L2_leaf-1b_Ethernet1
   no shutdown
   channel-group 1 mode active
!
interface Ethernet3
   description L2_leaf-2a_Ethernet1
   no shutdown
   channel-group 3 mode active
!
interface Ethernet4
   description L2_leaf-2b_Ethernet1
   no shutdown
   channel-group 3 mode active
!
interface Ethernet47
   description MLAG_spine-2_Ethernet47
   no shutdown
   channel-group 47 mode active
!
interface Ethernet48
   description MLAG_spine-2_Ethernet48
   no shutdown
   channel-group 47 mode active
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | --------------------- | ------------------ | ------- | -------- |
| Port-Channel1 | L2_DC1-LEAF1_Port-Channel1 | trunk | 110,120,130-299 | - | - | - | - | 1 | - |
| Port-Channel3 | L2_DC1-LEAF2_Port-Channel1 | trunk | 110,120,130-299 | - | - | - | - | 3 | - |
| Port-Channel47 | MLAG_spine-2_Port-Channel47 | trunk | - | - | MLAG | - | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel1
   description L2_DC1-LEAF1_Port-Channel1
   no shutdown
   switchport trunk allowed vlan 110,120,130-299
   switchport mode trunk
   switchport
   mlag 1
!
interface Port-Channel3
   description L2_DC1-LEAF2_Port-Channel1
   no shutdown
   switchport trunk allowed vlan 110,120,130-299
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
   ip ospf area 0.0.0.0
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF | MTU | Shutdown |
| --------- | ----------- | --- | --- | -------- |
| Vlan110 | DC1_DATA_110 | default | - | False |
| Vlan120 | DC1_DATA_120 | default | - | False |
| Vlan130 | DC1_DATA_130 | default | - | False |
| Vlan131 | DC1_DATA_131 | default | - | False |
| Vlan132 | DC1_DATA_132 | default | - | False |
| Vlan133 | DC1_DATA_133 | default | - | False |
| Vlan134 | DC1_DATA_134 | default | - | False |
| Vlan135 | DC1_DATA_135 | default | - | False |
| Vlan136 | DC1_DATA_136 | default | - | False |
| Vlan137 | DC1_DATA_137 | default | - | False |
| Vlan138 | DC1_DATA_138 | default | - | False |
| Vlan139 | DC1_DATA_139 | default | - | False |
| Vlan140 | DC1_DATA_140 | default | - | False |
| Vlan141 | DC1_DATA_141 | default | - | False |
| Vlan142 | DC1_DATA_142 | default | - | False |
| Vlan143 | DC1_DATA_143 | default | - | False |
| Vlan144 | DC1_DATA_144 | default | - | False |
| Vlan145 | DC1_DATA_145 | default | - | False |
| Vlan146 | DC1_DATA_146 | default | - | False |
| Vlan147 | DC1_DATA_147 | default | - | False |
| Vlan148 | DC1_DATA_148 | default | - | False |
| Vlan149 | DC1_DATA_149 | default | - | False |
| Vlan150 | DC1_DATA_150 | default | - | False |
| Vlan151 | DC1_DATA_151 | default | - | False |
| Vlan152 | DC1_DATA_152 | default | - | False |
| Vlan153 | DC1_DATA_153 | default | - | False |
| Vlan154 | DC1_DATA_154 | default | - | False |
| Vlan155 | DC1_DATA_155 | default | - | False |
| Vlan156 | DC1_DATA_156 | default | - | False |
| Vlan157 | DC1_DATA_157 | default | - | False |
| Vlan158 | DC1_DATA_158 | default | - | False |
| Vlan159 | DC1_DATA_159 | default | - | False |
| Vlan160 | DC1_DATA_160 | default | - | False |
| Vlan161 | DC1_DATA_161 | default | - | False |
| Vlan162 | DC1_DATA_162 | default | - | False |
| Vlan163 | DC1_DATA_163 | default | - | False |
| Vlan164 | DC1_DATA_164 | default | - | False |
| Vlan165 | DC1_DATA_165 | default | - | False |
| Vlan166 | DC1_DATA_166 | default | - | False |
| Vlan167 | DC1_DATA_167 | default | - | False |
| Vlan168 | DC1_DATA_168 | default | - | False |
| Vlan169 | DC1_DATA_169 | default | - | False |
| Vlan170 | DC1_DATA_170 | default | - | False |
| Vlan171 | DC1_DATA_171 | default | - | False |
| Vlan172 | DC1_DATA_172 | default | - | False |
| Vlan173 | DC1_DATA_173 | default | - | False |
| Vlan174 | DC1_DATA_174 | default | - | False |
| Vlan175 | DC1_DATA_175 | default | - | False |
| Vlan176 | DC1_DATA_176 | default | - | False |
| Vlan177 | DC1_DATA_177 | default | - | False |
| Vlan178 | DC1_DATA_178 | default | - | False |
| Vlan179 | DC1_DATA_179 | default | - | False |
| Vlan180 | DC1_DATA_180 | default | - | False |
| Vlan181 | DC1_DATA_181 | default | - | False |
| Vlan182 | DC1_DATA_182 | default | - | False |
| Vlan183 | DC1_DATA_183 | default | - | False |
| Vlan184 | DC1_DATA_184 | default | - | False |
| Vlan185 | DC1_DATA_185 | default | - | False |
| Vlan186 | DC1_DATA_186 | default | - | False |
| Vlan187 | DC1_DATA_187 | default | - | False |
| Vlan188 | DC1_DATA_188 | default | - | False |
| Vlan189 | DC1_DATA_189 | default | - | False |
| Vlan190 | DC1_DATA_190 | default | - | False |
| Vlan191 | DC1_DATA_191 | default | - | False |
| Vlan192 | DC1_DATA_192 | default | - | False |
| Vlan193 | DC1_DATA_193 | default | - | False |
| Vlan194 | DC1_DATA_194 | default | - | False |
| Vlan195 | DC1_DATA_195 | default | - | False |
| Vlan196 | DC1_DATA_196 | default | - | False |
| Vlan197 | DC1_DATA_197 | default | - | False |
| Vlan198 | DC1_DATA_198 | default | - | False |
| Vlan199 | DC1_DATA_199 | default | - | False |
| Vlan200 | DC1_DATA_200 | default | - | False |
| Vlan201 | DC1_DATA_201 | default | - | False |
| Vlan202 | DC1_DATA_202 | default | - | False |
| Vlan203 | DC1_DATA_203 | default | - | False |
| Vlan204 | DC1_DATA_204 | default | - | False |
| Vlan205 | DC1_DATA_205 | default | - | False |
| Vlan206 | DC1_DATA_206 | default | - | False |
| Vlan207 | DC1_DATA_207 | default | - | False |
| Vlan208 | DC1_DATA_208 | default | - | False |
| Vlan209 | DC1_DATA_209 | default | - | False |
| Vlan210 | DC1_DATA_210 | default | - | False |
| Vlan211 | DC1_DATA_211 | default | - | False |
| Vlan212 | DC1_DATA_212 | default | - | False |
| Vlan213 | DC1_DATA_213 | default | - | False |
| Vlan214 | DC1_DATA_214 | default | - | False |
| Vlan215 | DC1_DATA_215 | default | - | False |
| Vlan216 | DC1_DATA_216 | default | - | False |
| Vlan217 | DC1_DATA_217 | default | - | False |
| Vlan218 | DC1_DATA_218 | default | - | False |
| Vlan219 | DC1_DATA_219 | default | - | False |
| Vlan220 | DC1_DATA_220 | default | - | False |
| Vlan221 | DC1_DATA_221 | default | - | False |
| Vlan222 | DC1_DATA_222 | default | - | False |
| Vlan223 | DC1_DATA_223 | default | - | False |
| Vlan224 | DC1_DATA_224 | default | - | False |
| Vlan225 | DC1_DATA_225 | default | - | False |
| Vlan226 | DC1_DATA_226 | default | - | False |
| Vlan227 | DC1_DATA_227 | default | - | False |
| Vlan228 | DC1_DATA_228 | default | - | False |
| Vlan229 | DC1_DATA_229 | default | - | False |
| Vlan230 | DC1_DATA_230 | default | - | False |
| Vlan231 | DC1_DATA_231 | default | - | False |
| Vlan232 | DC1_DATA_232 | default | - | False |
| Vlan233 | DC1_DATA_233 | default | - | False |
| Vlan234 | DC1_DATA_234 | default | - | False |
| Vlan235 | DC1_DATA_235 | default | - | False |
| Vlan236 | DC1_DATA_236 | default | - | False |
| Vlan237 | DC1_DATA_237 | default | - | False |
| Vlan238 | DC1_DATA_238 | default | - | False |
| Vlan239 | DC1_DATA_239 | default | - | False |
| Vlan240 | DC1_DATA_240 | default | - | False |
| Vlan241 | DC1_DATA_241 | default | - | False |
| Vlan242 | DC1_DATA_242 | default | - | False |
| Vlan243 | DC1_DATA_243 | default | - | False |
| Vlan244 | DC1_DATA_244 | default | - | False |
| Vlan245 | DC1_DATA_245 | default | - | False |
| Vlan246 | DC1_DATA_246 | default | - | False |
| Vlan247 | DC1_DATA_247 | default | - | False |
| Vlan248 | DC1_DATA_248 | default | - | False |
| Vlan249 | DC1_DATA_249 | default | - | False |
| Vlan250 | DC1_DATA_250 | default | - | False |
| Vlan251 | DC1_DATA_251 | default | - | False |
| Vlan252 | DC1_DATA_252 | default | - | False |
| Vlan253 | DC1_DATA_253 | default | - | False |
| Vlan254 | DC1_DATA_254 | default | - | False |
| Vlan255 | DC1_DATA_255 | default | - | False |
| Vlan256 | DC1_DATA_256 | default | - | False |
| Vlan257 | DC1_DATA_257 | default | - | False |
| Vlan258 | DC1_DATA_258 | default | - | False |
| Vlan259 | DC1_DATA_259 | default | - | False |
| Vlan260 | DC1_DATA_260 | default | - | False |
| Vlan261 | DC1_DATA_261 | default | - | False |
| Vlan262 | DC1_DATA_262 | default | - | False |
| Vlan263 | DC1_DATA_263 | default | - | False |
| Vlan264 | DC1_DATA_264 | default | - | False |
| Vlan265 | DC1_DATA_265 | default | - | False |
| Vlan266 | DC1_DATA_266 | default | - | False |
| Vlan267 | DC1_DATA_267 | default | - | False |
| Vlan268 | DC1_DATA_268 | default | - | False |
| Vlan269 | DC1_DATA_269 | default | - | False |
| Vlan270 | DC1_DATA_270 | default | - | False |
| Vlan271 | DC1_DATA_271 | default | - | False |
| Vlan272 | DC1_DATA_272 | default | - | False |
| Vlan273 | DC1_DATA_273 | default | - | False |
| Vlan274 | DC1_DATA_274 | default | - | False |
| Vlan275 | DC1_DATA_275 | default | - | False |
| Vlan276 | DC1_DATA_276 | default | - | False |
| Vlan277 | DC1_DATA_277 | default | - | False |
| Vlan278 | DC1_DATA_278 | default | - | False |
| Vlan279 | DC1_DATA_279 | default | - | False |
| Vlan280 | DC1_DATA_280 | default | - | False |
| Vlan281 | DC1_DATA_281 | default | - | False |
| Vlan282 | DC1_DATA_282 | default | - | False |
| Vlan283 | DC1_DATA_283 | default | - | False |
| Vlan284 | DC1_DATA_284 | default | - | False |
| Vlan285 | DC1_DATA_285 | default | - | False |
| Vlan286 | DC1_DATA_286 | default | - | False |
| Vlan287 | DC1_DATA_287 | default | - | False |
| Vlan288 | DC1_DATA_288 | default | - | False |
| Vlan289 | DC1_DATA_289 | default | - | False |
| Vlan290 | DC1_DATA_290 | default | - | False |
| Vlan291 | DC1_DATA_291 | default | - | False |
| Vlan292 | DC1_DATA_292 | default | - | False |
| Vlan293 | DC1_DATA_293 | default | - | False |
| Vlan294 | DC1_DATA_294 | default | - | False |
| Vlan295 | DC1_DATA_295 | default | - | False |
| Vlan296 | DC1_DATA_296 | default | - | False |
| Vlan297 | DC1_DATA_297 | default | - | False |
| Vlan298 | DC1_DATA_298 | default | - | False |
| Vlan299 | DC1_DATA_299 | default | - | False |
| Vlan4093 | MLAG_L3 | default | 1500 | False |
| Vlan4094 | MLAG | default | 1500 | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan110 | default | 10.1.10.2/24 | - | 10.1.10.1 | - | - |
| Vlan120 | default | 10.1.20.2/24 | - | 10.1.20.1 | - | - |
| Vlan130 | default | 10.1.30.2/24 | - | 10.1.30.1 | - | - |
| Vlan131 | default | 10.1.31.2/24 | - | 10.1.31.1 | - | - |
| Vlan132 | default | 10.1.32.2/24 | - | 10.1.32.1 | - | - |
| Vlan133 | default | 10.1.33.2/24 | - | 10.1.33.1 | - | - |
| Vlan134 | default | 10.1.34.2/24 | - | 10.1.34.1 | - | - |
| Vlan135 | default | 10.1.35.2/24 | - | 10.1.35.1 | - | - |
| Vlan136 | default | 10.1.36.2/24 | - | 10.1.36.1 | - | - |
| Vlan137 | default | 10.1.37.2/24 | - | 10.1.37.1 | - | - |
| Vlan138 | default | 10.1.38.2/24 | - | 10.1.38.1 | - | - |
| Vlan139 | default | 10.1.39.2/24 | - | 10.1.39.1 | - | - |
| Vlan140 | default | 10.1.40.2/24 | - | 10.1.40.1 | - | - |
| Vlan141 | default | 10.1.41.2/24 | - | 10.1.41.1 | - | - |
| Vlan142 | default | 10.1.42.2/24 | - | 10.1.42.1 | - | - |
| Vlan143 | default | 10.1.43.2/24 | - | 10.1.43.1 | - | - |
| Vlan144 | default | 10.1.44.2/24 | - | 10.1.44.1 | - | - |
| Vlan145 | default | 10.1.45.2/24 | - | 10.1.45.1 | - | - |
| Vlan146 | default | 10.1.46.2/24 | - | 10.1.46.1 | - | - |
| Vlan147 | default | 10.1.47.2/24 | - | 10.1.47.1 | - | - |
| Vlan148 | default | 10.1.48.2/24 | - | 10.1.48.1 | - | - |
| Vlan149 | default | 10.1.49.2/24 | - | 10.1.49.1 | - | - |
| Vlan150 | default | 10.1.50.2/24 | - | 10.1.50.1 | - | - |
| Vlan151 | default | 10.1.51.2/24 | - | 10.1.51.1 | - | - |
| Vlan152 | default | 10.1.52.2/24 | - | 10.1.52.1 | - | - |
| Vlan153 | default | 10.1.53.2/24 | - | 10.1.53.1 | - | - |
| Vlan154 | default | 10.1.54.2/24 | - | 10.1.54.1 | - | - |
| Vlan155 | default | 10.1.55.2/24 | - | 10.1.55.1 | - | - |
| Vlan156 | default | 10.1.56.2/24 | - | 10.1.56.1 | - | - |
| Vlan157 | default | 10.1.57.2/24 | - | 10.1.57.1 | - | - |
| Vlan158 | default | 10.1.58.2/24 | - | 10.1.58.1 | - | - |
| Vlan159 | default | 10.1.59.2/24 | - | 10.1.59.1 | - | - |
| Vlan160 | default | 10.1.60.2/24 | - | 10.1.60.1 | - | - |
| Vlan161 | default | 10.1.61.2/24 | - | 10.1.61.1 | - | - |
| Vlan162 | default | 10.1.62.2/24 | - | 10.1.62.1 | - | - |
| Vlan163 | default | 10.1.63.2/24 | - | 10.1.63.1 | - | - |
| Vlan164 | default | 10.1.64.2/24 | - | 10.1.64.1 | - | - |
| Vlan165 | default | 10.1.65.2/24 | - | 10.1.65.1 | - | - |
| Vlan166 | default | 10.1.66.2/24 | - | 10.1.66.1 | - | - |
| Vlan167 | default | 10.1.67.2/24 | - | 10.1.67.1 | - | - |
| Vlan168 | default | 10.1.68.2/24 | - | 10.1.68.1 | - | - |
| Vlan169 | default | 10.1.69.2/24 | - | 10.1.69.1 | - | - |
| Vlan170 | default | 10.1.70.2/24 | - | 10.1.70.1 | - | - |
| Vlan171 | default | 10.1.71.2/24 | - | 10.1.71.1 | - | - |
| Vlan172 | default | 10.1.72.2/24 | - | 10.1.72.1 | - | - |
| Vlan173 | default | 10.1.73.2/24 | - | 10.1.73.1 | - | - |
| Vlan174 | default | 10.1.74.2/24 | - | 10.1.74.1 | - | - |
| Vlan175 | default | 10.1.75.2/24 | - | 10.1.75.1 | - | - |
| Vlan176 | default | 10.1.76.2/24 | - | 10.1.76.1 | - | - |
| Vlan177 | default | 10.1.77.2/24 | - | 10.1.77.1 | - | - |
| Vlan178 | default | 10.1.78.2/24 | - | 10.1.78.1 | - | - |
| Vlan179 | default | 10.1.79.2/24 | - | 10.1.79.1 | - | - |
| Vlan180 | default | 10.1.80.2/24 | - | 10.1.80.1 | - | - |
| Vlan181 | default | 10.1.81.2/24 | - | 10.1.81.1 | - | - |
| Vlan182 | default | 10.1.82.2/24 | - | 10.1.82.1 | - | - |
| Vlan183 | default | 10.1.83.2/24 | - | 10.1.83.1 | - | - |
| Vlan184 | default | 10.1.84.2/24 | - | 10.1.84.1 | - | - |
| Vlan185 | default | 10.1.85.2/24 | - | 10.1.85.1 | - | - |
| Vlan186 | default | 10.1.86.2/24 | - | 10.1.86.1 | - | - |
| Vlan187 | default | 10.1.87.2/24 | - | 10.1.87.1 | - | - |
| Vlan188 | default | 10.1.88.2/24 | - | 10.1.88.1 | - | - |
| Vlan189 | default | 10.1.89.2/24 | - | 10.1.89.1 | - | - |
| Vlan190 | default | 10.1.90.2/24 | - | 10.1.90.1 | - | - |
| Vlan191 | default | 10.1.91.2/24 | - | 10.1.91.1 | - | - |
| Vlan192 | default | 10.1.92.2/24 | - | 10.1.92.1 | - | - |
| Vlan193 | default | 10.1.93.2/24 | - | 10.1.93.1 | - | - |
| Vlan194 | default | 10.1.94.2/24 | - | 10.1.94.1 | - | - |
| Vlan195 | default | 10.1.95.2/24 | - | 10.1.95.1 | - | - |
| Vlan196 | default | 10.1.96.2/24 | - | 10.1.96.1 | - | - |
| Vlan197 | default | 10.1.97.2/24 | - | 10.1.97.1 | - | - |
| Vlan198 | default | 10.1.98.2/24 | - | 10.1.98.1 | - | - |
| Vlan199 | default | 10.1.99.2/24 | - | 10.1.99.1 | - | - |
| Vlan200 | default | 10.1.100.2/24 | - | 10.1.100.1 | - | - |
| Vlan201 | default | 10.1.101.2/24 | - | 10.1.101.1 | - | - |
| Vlan202 | default | 10.1.102.2/24 | - | 10.1.102.1 | - | - |
| Vlan203 | default | 10.1.103.2/24 | - | 10.1.103.1 | - | - |
| Vlan204 | default | 10.1.104.2/24 | - | 10.1.104.1 | - | - |
| Vlan205 | default | 10.1.105.2/24 | - | 10.1.105.1 | - | - |
| Vlan206 | default | 10.1.106.2/24 | - | 10.1.106.1 | - | - |
| Vlan207 | default | 10.1.107.2/24 | - | 10.1.107.1 | - | - |
| Vlan208 | default | 10.1.108.2/24 | - | 10.1.108.1 | - | - |
| Vlan209 | default | 10.1.109.2/24 | - | 10.1.109.1 | - | - |
| Vlan210 | default | 10.1.110.2/24 | - | 10.1.110.1 | - | - |
| Vlan211 | default | 10.1.111.2/24 | - | 10.1.111.1 | - | - |
| Vlan212 | default | 10.1.112.2/24 | - | 10.1.112.1 | - | - |
| Vlan213 | default | 10.1.113.2/24 | - | 10.1.113.1 | - | - |
| Vlan214 | default | 10.1.114.2/24 | - | 10.1.114.1 | - | - |
| Vlan215 | default | 10.1.115.2/24 | - | 10.1.115.1 | - | - |
| Vlan216 | default | 10.1.116.2/24 | - | 10.1.116.1 | - | - |
| Vlan217 | default | 10.1.117.2/24 | - | 10.1.117.1 | - | - |
| Vlan218 | default | 10.1.118.2/24 | - | 10.1.118.1 | - | - |
| Vlan219 | default | 10.1.119.2/24 | - | 10.1.119.1 | - | - |
| Vlan220 | default | 10.1.120.2/24 | - | 10.1.120.1 | - | - |
| Vlan221 | default | 10.1.121.2/24 | - | 10.1.121.1 | - | - |
| Vlan222 | default | 10.1.122.2/24 | - | 10.1.122.1 | - | - |
| Vlan223 | default | 10.1.123.2/24 | - | 10.1.123.1 | - | - |
| Vlan224 | default | 10.1.124.2/24 | - | 10.1.124.1 | - | - |
| Vlan225 | default | 10.1.125.2/24 | - | 10.1.125.1 | - | - |
| Vlan226 | default | 10.1.126.2/24 | - | 10.1.126.1 | - | - |
| Vlan227 | default | 10.1.127.2/24 | - | 10.1.127.1 | - | - |
| Vlan228 | default | 10.1.128.2/24 | - | 10.1.128.1 | - | - |
| Vlan229 | default | 10.1.129.2/24 | - | 10.1.129.1 | - | - |
| Vlan230 | default | 10.1.130.2/24 | - | 10.1.130.1 | - | - |
| Vlan231 | default | 10.1.131.2/24 | - | 10.1.131.1 | - | - |
| Vlan232 | default | 10.1.132.2/24 | - | 10.1.132.1 | - | - |
| Vlan233 | default | 10.1.133.2/24 | - | 10.1.133.1 | - | - |
| Vlan234 | default | 10.1.134.2/24 | - | 10.1.134.1 | - | - |
| Vlan235 | default | 10.1.135.2/24 | - | 10.1.135.1 | - | - |
| Vlan236 | default | 10.1.136.2/24 | - | 10.1.136.1 | - | - |
| Vlan237 | default | 10.1.137.2/24 | - | 10.1.137.1 | - | - |
| Vlan238 | default | 10.1.138.2/24 | - | 10.1.138.1 | - | - |
| Vlan239 | default | 10.1.139.2/24 | - | 10.1.139.1 | - | - |
| Vlan240 | default | 10.1.140.2/24 | - | 10.1.140.1 | - | - |
| Vlan241 | default | 10.1.141.2/24 | - | 10.1.141.1 | - | - |
| Vlan242 | default | 10.1.142.2/24 | - | 10.1.142.1 | - | - |
| Vlan243 | default | 10.1.143.2/24 | - | 10.1.143.1 | - | - |
| Vlan244 | default | 10.1.144.2/24 | - | 10.1.144.1 | - | - |
| Vlan245 | default | 10.1.145.2/24 | - | 10.1.145.1 | - | - |
| Vlan246 | default | 10.1.146.2/24 | - | 10.1.146.1 | - | - |
| Vlan247 | default | 10.1.147.2/24 | - | 10.1.147.1 | - | - |
| Vlan248 | default | 10.1.148.2/24 | - | 10.1.148.1 | - | - |
| Vlan249 | default | 10.1.149.2/24 | - | 10.1.149.1 | - | - |
| Vlan250 | default | 10.1.150.2/24 | - | 10.1.150.1 | - | - |
| Vlan251 | default | 10.1.151.2/24 | - | 10.1.151.1 | - | - |
| Vlan252 | default | 10.1.152.2/24 | - | 10.1.152.1 | - | - |
| Vlan253 | default | 10.1.153.2/24 | - | 10.1.153.1 | - | - |
| Vlan254 | default | 10.1.154.2/24 | - | 10.1.154.1 | - | - |
| Vlan255 | default | 10.1.155.2/24 | - | 10.1.155.1 | - | - |
| Vlan256 | default | 10.1.156.2/24 | - | 10.1.156.1 | - | - |
| Vlan257 | default | 10.1.157.2/24 | - | 10.1.157.1 | - | - |
| Vlan258 | default | 10.1.158.2/24 | - | 10.1.158.1 | - | - |
| Vlan259 | default | 10.1.159.2/24 | - | 10.1.159.1 | - | - |
| Vlan260 | default | 10.1.160.2/24 | - | 10.1.160.1 | - | - |
| Vlan261 | default | 10.1.161.2/24 | - | 10.1.161.1 | - | - |
| Vlan262 | default | 10.1.162.2/24 | - | 10.1.162.1 | - | - |
| Vlan263 | default | 10.1.163.2/24 | - | 10.1.163.1 | - | - |
| Vlan264 | default | 10.1.164.2/24 | - | 10.1.164.1 | - | - |
| Vlan265 | default | 10.1.165.2/24 | - | 10.1.165.1 | - | - |
| Vlan266 | default | 10.1.166.2/24 | - | 10.1.166.1 | - | - |
| Vlan267 | default | 10.1.167.2/24 | - | 10.1.167.1 | - | - |
| Vlan268 | default | 10.1.168.2/24 | - | 10.1.168.1 | - | - |
| Vlan269 | default | 10.1.169.2/24 | - | 10.1.169.1 | - | - |
| Vlan270 | default | 10.1.170.2/24 | - | 10.1.170.1 | - | - |
| Vlan271 | default | 10.1.171.2/24 | - | 10.1.171.1 | - | - |
| Vlan272 | default | 10.1.172.2/24 | - | 10.1.172.1 | - | - |
| Vlan273 | default | 10.1.173.2/24 | - | 10.1.173.1 | - | - |
| Vlan274 | default | 10.1.174.2/24 | - | 10.1.174.1 | - | - |
| Vlan275 | default | 10.1.175.2/24 | - | 10.1.175.1 | - | - |
| Vlan276 | default | 10.1.176.2/24 | - | 10.1.176.1 | - | - |
| Vlan277 | default | 10.1.177.2/24 | - | 10.1.177.1 | - | - |
| Vlan278 | default | 10.1.178.2/24 | - | 10.1.178.1 | - | - |
| Vlan279 | default | 10.1.179.2/24 | - | 10.1.179.1 | - | - |
| Vlan280 | default | 10.1.180.2/24 | - | 10.1.180.1 | - | - |
| Vlan281 | default | 10.1.181.2/24 | - | 10.1.181.1 | - | - |
| Vlan282 | default | 10.1.182.2/24 | - | 10.1.182.1 | - | - |
| Vlan283 | default | 10.1.183.2/24 | - | 10.1.183.1 | - | - |
| Vlan284 | default | 10.1.184.2/24 | - | 10.1.184.1 | - | - |
| Vlan285 | default | 10.1.185.2/24 | - | 10.1.185.1 | - | - |
| Vlan286 | default | 10.1.186.2/24 | - | 10.1.186.1 | - | - |
| Vlan287 | default | 10.1.187.2/24 | - | 10.1.187.1 | - | - |
| Vlan288 | default | 10.1.188.2/24 | - | 10.1.188.1 | - | - |
| Vlan289 | default | 10.1.189.2/24 | - | 10.1.189.1 | - | - |
| Vlan290 | default | 10.1.190.2/24 | - | 10.1.190.1 | - | - |
| Vlan291 | default | 10.1.191.2/24 | - | 10.1.191.1 | - | - |
| Vlan292 | default | 10.1.192.2/24 | - | 10.1.192.1 | - | - |
| Vlan293 | default | 10.1.193.2/24 | - | 10.1.193.1 | - | - |
| Vlan294 | default | 10.1.194.2/24 | - | 10.1.194.1 | - | - |
| Vlan295 | default | 10.1.195.2/24 | - | 10.1.195.1 | - | - |
| Vlan296 | default | 10.1.196.2/24 | - | 10.1.196.1 | - | - |
| Vlan297 | default | 10.1.197.2/24 | - | 10.1.197.1 | - | - |
| Vlan298 | default | 10.1.198.2/24 | - | 10.1.198.1 | - | - |
| Vlan299 | default | 10.1.199.2/24 | - | 10.1.199.1 | - | - |
| Vlan4093 | default | 10.253.1.2/31 | - | - | - | - |
| Vlan4094 | default | 10.253.1.0/31 | - | - | - | - |

##### OSPF

| Interface | OSPF Network Point to Point | OSPF Area | OSPF Cost | OSPF Authentication | IPv6 OSPF Process ID | IPv6 OSPF Area | IPv6 OSPF Network Point to Point |
| --------- | --------------------------- | --------- | --------- | ------------------- | -------------------- | -------------- | -------------------------------- |
| Vlan4093 | True | 0.0.0.0 | - | - | - | - | - |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan110
   description DC1_DATA_110
   no shutdown
   ip address 10.1.10.2/24
   ip virtual-router address 10.1.10.1
!
interface Vlan120
   description DC1_DATA_120
   no shutdown
   ip address 10.1.20.2/24
   ip virtual-router address 10.1.20.1
!
interface Vlan130
   description DC1_DATA_130
   no shutdown
   ip address 10.1.30.2/24
   ip virtual-router address 10.1.30.1
!
interface Vlan131
   description DC1_DATA_131
   no shutdown
   ip address 10.1.31.2/24
   ip virtual-router address 10.1.31.1
!
interface Vlan132
   description DC1_DATA_132
   no shutdown
   ip address 10.1.32.2/24
   ip virtual-router address 10.1.32.1
!
interface Vlan133
   description DC1_DATA_133
   no shutdown
   ip address 10.1.33.2/24
   ip virtual-router address 10.1.33.1
!
interface Vlan134
   description DC1_DATA_134
   no shutdown
   ip address 10.1.34.2/24
   ip virtual-router address 10.1.34.1
!
interface Vlan135
   description DC1_DATA_135
   no shutdown
   ip address 10.1.35.2/24
   ip virtual-router address 10.1.35.1
!
interface Vlan136
   description DC1_DATA_136
   no shutdown
   ip address 10.1.36.2/24
   ip virtual-router address 10.1.36.1
!
interface Vlan137
   description DC1_DATA_137
   no shutdown
   ip address 10.1.37.2/24
   ip virtual-router address 10.1.37.1
!
interface Vlan138
   description DC1_DATA_138
   no shutdown
   ip address 10.1.38.2/24
   ip virtual-router address 10.1.38.1
!
interface Vlan139
   description DC1_DATA_139
   no shutdown
   ip address 10.1.39.2/24
   ip virtual-router address 10.1.39.1
!
interface Vlan140
   description DC1_DATA_140
   no shutdown
   ip address 10.1.40.2/24
   ip virtual-router address 10.1.40.1
!
interface Vlan141
   description DC1_DATA_141
   no shutdown
   ip address 10.1.41.2/24
   ip virtual-router address 10.1.41.1
!
interface Vlan142
   description DC1_DATA_142
   no shutdown
   ip address 10.1.42.2/24
   ip virtual-router address 10.1.42.1
!
interface Vlan143
   description DC1_DATA_143
   no shutdown
   ip address 10.1.43.2/24
   ip virtual-router address 10.1.43.1
!
interface Vlan144
   description DC1_DATA_144
   no shutdown
   ip address 10.1.44.2/24
   ip virtual-router address 10.1.44.1
!
interface Vlan145
   description DC1_DATA_145
   no shutdown
   ip address 10.1.45.2/24
   ip virtual-router address 10.1.45.1
!
interface Vlan146
   description DC1_DATA_146
   no shutdown
   ip address 10.1.46.2/24
   ip virtual-router address 10.1.46.1
!
interface Vlan147
   description DC1_DATA_147
   no shutdown
   ip address 10.1.47.2/24
   ip virtual-router address 10.1.47.1
!
interface Vlan148
   description DC1_DATA_148
   no shutdown
   ip address 10.1.48.2/24
   ip virtual-router address 10.1.48.1
!
interface Vlan149
   description DC1_DATA_149
   no shutdown
   ip address 10.1.49.2/24
   ip virtual-router address 10.1.49.1
!
interface Vlan150
   description DC1_DATA_150
   no shutdown
   ip address 10.1.50.2/24
   ip virtual-router address 10.1.50.1
!
interface Vlan151
   description DC1_DATA_151
   no shutdown
   ip address 10.1.51.2/24
   ip virtual-router address 10.1.51.1
!
interface Vlan152
   description DC1_DATA_152
   no shutdown
   ip address 10.1.52.2/24
   ip virtual-router address 10.1.52.1
!
interface Vlan153
   description DC1_DATA_153
   no shutdown
   ip address 10.1.53.2/24
   ip virtual-router address 10.1.53.1
!
interface Vlan154
   description DC1_DATA_154
   no shutdown
   ip address 10.1.54.2/24
   ip virtual-router address 10.1.54.1
!
interface Vlan155
   description DC1_DATA_155
   no shutdown
   ip address 10.1.55.2/24
   ip virtual-router address 10.1.55.1
!
interface Vlan156
   description DC1_DATA_156
   no shutdown
   ip address 10.1.56.2/24
   ip virtual-router address 10.1.56.1
!
interface Vlan157
   description DC1_DATA_157
   no shutdown
   ip address 10.1.57.2/24
   ip virtual-router address 10.1.57.1
!
interface Vlan158
   description DC1_DATA_158
   no shutdown
   ip address 10.1.58.2/24
   ip virtual-router address 10.1.58.1
!
interface Vlan159
   description DC1_DATA_159
   no shutdown
   ip address 10.1.59.2/24
   ip virtual-router address 10.1.59.1
!
interface Vlan160
   description DC1_DATA_160
   no shutdown
   ip address 10.1.60.2/24
   ip virtual-router address 10.1.60.1
!
interface Vlan161
   description DC1_DATA_161
   no shutdown
   ip address 10.1.61.2/24
   ip virtual-router address 10.1.61.1
!
interface Vlan162
   description DC1_DATA_162
   no shutdown
   ip address 10.1.62.2/24
   ip virtual-router address 10.1.62.1
!
interface Vlan163
   description DC1_DATA_163
   no shutdown
   ip address 10.1.63.2/24
   ip virtual-router address 10.1.63.1
!
interface Vlan164
   description DC1_DATA_164
   no shutdown
   ip address 10.1.64.2/24
   ip virtual-router address 10.1.64.1
!
interface Vlan165
   description DC1_DATA_165
   no shutdown
   ip address 10.1.65.2/24
   ip virtual-router address 10.1.65.1
!
interface Vlan166
   description DC1_DATA_166
   no shutdown
   ip address 10.1.66.2/24
   ip virtual-router address 10.1.66.1
!
interface Vlan167
   description DC1_DATA_167
   no shutdown
   ip address 10.1.67.2/24
   ip virtual-router address 10.1.67.1
!
interface Vlan168
   description DC1_DATA_168
   no shutdown
   ip address 10.1.68.2/24
   ip virtual-router address 10.1.68.1
!
interface Vlan169
   description DC1_DATA_169
   no shutdown
   ip address 10.1.69.2/24
   ip virtual-router address 10.1.69.1
!
interface Vlan170
   description DC1_DATA_170
   no shutdown
   ip address 10.1.70.2/24
   ip virtual-router address 10.1.70.1
!
interface Vlan171
   description DC1_DATA_171
   no shutdown
   ip address 10.1.71.2/24
   ip virtual-router address 10.1.71.1
!
interface Vlan172
   description DC1_DATA_172
   no shutdown
   ip address 10.1.72.2/24
   ip virtual-router address 10.1.72.1
!
interface Vlan173
   description DC1_DATA_173
   no shutdown
   ip address 10.1.73.2/24
   ip virtual-router address 10.1.73.1
!
interface Vlan174
   description DC1_DATA_174
   no shutdown
   ip address 10.1.74.2/24
   ip virtual-router address 10.1.74.1
!
interface Vlan175
   description DC1_DATA_175
   no shutdown
   ip address 10.1.75.2/24
   ip virtual-router address 10.1.75.1
!
interface Vlan176
   description DC1_DATA_176
   no shutdown
   ip address 10.1.76.2/24
   ip virtual-router address 10.1.76.1
!
interface Vlan177
   description DC1_DATA_177
   no shutdown
   ip address 10.1.77.2/24
   ip virtual-router address 10.1.77.1
!
interface Vlan178
   description DC1_DATA_178
   no shutdown
   ip address 10.1.78.2/24
   ip virtual-router address 10.1.78.1
!
interface Vlan179
   description DC1_DATA_179
   no shutdown
   ip address 10.1.79.2/24
   ip virtual-router address 10.1.79.1
!
interface Vlan180
   description DC1_DATA_180
   no shutdown
   ip address 10.1.80.2/24
   ip virtual-router address 10.1.80.1
!
interface Vlan181
   description DC1_DATA_181
   no shutdown
   ip address 10.1.81.2/24
   ip virtual-router address 10.1.81.1
!
interface Vlan182
   description DC1_DATA_182
   no shutdown
   ip address 10.1.82.2/24
   ip virtual-router address 10.1.82.1
!
interface Vlan183
   description DC1_DATA_183
   no shutdown
   ip address 10.1.83.2/24
   ip virtual-router address 10.1.83.1
!
interface Vlan184
   description DC1_DATA_184
   no shutdown
   ip address 10.1.84.2/24
   ip virtual-router address 10.1.84.1
!
interface Vlan185
   description DC1_DATA_185
   no shutdown
   ip address 10.1.85.2/24
   ip virtual-router address 10.1.85.1
!
interface Vlan186
   description DC1_DATA_186
   no shutdown
   ip address 10.1.86.2/24
   ip virtual-router address 10.1.86.1
!
interface Vlan187
   description DC1_DATA_187
   no shutdown
   ip address 10.1.87.2/24
   ip virtual-router address 10.1.87.1
!
interface Vlan188
   description DC1_DATA_188
   no shutdown
   ip address 10.1.88.2/24
   ip virtual-router address 10.1.88.1
!
interface Vlan189
   description DC1_DATA_189
   no shutdown
   ip address 10.1.89.2/24
   ip virtual-router address 10.1.89.1
!
interface Vlan190
   description DC1_DATA_190
   no shutdown
   ip address 10.1.90.2/24
   ip virtual-router address 10.1.90.1
!
interface Vlan191
   description DC1_DATA_191
   no shutdown
   ip address 10.1.91.2/24
   ip virtual-router address 10.1.91.1
!
interface Vlan192
   description DC1_DATA_192
   no shutdown
   ip address 10.1.92.2/24
   ip virtual-router address 10.1.92.1
!
interface Vlan193
   description DC1_DATA_193
   no shutdown
   ip address 10.1.93.2/24
   ip virtual-router address 10.1.93.1
!
interface Vlan194
   description DC1_DATA_194
   no shutdown
   ip address 10.1.94.2/24
   ip virtual-router address 10.1.94.1
!
interface Vlan195
   description DC1_DATA_195
   no shutdown
   ip address 10.1.95.2/24
   ip virtual-router address 10.1.95.1
!
interface Vlan196
   description DC1_DATA_196
   no shutdown
   ip address 10.1.96.2/24
   ip virtual-router address 10.1.96.1
!
interface Vlan197
   description DC1_DATA_197
   no shutdown
   ip address 10.1.97.2/24
   ip virtual-router address 10.1.97.1
!
interface Vlan198
   description DC1_DATA_198
   no shutdown
   ip address 10.1.98.2/24
   ip virtual-router address 10.1.98.1
!
interface Vlan199
   description DC1_DATA_199
   no shutdown
   ip address 10.1.99.2/24
   ip virtual-router address 10.1.99.1
!
interface Vlan200
   description DC1_DATA_200
   no shutdown
   ip address 10.1.100.2/24
   ip virtual-router address 10.1.100.1
!
interface Vlan201
   description DC1_DATA_201
   no shutdown
   ip address 10.1.101.2/24
   ip virtual-router address 10.1.101.1
!
interface Vlan202
   description DC1_DATA_202
   no shutdown
   ip address 10.1.102.2/24
   ip virtual-router address 10.1.102.1
!
interface Vlan203
   description DC1_DATA_203
   no shutdown
   ip address 10.1.103.2/24
   ip virtual-router address 10.1.103.1
!
interface Vlan204
   description DC1_DATA_204
   no shutdown
   ip address 10.1.104.2/24
   ip virtual-router address 10.1.104.1
!
interface Vlan205
   description DC1_DATA_205
   no shutdown
   ip address 10.1.105.2/24
   ip virtual-router address 10.1.105.1
!
interface Vlan206
   description DC1_DATA_206
   no shutdown
   ip address 10.1.106.2/24
   ip virtual-router address 10.1.106.1
!
interface Vlan207
   description DC1_DATA_207
   no shutdown
   ip address 10.1.107.2/24
   ip virtual-router address 10.1.107.1
!
interface Vlan208
   description DC1_DATA_208
   no shutdown
   ip address 10.1.108.2/24
   ip virtual-router address 10.1.108.1
!
interface Vlan209
   description DC1_DATA_209
   no shutdown
   ip address 10.1.109.2/24
   ip virtual-router address 10.1.109.1
!
interface Vlan210
   description DC1_DATA_210
   no shutdown
   ip address 10.1.110.2/24
   ip virtual-router address 10.1.110.1
!
interface Vlan211
   description DC1_DATA_211
   no shutdown
   ip address 10.1.111.2/24
   ip virtual-router address 10.1.111.1
!
interface Vlan212
   description DC1_DATA_212
   no shutdown
   ip address 10.1.112.2/24
   ip virtual-router address 10.1.112.1
!
interface Vlan213
   description DC1_DATA_213
   no shutdown
   ip address 10.1.113.2/24
   ip virtual-router address 10.1.113.1
!
interface Vlan214
   description DC1_DATA_214
   no shutdown
   ip address 10.1.114.2/24
   ip virtual-router address 10.1.114.1
!
interface Vlan215
   description DC1_DATA_215
   no shutdown
   ip address 10.1.115.2/24
   ip virtual-router address 10.1.115.1
!
interface Vlan216
   description DC1_DATA_216
   no shutdown
   ip address 10.1.116.2/24
   ip virtual-router address 10.1.116.1
!
interface Vlan217
   description DC1_DATA_217
   no shutdown
   ip address 10.1.117.2/24
   ip virtual-router address 10.1.117.1
!
interface Vlan218
   description DC1_DATA_218
   no shutdown
   ip address 10.1.118.2/24
   ip virtual-router address 10.1.118.1
!
interface Vlan219
   description DC1_DATA_219
   no shutdown
   ip address 10.1.119.2/24
   ip virtual-router address 10.1.119.1
!
interface Vlan220
   description DC1_DATA_220
   no shutdown
   ip address 10.1.120.2/24
   ip virtual-router address 10.1.120.1
!
interface Vlan221
   description DC1_DATA_221
   no shutdown
   ip address 10.1.121.2/24
   ip virtual-router address 10.1.121.1
!
interface Vlan222
   description DC1_DATA_222
   no shutdown
   ip address 10.1.122.2/24
   ip virtual-router address 10.1.122.1
!
interface Vlan223
   description DC1_DATA_223
   no shutdown
   ip address 10.1.123.2/24
   ip virtual-router address 10.1.123.1
!
interface Vlan224
   description DC1_DATA_224
   no shutdown
   ip address 10.1.124.2/24
   ip virtual-router address 10.1.124.1
!
interface Vlan225
   description DC1_DATA_225
   no shutdown
   ip address 10.1.125.2/24
   ip virtual-router address 10.1.125.1
!
interface Vlan226
   description DC1_DATA_226
   no shutdown
   ip address 10.1.126.2/24
   ip virtual-router address 10.1.126.1
!
interface Vlan227
   description DC1_DATA_227
   no shutdown
   ip address 10.1.127.2/24
   ip virtual-router address 10.1.127.1
!
interface Vlan228
   description DC1_DATA_228
   no shutdown
   ip address 10.1.128.2/24
   ip virtual-router address 10.1.128.1
!
interface Vlan229
   description DC1_DATA_229
   no shutdown
   ip address 10.1.129.2/24
   ip virtual-router address 10.1.129.1
!
interface Vlan230
   description DC1_DATA_230
   no shutdown
   ip address 10.1.130.2/24
   ip virtual-router address 10.1.130.1
!
interface Vlan231
   description DC1_DATA_231
   no shutdown
   ip address 10.1.131.2/24
   ip virtual-router address 10.1.131.1
!
interface Vlan232
   description DC1_DATA_232
   no shutdown
   ip address 10.1.132.2/24
   ip virtual-router address 10.1.132.1
!
interface Vlan233
   description DC1_DATA_233
   no shutdown
   ip address 10.1.133.2/24
   ip virtual-router address 10.1.133.1
!
interface Vlan234
   description DC1_DATA_234
   no shutdown
   ip address 10.1.134.2/24
   ip virtual-router address 10.1.134.1
!
interface Vlan235
   description DC1_DATA_235
   no shutdown
   ip address 10.1.135.2/24
   ip virtual-router address 10.1.135.1
!
interface Vlan236
   description DC1_DATA_236
   no shutdown
   ip address 10.1.136.2/24
   ip virtual-router address 10.1.136.1
!
interface Vlan237
   description DC1_DATA_237
   no shutdown
   ip address 10.1.137.2/24
   ip virtual-router address 10.1.137.1
!
interface Vlan238
   description DC1_DATA_238
   no shutdown
   ip address 10.1.138.2/24
   ip virtual-router address 10.1.138.1
!
interface Vlan239
   description DC1_DATA_239
   no shutdown
   ip address 10.1.139.2/24
   ip virtual-router address 10.1.139.1
!
interface Vlan240
   description DC1_DATA_240
   no shutdown
   ip address 10.1.140.2/24
   ip virtual-router address 10.1.140.1
!
interface Vlan241
   description DC1_DATA_241
   no shutdown
   ip address 10.1.141.2/24
   ip virtual-router address 10.1.141.1
!
interface Vlan242
   description DC1_DATA_242
   no shutdown
   ip address 10.1.142.2/24
   ip virtual-router address 10.1.142.1
!
interface Vlan243
   description DC1_DATA_243
   no shutdown
   ip address 10.1.143.2/24
   ip virtual-router address 10.1.143.1
!
interface Vlan244
   description DC1_DATA_244
   no shutdown
   ip address 10.1.144.2/24
   ip virtual-router address 10.1.144.1
!
interface Vlan245
   description DC1_DATA_245
   no shutdown
   ip address 10.1.145.2/24
   ip virtual-router address 10.1.145.1
!
interface Vlan246
   description DC1_DATA_246
   no shutdown
   ip address 10.1.146.2/24
   ip virtual-router address 10.1.146.1
!
interface Vlan247
   description DC1_DATA_247
   no shutdown
   ip address 10.1.147.2/24
   ip virtual-router address 10.1.147.1
!
interface Vlan248
   description DC1_DATA_248
   no shutdown
   ip address 10.1.148.2/24
   ip virtual-router address 10.1.148.1
!
interface Vlan249
   description DC1_DATA_249
   no shutdown
   ip address 10.1.149.2/24
   ip virtual-router address 10.1.149.1
!
interface Vlan250
   description DC1_DATA_250
   no shutdown
   ip address 10.1.150.2/24
   ip virtual-router address 10.1.150.1
!
interface Vlan251
   description DC1_DATA_251
   no shutdown
   ip address 10.1.151.2/24
   ip virtual-router address 10.1.151.1
!
interface Vlan252
   description DC1_DATA_252
   no shutdown
   ip address 10.1.152.2/24
   ip virtual-router address 10.1.152.1
!
interface Vlan253
   description DC1_DATA_253
   no shutdown
   ip address 10.1.153.2/24
   ip virtual-router address 10.1.153.1
!
interface Vlan254
   description DC1_DATA_254
   no shutdown
   ip address 10.1.154.2/24
   ip virtual-router address 10.1.154.1
!
interface Vlan255
   description DC1_DATA_255
   no shutdown
   ip address 10.1.155.2/24
   ip virtual-router address 10.1.155.1
!
interface Vlan256
   description DC1_DATA_256
   no shutdown
   ip address 10.1.156.2/24
   ip virtual-router address 10.1.156.1
!
interface Vlan257
   description DC1_DATA_257
   no shutdown
   ip address 10.1.157.2/24
   ip virtual-router address 10.1.157.1
!
interface Vlan258
   description DC1_DATA_258
   no shutdown
   ip address 10.1.158.2/24
   ip virtual-router address 10.1.158.1
!
interface Vlan259
   description DC1_DATA_259
   no shutdown
   ip address 10.1.159.2/24
   ip virtual-router address 10.1.159.1
!
interface Vlan260
   description DC1_DATA_260
   no shutdown
   ip address 10.1.160.2/24
   ip virtual-router address 10.1.160.1
!
interface Vlan261
   description DC1_DATA_261
   no shutdown
   ip address 10.1.161.2/24
   ip virtual-router address 10.1.161.1
!
interface Vlan262
   description DC1_DATA_262
   no shutdown
   ip address 10.1.162.2/24
   ip virtual-router address 10.1.162.1
!
interface Vlan263
   description DC1_DATA_263
   no shutdown
   ip address 10.1.163.2/24
   ip virtual-router address 10.1.163.1
!
interface Vlan264
   description DC1_DATA_264
   no shutdown
   ip address 10.1.164.2/24
   ip virtual-router address 10.1.164.1
!
interface Vlan265
   description DC1_DATA_265
   no shutdown
   ip address 10.1.165.2/24
   ip virtual-router address 10.1.165.1
!
interface Vlan266
   description DC1_DATA_266
   no shutdown
   ip address 10.1.166.2/24
   ip virtual-router address 10.1.166.1
!
interface Vlan267
   description DC1_DATA_267
   no shutdown
   ip address 10.1.167.2/24
   ip virtual-router address 10.1.167.1
!
interface Vlan268
   description DC1_DATA_268
   no shutdown
   ip address 10.1.168.2/24
   ip virtual-router address 10.1.168.1
!
interface Vlan269
   description DC1_DATA_269
   no shutdown
   ip address 10.1.169.2/24
   ip virtual-router address 10.1.169.1
!
interface Vlan270
   description DC1_DATA_270
   no shutdown
   ip address 10.1.170.2/24
   ip virtual-router address 10.1.170.1
!
interface Vlan271
   description DC1_DATA_271
   no shutdown
   ip address 10.1.171.2/24
   ip virtual-router address 10.1.171.1
!
interface Vlan272
   description DC1_DATA_272
   no shutdown
   ip address 10.1.172.2/24
   ip virtual-router address 10.1.172.1
!
interface Vlan273
   description DC1_DATA_273
   no shutdown
   ip address 10.1.173.2/24
   ip virtual-router address 10.1.173.1
!
interface Vlan274
   description DC1_DATA_274
   no shutdown
   ip address 10.1.174.2/24
   ip virtual-router address 10.1.174.1
!
interface Vlan275
   description DC1_DATA_275
   no shutdown
   ip address 10.1.175.2/24
   ip virtual-router address 10.1.175.1
!
interface Vlan276
   description DC1_DATA_276
   no shutdown
   ip address 10.1.176.2/24
   ip virtual-router address 10.1.176.1
!
interface Vlan277
   description DC1_DATA_277
   no shutdown
   ip address 10.1.177.2/24
   ip virtual-router address 10.1.177.1
!
interface Vlan278
   description DC1_DATA_278
   no shutdown
   ip address 10.1.178.2/24
   ip virtual-router address 10.1.178.1
!
interface Vlan279
   description DC1_DATA_279
   no shutdown
   ip address 10.1.179.2/24
   ip virtual-router address 10.1.179.1
!
interface Vlan280
   description DC1_DATA_280
   no shutdown
   ip address 10.1.180.2/24
   ip virtual-router address 10.1.180.1
!
interface Vlan281
   description DC1_DATA_281
   no shutdown
   ip address 10.1.181.2/24
   ip virtual-router address 10.1.181.1
!
interface Vlan282
   description DC1_DATA_282
   no shutdown
   ip address 10.1.182.2/24
   ip virtual-router address 10.1.182.1
!
interface Vlan283
   description DC1_DATA_283
   no shutdown
   ip address 10.1.183.2/24
   ip virtual-router address 10.1.183.1
!
interface Vlan284
   description DC1_DATA_284
   no shutdown
   ip address 10.1.184.2/24
   ip virtual-router address 10.1.184.1
!
interface Vlan285
   description DC1_DATA_285
   no shutdown
   ip address 10.1.185.2/24
   ip virtual-router address 10.1.185.1
!
interface Vlan286
   description DC1_DATA_286
   no shutdown
   ip address 10.1.186.2/24
   ip virtual-router address 10.1.186.1
!
interface Vlan287
   description DC1_DATA_287
   no shutdown
   ip address 10.1.187.2/24
   ip virtual-router address 10.1.187.1
!
interface Vlan288
   description DC1_DATA_288
   no shutdown
   ip address 10.1.188.2/24
   ip virtual-router address 10.1.188.1
!
interface Vlan289
   description DC1_DATA_289
   no shutdown
   ip address 10.1.189.2/24
   ip virtual-router address 10.1.189.1
!
interface Vlan290
   description DC1_DATA_290
   no shutdown
   ip address 10.1.190.2/24
   ip virtual-router address 10.1.190.1
!
interface Vlan291
   description DC1_DATA_291
   no shutdown
   ip address 10.1.191.2/24
   ip virtual-router address 10.1.191.1
!
interface Vlan292
   description DC1_DATA_292
   no shutdown
   ip address 10.1.192.2/24
   ip virtual-router address 10.1.192.1
!
interface Vlan293
   description DC1_DATA_293
   no shutdown
   ip address 10.1.193.2/24
   ip virtual-router address 10.1.193.1
!
interface Vlan294
   description DC1_DATA_294
   no shutdown
   ip address 10.1.194.2/24
   ip virtual-router address 10.1.194.1
!
interface Vlan295
   description DC1_DATA_295
   no shutdown
   ip address 10.1.195.2/24
   ip virtual-router address 10.1.195.1
!
interface Vlan296
   description DC1_DATA_296
   no shutdown
   ip address 10.1.196.2/24
   ip virtual-router address 10.1.196.1
!
interface Vlan297
   description DC1_DATA_297
   no shutdown
   ip address 10.1.197.2/24
   ip virtual-router address 10.1.197.1
!
interface Vlan298
   description DC1_DATA_298
   no shutdown
   ip address 10.1.198.2/24
   ip virtual-router address 10.1.198.1
!
interface Vlan299
   description DC1_DATA_299
   no shutdown
   ip address 10.1.199.2/24
   ip virtual-router address 10.1.199.1
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

Virtual Router MAC Address: 00:1c:73:00:dc:01

#### Virtual Router MAC Address Device Configuration

```eos
!
ip virtual-router mac-address 00:1c:73:00:dc:01
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

### Router OSPF

#### Router OSPF Summary

| Process ID | Router ID | Default Passive Interface | No Passive Interface | BFD | Max LSA | Default Information Originate | Log Adjacency Changes Detail | Auto Cost Reference Bandwidth | Maximum Paths | MPLS LDP Sync Default | Distribute List In |
| ---------- | --------- | ------------------------- | -------------------- | --- | ------- | ----------------------------- | ---------------------------- | ----------------------------- | ------------- | --------------------- | ------------------ |
| 100 | 10.252.1.1 | enabled | Vlan4093 | disabled | 12000 | disabled | disabled | - | - | - | - |

#### Router OSPF Router Redistribution

| Process ID | Source Protocol | Include Leaked | Route Map |
| ---------- | --------------- | -------------- | --------- |
| 100 | connected | disabled | - |

#### OSPF Interfaces

| Interface | Area | Cost | Point To Point |
| -------- | -------- | -------- | -------- |
| Vlan4093 | 0.0.0.0 | - | True |
| Loopback0 | 0.0.0.0 | - | - |

#### Router OSPF Device Configuration

```eos
!
router ospf 100
   router-id 10.252.1.1
   passive-interface default
   no passive-interface Vlan4093
   redistribute connected
   max-lsa 12000
   graceful-restart
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
