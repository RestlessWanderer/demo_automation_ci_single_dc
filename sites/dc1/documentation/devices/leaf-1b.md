# leaf-1b

Serial Number: SGD22402922

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
| Ethernet1 | L2_spine-1_Ethernet2 | *trunk | *110,120,130-299 | *- | *- | 1 |
| Ethernet2 | L2_spine-2_Ethernet2 | *trunk | *110,120,130-299 | *- | *- | 1 |
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
| Port-Channel1 | L2_DC1-SPINES_Port-Channel1 | trunk | 110,120,130-299 | - | - | - | - | 1 | - |
| Port-Channel47 | MLAG_leaf-1a_Port-Channel47 | trunk | - | - | MLAG | - | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel1
   description L2_DC1-SPINES_Port-Channel1
   no shutdown
   switchport trunk allowed vlan 110,120,130-299
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
