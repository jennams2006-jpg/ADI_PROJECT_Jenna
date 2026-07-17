# Specification Version Comparison Report

**Generated:** 2026-07-16T10:36:55  
**Old document:** `/home/eng-6990/PROJECT/extractor/ADI_PROJECT_Jenna/RISC_SPEC_OUTPUT/document.json` — riscv-2025.pdf (221 pages)  
**New document:** `/home/eng-6990/PROJECT/extractor/ADI_PROJECT_Jenna/RISC1_SPEC_OUTPUT/document1.json` — riscv-2026.pdf (213 pages)

🔴 **84** Critical Changes · 🟠 **93** Content Changes · 🟡 **375** Structural Changes · 🔵 **164** Relocations · ⚪ **1** Metadata

**Total changes:** 717

---

## Table of Contents

- [Summary](#summary)
- [🔴 Critical Changes](#critical-changes) (84)
  - [Requirement changes](#critical-changes-requirement-changes) (66)
  - [Numeric changes](#critical-changes-numeric-changes) (17)
  - [Requirement strength changes](#critical-changes-requirement-strength-changes) (1)
- [🟠 Content Changes](#content-changes) (93)
  - [Modified tables](#content-changes-modified-tables) (80)
  - [Modified notes](#content-changes-modified-notes) (13)
- [🟡 Structural Changes](#structural-changes) (375)
  - [Sections added](#structural-changes-sections-added) (197)
  - [Pages added](#structural-changes-pages-added) (85)
  - [Pages removed](#structural-changes-pages-removed) (93)
- [🔵 Relocations](#relocations) (164)
  - [Moved tables](#relocations-moved-tables) (163)
  - [Page shifts](#relocations-page-shifts) (1)
- [⚪ Metadata](#metadata) (1)
  - [Title](#metadata-title) (1)

---

## Summary

### By Area

| Category | Count |
|---|---|
| table | 243 |
| section | 197 |
| page | 187 |
| requirement | 76 |
| note | 13 |
| metadata | 1 |

### By Change Type

| Category | Count |
|---|---|
| added | 331 |
| moved | 164 |
| removed | 155 |
| modified | 67 |

### By Difference Category

| Category | Count |
|---|---|
| section_added | 197 |
| table_moved | 163 |
| page_removed | 93 |
| page_added | 85 |
| numeric_value_change | 37 |
| table_removed | 37 |
| requirement_added | 28 |
| minor_wording_change | 25 |
| requirement_removed | 22 |
| table_added | 17 |
| note_added | 4 |
| substantive_wording_change | 3 |
| note_removed | 3 |
| metadata_change | 1 |
| requirement_strength_change | 1 |
| structural_page_shift | 1 |

---

## 🔴 Critical Changes

### Requirement changes (66)

<details>
<summary>🔴 **CHG-0225** Requirement removed `Alternatively, the original CSR definition must specify that subfields can only be updated atomically, which may requ...` (p. 28) — 0% similar</summary>

**Page:** 28 → ?

**Preview:** Alternatively, the original CSR definition must specify that subfields can only be updated atomically, which may requ...

**Old:**
```
Alternatively, the original CSR definition must specify that subfields can only be updated atomically, which may require a two-instruction clear bit/set bit sequence in general that can be problematic if intermediate values are not legal.
```

**Detail:** Removed requirement

</details>

<details>
<summary>🔴 **CHG-0247** Requirement added `original CSR definition must specify that subfields can only be updated atomically, which may require a two-instructi...` (p. 32) — 0% similar</summary>

**Page:** ? → 32

**Preview:** original CSR definition must specify that subfields can only be updated atomically, which may require a two-instructi...

**New:**
```
original CSR definition must specify that subfields can only be updated atomically, which may require a two-instruction clear bit/set bit sequence in general that can be problematic if intermediate values are not legal.
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0248** Requirement added `All bits that are reserved for future use must return zero when read.` (p. 35) — 0% similar</summary>

**Page:** ? → 35

**New:**
```
All bits that are reserved for future use must return zero when read.
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0207** Requirement modified `Hart IDs might not necessarily be numbered contiguously in a multiprocessor system, but one hart must have a hart ID ...` (p. 38) — 97% similar</summary>

**Page:** 36 → 38

**Preview:** Hart IDs might not necessarily be numbered contiguously in a multiprocessor system, but one hart must have a hart ID ...

**Old:**
```
Hart IDs might not necessarily be numbered contiguously in a multiprocessor system, but at least one hart must have a hart ID of zero.
```

**New:**
```
Hart IDs might not necessarily be numbered contiguously in a multiprocessor system, but one hart must have a hart ID of zero.
```

**Detail:** Changed 'at least' to ''

</details>

<details>
<summary>🔴 **CHG-0226** Requirement removed `MXLEN-1 2 1 0 BASE[MXLEN-1:2] (WARL) MODE (WARL) MXLEN-2 2 The mtvec register must always be implemented, but can con...` (p. 46) — 0% similar</summary>

**Page:** 46 → ?

**Preview:** MXLEN-1 2 1 0 BASE[MXLEN-1:2] (WARL) MODE (WARL) MXLEN-2 2 The mtvec register must always be implemented, but can con...

**Old:**
```
MXLEN-1 2 1 0 BASE[MXLEN-1:2] (WARL) MODE (WARL) MXLEN-2 2 The mtvec register must always be implemented, but can contain a read-only value.
```

**Detail:** Removed requirement

</details>

<details>
<summary>🔴 **CHG-0227** Requirement removed `0b11 | OR | XS==0b11 OR VS==0b11)). This allows privileged code to quickly determine when no additional context save ...` (p. 46) — 0% similar</summary>

**Page:** 46 → ?

**Preview:** 0b11 | OR | XS==0b11 OR VS==0b11)). This allows privileged code to quickly determine when no additional context save ...

**Old:**
```
0b11 | OR | XS==0b11 OR VS==0b11)). This allows privileged code to quickly determine when no additional context save is required beyond the integer register set and pc. The floating-point unit state is always initialized, saved, and restored using standard instructions (F, D, and/or Q), and privileged code must be aware of FLEN to determine the appropriate space to reserve for each f register. Machine and Supervisor modes share a single copy of the FS, VS, and XS bits. Supervisor-level software normally uses the FS, VS, and XS bits directly to record the status with respect to the supervisor-level saved context. Machine-level software must be more conservative in saving and restoring the extension state in their corresponding version of the context.  In any reasonable use case, the number of context switches between user and supervisor level should far outweigh the number of context switches to other privilege levels. Note that coprocessors should not require their context to be saved and restored to service asynchronous interrupts, unless the interrupt results in a user-level context swap. 3.1.6.8. Previous Expected Landing Pad (ELP) State in mstatus Register The Zicfilp extension adds the SPELP and MPELP fields that hold the previous ELP, and are updated as specified in Section 22.1.2. The x PELP fields are encoded as follows: ⚫0-NO_LP_EXPECTED-no landing pad instruction expected. ⚫1-LP_EXPECTED-a landing pad instruction is expected. 3.1.7. Machine Trap-Vector Base-Address (mtvec) Register The mtvec register is an MXLEN-bit WARL read/write register that holds trap vector configuration, consisting of a vector base address (BASE) and a vector mode (MODE). MXLEN-1
```

**Detail:** Removed requirement

</details>

<details>
<summary>🔴 **CHG-0228** Requirement removed `Similarly, an implementation shall not fix as read-3.1.` (p. 47) — 0% similar</summary>

**Page:** 47 → ?

**Old:**
```
Similarly, an implementation shall not fix as read-3.1.
```

**Detail:** Removed requirement

</details>

<details>
<summary>🔴 **CHG-0249** Requirement added `0b11 | OR | XS==0b11 OR VS==0b11)). This allows privileged code to quickly determine when no additional context save ...` (p. 47) — 0% similar</summary>

**Page:** ? → 47

**Preview:** 0b11 | OR | XS==0b11 OR VS==0b11)). This allows privileged code to quickly determine when no additional context save ...

**New:**
```
0b11 | OR | XS==0b11 OR VS==0b11)). This allows privileged code to quickly determine when no additional context save is required beyond the integer register set and pc. 3.1. Machine-Level CSRs | Page
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0250** Requirement added `The floating-point unit state is always initialized, saved, and restored using standard instructions (F, D, and/or Q)...` (p. 48) — 0% similar</summary>

**Page:** ? → 48

**Preview:** The floating-point unit state is always initialized, saved, and restored using standard instructions (F, D, and/or Q)...

**New:**
```
The floating-point unit state is always initialized, saved, and restored using standard instructions (F, D, and/or Q), and privileged code must be aware of FLEN to determine the appropriate space to reserve for each f register.
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0251** Requirement added `Machine-level software must be more conservative in saving and restoring the extension state in their corresponding v...` (p. 48) — 0% similar</summary>

**Page:** ? → 48

**Preview:** Machine-level software must be more conservative in saving and restoring the extension state in their corresponding v...

**New:**
```
Machine-level software must be more conservative in saving and restoring the extension state in their corresponding version of the context.
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0252** Requirement added ` In any reasonable use case, the number of context switches between user and supervisor level should far outweigh th...` (p. 48) — 0% similar</summary>

**Page:** ? → 48

**Preview:**  In any reasonable use case, the number of context switches between user and supervisor level should far outweigh th...

**New:**
```
 In any reasonable use case, the number of context switches between user and supervisor level should far outweigh the number of context switches to other privilege levels.
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0253** Requirement added `Note that coprocessors should not require their context to be saved and restored to service asynchronous interrupts, ...` (p. 48) — 0% similar</summary>

**Page:** ? → 48

**Preview:** Note that coprocessors should not require their context to be saved and restored to service asynchronous interrupts, ...

**New:**
```
Note that coprocessors should not require their context to be saved and restored to service asynchronous interrupts, unless the interrupt results in a user-level context swap.
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0254** Requirement added `partial$bytefield/mtvec.edn The mtvec register must always be implemented, but can contain a read-only value.` (p. 48) — 0% similar</summary>

**Page:** ? → 48

**New:**
```
partial$bytefield/mtvec.edn The mtvec register must always be implemented, but can contain a read-only value.
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0229** Requirement removed `Bits of mie that are not writable must be read-only zero.` (p. 49) — 0% similar</summary>

**Page:** 49 → ?

**Old:**
```
Bits of mie that are not writable must be read-only zero.
```

**Detail:** Removed requirement

</details>

<details>
<summary>🔴 **CHG-0255** Requirement added `Similarly, an implementation shall not fix as read-only one any bits of mideleg corresponding to machine-level interr...` (p. 49) — 0% similar</summary>

**Page:** ? → 49

**Preview:** Similarly, an implementation shall not fix as read-only one any bits of mideleg corresponding to machine-level interr...

**New:**
```
Similarly, an implementation shall not fix as read-only one any bits of mideleg corresponding to machine-level interrupts (but may do so for lower-level interrupts).
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0256** Requirement added `not writable must be read-only zero.` (p. 51) — 0% similar</summary>

**Page:** ? → 51

**New:**
```
not writable must be read-only zero.
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0257** Requirement added `The USEED and SSEED fields of the mseccfg CSR must have defined reset values.` (p. 70) — 0% similar</summary>

**Page:** ? → 70

**New:**
```
The USEED and SSEED fields of the mseccfg CSR must have defined reset values.
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0258** Requirement added `The system must not allow them to be in an undefined state after reset.` (p. 70) — 0% similar</summary>

**Page:** ? → 70

**New:**
```
The system must not allow them to be in an undefined state after reset.
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0230** Requirement removed ` The Sv32 page-based virtual-memory scheme described in Section 12.3 supports 34-bit physical addresses for RV32, so...` (p. 75) — 0% similar</summary>

**Page:** 75 → ?

**Preview:**  The Sv32 page-based virtual-memory scheme described in Section 12.3 supports 34-bit physical addresses for RV32, so...

**Old:**
```
 The Sv32 page-based virtual-memory scheme described in Section 12.3 supports 34-bit physical addresses for RV32, so the PMP scheme must support addresses wider than XLEN for RV32.
```

**Detail:** Removed requirement

</details>

<details>
<summary>🔴 **CHG-0199** Requirement modified `Furthermore, when a non-speculative instruction fetch is performed, an implementation is permitted to additionally re...` (p. 76) — 100% similar</summary>

**Page:** 73 → 76

**Preview:** Furthermore, when a non-speculative instruction fetch is performed, an implementation is permitted to additionally re...

**Old:**
```
Furthermore, when a non-speculative instruction fetch is performed, an implementation is permitted to additionally read any of the bytes within the next naturally aligned power-of-2 region of the same size (with the address of the region taken modulo 2 XLEN.
```

**New:**
```
Furthermore, when a non-speculative instruction fetch is performed, an implementation is permitted to additionally read any of the bytes within the next naturally aligned power-of-2 region of the same size (with the address of the region taken modulo 2XLEN).
```

**Detail:** Changed '2 xlen.' to '2xlen).'

</details>

<details>
<summary>🔴 **CHG-0259** Requirement added ` The Sv32 page-based virtual-memory scheme described in Sv32: Page-Based 32-bit Virtual-Memory Systems supports 34-b...` (p. 77) — 0% similar</summary>

**Page:** ? → 77

**Preview:**  The Sv32 page-based virtual-memory scheme described in Sv32: Page-Based 32-bit Virtual-Memory Systems supports 34-b...

**New:**
```
 The Sv32 page-based virtual-memory scheme described in Sv32: Page-Based 32-bit Virtual-Memory Systems supports 34-bit physical addresses for RV32, so the PMP scheme must support addresses wider than XLEN for RV32.
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0231** Requirement removed `The effective privilege mode for implicit page-Implementations with virtual memory are permitted to perform address t...` (p. 78) — 0% similar</summary>

**Page:** 78 → ?

**Preview:** The effective privilege mode for implicit page-Implementations with virtual memory are permitted to perform address t...

**Old:**
```
The effective privilege mode for implicit page-Implementations with virtual memory are permitted to perform address translations speculatively and earlier than required by an explicit memory access, and are permitted to cache them in address translation cache structures—including possibly caching the identity mappings from effective address to physical address used in Bare translation modes and M-mode.
```

**Detail:** Removed requirement

</details>

<details>
<summary>🔴 **CHG-0260** Requirement added ` It is not possible to represent the address 2XLEN+2 as the top of a range, so, for example, in an RV32 system with ...` (p. 78) — 0% similar</summary>

**Page:** ? → 78

**Preview:**  It is not possible to represent the address 2XLEN+2 as the top of a range, so, for example, in an RV32 system with ...

**New:**
```
 It is not possible to represent the address 2XLEN+2 as the top of a range, so, for example, in an RV32 system with 34-bit physical addresses, a TOR PMP cannot be used to give less-privileged modes access to the uppermost word of memory.
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0220** Requirement modified `The matching PMP entry must match all bytes of a memory operation, or the operation fails, irrespective of the L, R, ...` (p. 79) — 86% similar</summary>

**Page:** 77 → 79

**Preview:** The matching PMP entry must match all bytes of a memory operation, or the operation fails, irrespective of the L, R, ...

**Old:**
```
The matching PMP entry must match all bytes of an access, or the access fails, irrespective of the L, R, W, and X bits.
```

**New:**
```
The matching PMP entry must match all bytes of a memory operation, or the operation fails, irrespective of the L, R, W, and X bits.
```

**Detail:** Changed 'an access,' to 'a memory operation,'

</details>

<details>
<summary>🔴 **CHG-0224** Requirement modified `instruction may generate multiple memory operations, which may not be mutually atomic.` (p. 80) — 78% similar</summary>

**Page:** 77 → 80

**Old:**
```
Note that a single instruction may generate multiple accesses, which may not be mutually atomic.
```

**New:**
```
instruction may generate multiple memory operations, which may not be mutually atomic.
```

**Detail:** Changed 'note that a single' to ''

</details>

<details>
<summary>🔴 **CHG-0261** Requirement added `Implementations with virtual memory are permitted to perform address translations speculatively and earlier than requ...` (p. 80) — 0% similar</summary>

**Page:** ? → 80

**Preview:** Implementations with virtual memory are permitted to perform address translations speculatively and earlier than requ...

**New:**
```
Implementations with virtual memory are permitted to perform address translations speculatively and earlier than required by an explicit memory access, and are permitted to cache them in address translation cache structures—including possibly caching the identity mappings from effective address to physical address used in Bare translation modes and M-mode.
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0232** Requirement removed `All mseccfg fields defined on this proposal are WARL, and the remaining bits are reserved for future standard use and...` (p. 91) — 0% similar</summary>

**Page:** 91 → ?

**Preview:** All mseccfg fields defined on this proposal are WARL, and the remaining bits are reserved for future standard use and...

**Old:**
```
All mseccfg fields defined on this proposal are WARL, and the remaining bits are reserved for future standard use and should always read zero.
```

**Detail:** Removed requirement

</details>

<details>
<summary>🔴 **CHG-0233** Requirement removed `The reset value of mseccfg is implementation-specific, otherwise if backwards compatibility is a requirement it shoul...` (p. 91) — 0% similar</summary>

**Page:** 91 → ?

**Preview:** The reset value of mseccfg is implementation-specific, otherwise if backwards compatibility is a requirement it shoul...

**Old:**
```
The reset value of mseccfg is implementation-specific, otherwise if backwards compatibility is a requirement it should reset to zero on hard reset.
```

**Detail:** Removed requirement

</details>

<details>
<summary>🔴 **CHG-0234** Requirement removed `Bits on pmpcfg register Result 1 0 1 0 Locked Shared code region: Execute only on both M and S/U mode.* 1 0 1 1 Locke...` (p. 93) — 0% similar</summary>

**Page:** 93 → ?

**Preview:** Bits on pmpcfg register Result 1 0 1 0 Locked Shared code region: Execute only on both M and S/U mode.* 1 0 1 1 Locke...

**Old:**
```
Bits on pmpcfg register Result 1 0 1 0 Locked Shared code region: Execute only on both M and S/U mode.* 1 0 1 1 Locked Shared code region: Execute only on S/U mode, read/execute on M mode.* 1 1 0 0 Locked Read-only region* Access Exception 1 1 0 1 Locked Read/Execute region* Access Exception 1 1 1 0 Locked Read/Write region* Access Exception 1 1 1 1 Locked Shared data region: Read only on both M and S/U mode.* : *Locked rules cannot be removed or modified until a PMP reset, unless mseccfg.RLB is set.
```

**Detail:** Removed requirement

</details>

<details>
<summary>🔴 **CHG-0262** Requirement added `Bits on pmpcfg register Result L R W X M Mode S/U Mode 0 0 0 0 Inaccessible region (Access Exception) 0 0 0 1 Access ...` (p. 93) — 0% similar</summary>

**Page:** ? → 93

**Preview:** Bits on pmpcfg register Result L R W X M Mode S/U Mode 0 0 0 0 Inaccessible region (Access Exception) 0 0 0 1 Access ...

**New:**
```
Bits on pmpcfg register Result L R W X M Mode S/U Mode 0 0 0 0 Inaccessible region (Access Exception) 0 0 0 1 Access Exception Execute-only region 0 0 1 0 Shared data region: Read/write on M mode, read-only on S/U mode 0 0 1 1 Shared data region: Read/write for both M and S/U mode 0 1 0 0 Access Exception Read-only region 0 1 0 1 Access Exception Read/Execute region 0 1 1 0 Access Exception Read/Write region 0 1 1 1 Access Exception Read/Write/Execute region 1 0 0 0 Locked inaccessible region* (Access Exception) 1 0 0 1 Locked Execute-only region* Access Exception 1 0 1 0 Locked Shared code region: Execute only on both M and S/U mode.* 1 0 1 1 Locked Shared code region: Execute only on S/U mode, read/execute on M mode.* 1 1 0 0 Locked Read-only region* Access Exception 1 1 0 1 Locked Read/Execute region* Access Exception 1 1 1 0 Locked Read/Write region* Access Exception 1 1 1 1 Locked Shared data region: Read only on both M and S/U mode.* : *Locked rules cannot be removed or modified until a PMP reset, unless mseccfg.RLB is set.
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0235** Requirement removed `segments between M-mode and S/U-mode, mseccfg.RLB needs to be implemented, or else such rules can only be added toget...` (p. 96) — 0% similar</summary>

**Page:** 96 → ?

**Preview:** segments between M-mode and S/U-mode, mseccfg.RLB needs to be implemented, or else such rules can only be added toget...

**Old:**
```
segments between M-mode and S/U-mode, mseccfg.RLB needs to be implemented, or else such rules can only be added together with mseccfg.MML being set on PMP Reset.
```

**Detail:** Removed requirement

</details>

<details>
<summary>🔴 **CHG-0263** Requirement added `For a Supervisor-level environment, extension Ssccfg (‘Ss’ for Privileged architecture and Supervisor-level extension...` (p. 100) — 0% similar</summary>

**Page:** ? → 100

**Preview:** For a Supervisor-level environment, extension Ssccfg (‘Ss’ for Privileged architecture and Supervisor-level extension...

**New:**
```
For a Supervisor-level environment, extension Ssccfg (‘Ss’ for Privileged architecture and Supervisor-level extension, ‘ccfg’ for Counter Configuration) provides access to delegated counters, and to new supervisor-level state.For a RISC-V hardware platform, Smcdeleg and Ssccfg must always be implemented in tandem.
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0264** Requirement added `A hypervisor running in S-mode without the benefit of the hypervisor extension of "H" Extension for Hypervisor Suppor...` (p. 129) — 0% similar</summary>

**Page:** ? → 129

**Preview:** A hypervisor running in S-mode without the benefit of the hypervisor extension of "H" Extension for Hypervisor Suppor...

**New:**
```
A hypervisor running in S-mode without the benefit of the hypervisor extension of "H" Extension for Hypervisor Support may need to emulate a device for U-mode if paravirtualization cannot be employed.
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0236** Requirement removed `A hypervisor running in S-mode without the benefit of the hypervisor extension of Chapter 21 may need to emulate a de...` (p. 133) — 0% similar</summary>

**Page:** 133 → ?

**Preview:** A hypervisor running in S-mode without the benefit of the hypervisor extension of Chapter 21 may need to emulate a de...

**Old:**
```
A hypervisor running in S-mode without the benefit of the hypervisor extension of Chapter 21 may need to emulate a device for U-mode if paravirtualization cannot be employed.
```

**Detail:** Removed requirement

</details>

<details>
<summary>🔴 **CHG-0201** Requirement modified `The PTE update must be atomic with respect to other accesses to the PTE, and must atomically perform all page-table w...` (p. 138) — 99% similar</summary>

**Page:** 142 → 138

**Preview:** The PTE update must be atomic with respect to other accesses to the PTE, and must atomically perform all page-table w...

**Old:**
```
The PTE update must be atomic with respect to other accesses to the PTE, and must atomically perform all tablewalk checks for that leaf PTE as part of, and before, conditionally updating the PTE value.
```

**New:**
```
The PTE update must be atomic with respect to other accesses to the PTE, and must atomically perform all page-table walk checks for that leaf PTE as part of, and before, conditionally updating the PTE value.
```

**Detail:** Changed 'tablewalk' to 'page-table walk'

</details>

<details>
<summary>🔴 **CHG-0265** Requirement added `The hart must not perform the memory access that caused the PTE update before the PTE update is globally visible.` (p. 139) — 0% similar</summary>

**Page:** ? → 139

**New:**
```
The hart must not perform the memory access that caused the PTE update before the PTE update is globally visible.
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0266** Requirement added ` This implies, for example, that an Sv48 implementation may not use two separate 4 B reads to non-atomically access ...` (p. 141) — 0% similar</summary>

**Page:** ? → 141

**Preview:**  This implies, for example, that an Sv48 implementation may not use two separate 4 B reads to non-atomically access ...

**New:**
```
 This implies, for example, that an Sv48 implementation may not use two separate 4 B reads to non-atomically access a single 8 B PTE, and that A/D bit updates performed by the implementation are treated as atomically updating the entire PTE, rather than just the A and/or D bit alone (even though the PTE value does not otherwise change).
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0237** Requirement removed `The hart must not perform the memory access that caused 12.3.` (p. 142) — 0% similar</summary>

**Page:** 142 → ?

**Old:**
```
The hart must not perform the memory access that caused 12.3.
```

**Detail:** Removed requirement

</details>

<details>
<summary>🔴 **CHG-0238** Requirement removed ` This implies, for example, that an Sv48 implementation may not use two separate 4B reads to non-atomically access a...` (p. 144) — 0% similar</summary>

**Page:** 144 → ?

**Preview:**  This implies, for example, that an Sv48 implementation may not use two separate 4B reads to non-atomically access a...

**Old:**
```
 This implies, for example, that an Sv48 implementation may not use two separate 4B reads to non-atomically access a single 8B PTE, and that A/D bit updates performed 12.3.
```

**Detail:** Removed requirement

</details>

<details>
<summary>🔴 **CHG-0267** Requirement added `Any level of PTE may be a leaf PTE, so in addition to 4 KiB pages, Sv57 supports 2 MiB megapages, 1 GiB gigapages, 51...` (p. 145) — 0% similar</summary>

**Page:** ? → 145

**Preview:** Any level of PTE may be a leaf PTE, so in addition to 4 KiB pages, Sv57 supports 2 MiB megapages, 1 GiB gigapages, 51...

**New:**
```
Any level of PTE may be a leaf PTE, so in addition to 4 KiB pages, Sv57 supports 2 MiB megapages, 1 GiB gigapages, 512 GiB terapages, and 256 TiB petapages, each of which must be virtually and physically aligned to a boundary equal to its size.
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0239** Requirement removed `Any level of PTE may be a leaf PTE, so in addition to pages, Sv57 supports megapages, gigapages, terapages, and petap...` (p. 149) — 0% similar</summary>

**Page:** 149 → ?

**Preview:** Any level of PTE may be a leaf PTE, so in addition to pages, Sv57 supports megapages, gigapages, terapages, and petap...

**Old:**
```
Any level of PTE may be a leaf PTE, so in addition to pages, Sv57 supports megapages, gigapages, terapages, and petapages, each of which must be virtually and physically aligned to a boundary equal to its size.
```

**Detail:** Removed requirement

</details>

<details>
<summary>🔴 **CHG-0240** Requirement removed `Bit 0, corresponding to instruction address-misaligned exceptions, must be writable if IALIGN=32.` (p. 169) — 0% similar</summary>

**Page:** 169 → ?

**Old:**
```
Bit 0, corresponding to instruction address-misaligned exceptions, must be writable if IALIGN=32.
```

**Detail:** Removed requirement

</details>

<details>
<summary>🔴 **CHG-0268** Requirement added ` For a hypervisor to benefit from the extension context status, it must have its own copy in the HS-level sstatus, m...` (p. 170) — 0% similar</summary>

**Page:** ? → 170

**Preview:**  For a hypervisor to benefit from the extension context status, it must have its own copy in the HS-level sstatus, m...

**New:**
```
 For a hypervisor to benefit from the extension context status, it must have its own copy in the HS-level sstatus, maintained independently of a guest OS running in VS-mode.
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0532** Page modified `Page 178` (p. 170) — 41% similar</summary>

**Page:** 178 → 170

**Old:**
```
reading back the value in hgatp to see which bit positions in the VMID field hold a one. The least-significant bits of VMID are implemented first: that is, if VMIDLEN > 0, VMID[VMIDLEN-1:0] is writable. The maximal value of VMIDLEN, termed VMIDMAX, is 7 for Sv32x4 or 14 for Sv39x4, Sv48x4, and Sv57x4. The hgatp register is considered active for the purposes of the address-translation algorithm unless the effective privilege mode is U and hstatus.HU=0.  This definition simplifies the implementation of speculative execution of HLV, HLVX, and HSV instructions. Note that writing hgatp does not imply any ordering constraints between page-table updates and subsequent G-stage address translations. If the new virtual machine’s guest physical page tables have been modified, or if a VMID is reused, it may be necessary to execute an HFENCE.GVMA instruction (see Section 21.3.2) before or after writing hgatp. 21.2.11. Virtual Supervisor Status (vsstatus) Register The vsstatus register is a VSXLEN-bit read/write register that is VS-mode’s version of supervisor register sstatus, formatted as shown in Figure 98 when VSXLEN=32 and Figure 99 when VSXLEN=64. When V=1, vsstatus substitutes for the usual sstatus, so instructions that normally read or modify sstatus actually access vsstatus instead. 0 1 2 4 5 6 7 8 9 10 11 12 13 14 15 WPRI SIE WPRI SPIE UBE WPRI SPP VS[1:0] WPRI FS[1:0] XS[1:0] 16 17 18 19 20 22 23 24 25 30 31 XS[1:0] WPRI SUM MXR WPRI SPELP SDT WPRI SD Figure 98. Virtual supervisor status (vsstatus) register when VSXLEN=32. 0 1 2 4 5 6 7 8 9 10 11 12 13 14 15 WPRI SIE WPRI SPIE UBE WPRI SPP VS[1:0] WPRI FS[1:0] XS[1:0] 16 17 18 19 20 22 23 24 25 31 XS[1:0] WPRI SUM MXR WPRI SPELP SDT WPRI 32 33 34 47 UXL[1:0] WPRI 48 62 63 WPRI SD Figure 99. Virtual supervisor status (vsstatus) register when VSXLEN=64. The UXL field controls the effective XLEN for VU-mode, which may differ from the XLEN for VS-mode (VSXLEN). When VSXLEN=32, the UXL field does not exist, and VU-mode XLEN=32. When VSXLEN=64, UXL is a WARL field that is encoded the same as the MXL field of misa, shown in Table 9. In particular, an implementation may make UXL be a read-only copy of field VSXL of hstatus, forcing VU-mode XLEN=VSXLEN. If VSXLEN is changed from 32 to a wider width, and if field UXL is not restricted to a single value, it gets the value corresponding to the widest supported width not wider than the new VSXLEN. When V=1, both vsstatus.FS and the HS-level sstatus.FS are in effect. Attempts to execute a floating-point instruction when either field is 0 (Off) raise an illegal-instruction exception. Modifying the floating-point state when V=1 causes both fields to be set to 3 (Dirty).  For a hypervisor to benefit from the extension context status, it must have its own 21.2. Hypervisor and Virtual Supervisor CSRs | Page 171 The RISC-V Instruction Set Manual: Volume II | © RISC-V International
```

**New:**
```
0 1 2 4 5 6 7 8 9 10 11 12 13 14 15 WPRI SIE WPRI SPIE UBE WPRI SPP VS[1:0] WPRI FS[1:0] XS[1:0] 16 17 18 19 20 22 23 24 25 31 XS[1:0] WPRI SUM MXR WPRI SPELP SDT WPRI 32 33 34 47 UXL[1:0] WPRI 48 62 63 WPRI SD Figure 67. Virtual supervisor status (vsstatus) register when VSXLEN=64. The UXL field controls the effective XLEN for VU-mode, which may differ from the XLEN for VS-mode (VSXLEN). When VSXLEN=32, the UXL field does not exist, and VU-mode XLEN=32. When VSXLEN=64, UXL is a WARL field that is encoded the same as the MXL field of misa, shown in Encoding of MXL field in misa. In particular, an implementation may make UXL be a read-only copy of field VSXL of hstatus, forcing VU-mode XLEN=VSXLEN. If VSXLEN is changed from 32 to a wider width, and if field UXL is not restricted to a single value, it gets the value corresponding to the widest supported width not wider than the new VSXLEN. When V=1, both vsstatus.FS and the HS-level sstatus.FS are in effect. Attempts to execute a floating-point instruction when either field is 0 (Off) raise an illegal-instruction exception. Modifying the floating-point state when V=1 causes both fields to be set to 3 (Dirty).  For a hypervisor to benefit from the extension context status, it must have its own copy in the HS-level sstatus, maintained independently of a guest OS running in VS-mode. While a version of the extension context status obviously must exist in vsstatus for VS-mode, a hypervisor cannot rely on this version being maintained correctly, given that VS-level software can change vsstatus.FS arbitrarily. If the HS-level sstatus.FS were not independently active and maintained by the hardware in parallel with vsstatus.FS while V=1, hypervisors would always be forced to conservatively swap all floating-point state when context-switching between virtual machines. Similarly, when V=1, both vsstatus.VS and the HS-level sstatus.VS are in effect. Attempts to execute a vector instruction when either field is 0 (Off) raise an illegal-instruction exception. Modifying the vector state when V=1 causes both fields to be set to 3 (Dirty). Read-only fields SD and XS summarize the extension context status as it is visible to VS-mode only. For example, the value of the HS-level sstatus.FS does not affect vsstatus.SD. An implementation may make field UBE be a read-only copy of hstatus.VSBE. When V=0, vsstatus does not directly affect the behavior of the machine, unless a virtual-machine load/store (HLV, HLVX, or HSV) or the MPRV feature in the mstatus register is used to execute a load or store as though V=1. The Zicfilp extension adds the SPELP field that holds the previous ELP, and is updated as specified in Preserving Expected Landing Pad State on Traps. The SPELP field is encoded as follows: ⚫0-NO_LP_EXPECTED-no landing pad instruction expected. ⚫1-LP_EXPECTED-a landing pad instruction is expected. The Ssdbltrp adds an S-mode-disable-trap (SDT) field extension to address double trap (See Double Trap Control in sstatus Register) in VS-mode. 15.2. Hypervisor and Virtual Supervisor CSRs | Page 163 The RISC-V Instruction Set Manual, Volume II | © RISC-V International
```

**Detail:** Changed 'reading back the value in hgatp to see which bit positions in the vmid field hold a one. the least-significant bits of vmid are implemented first: that is, if vmidlen > 0, vmid[vmidlen-1:0] is writable. the maximal value of vmidlen, termed vmidmax, is 7 for sv32x4 or 14 for sv39x4, sv48x4, and sv57x4. the hgatp register is considered active for the purposes of the address-translation algorithm unless the effective privilege mode is u and hstatus.hu=0.  this definition simplifies the implementation of speculative execution of hlv, hlvx, and hsv instructions. note that writing hgatp does not imply any ordering constraints between page-table updates and subsequent g-stage address translations. if the new virtual machine’s guest physical page tables have been modified, or if a vmid is reused, it may be necessary to execute an hfence.gvma instruction (see section 21.3.2) before or after writing hgatp. 21.2.11. virtual supervisor status (vsstatus) register the vsstatus register is a vsxlen-bit read/write register that is vs-mode’s version of supervisor register sstatus, formatted as shown in figure 98 when vsxlen=32 and figure 99 when vsxlen=64. when v=1, vsstatus substitutes for the usual sstatus, so instructions that normally read or modify sstatus actually access vsstatus instead.' to ''

</details>

<details>
<summary>🔴 **CHG-0211** Requirement modified ` In particular, virtual-machine load/store (HLV, HLVX, or HSV) instructions that are mispredicted must not cause VS-...` (p. 173) — 94% similar</summary>

**Page:** 182 → 173

**Preview:**  In particular, virtual-machine load/store (HLV, HLVX, or HSV) instructions that are mispredicted must not cause VS-...

**Old:**
```
 In particular, virtual-machine load/store (HLV, HLVX, or HSV) instructions that are misspeculatively executed must not cause VS-stage A bits to be set.
```

**New:**
```
 In particular, virtual-machine load/store (HLV, HLVX, or HSV) instructions that are mispredicted must not cause VS-stage A bits to be set.
```

**Detail:** Changed 'misspeculatively executed' to 'mispredicted'

</details>

<details>
<summary>🔴 **CHG-0269** Requirement added `Instructions HLV.WU, HLV.D, and HSV.D are not valid for RV32, of course.` (p. 174) — 0% similar</summary>

**Page:** ? → 174

**New:**
```
Instructions HLV.WU, HLV.D, and HSV.D are not valid for RV32, of course.
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0533** Page modified `Page 183` (p. 175) — 62% similar</summary>

**Page:** 183 → 175

**Old:**
```
HSV.D are not valid for RV32, of course. Instructions HLVX.HU and HLVX.WU are the same as HLV.HU and HLV.WU, except that execute permission takes the place of read permission during address translation. That is, the memory being read must be executable in both stages of address translation, but read permission is not required. For the supervisor physical address that results from address translation, the supervisor physical memory attributes must grant both execute and read permissions. (The supervisor physical memory attributes are the machine’s physical memory attributes as modified by physical memory protection, Section 3.7, for supervisor level.)  HLVX cannot override machine-level physical memory protection (PMP), so attempting to read memory that PMP designates as execute-only still results in an access-fault exception. Although HLVX instructions’ explicit memory accesses require execute permissions, they still raise the same exceptions as other load instructions, rather than raising fetch exceptions instead. HLVX.WU is valid for RV32, even though LWU and HLV.WU are not. (For RV32, HLVX.WU can be considered a variant of HLV.W, as sign extension is irrelevant for 32-bit values.) Attempts to execute a virtual-machine load/store instruction (HLV, HLVX, or HSV) when V=1 cause a virtual-instruction exception. Attempts to execute one of these same instructions from U-mode when hstatus.HU=0 cause an illegal-instruction exception. 21.3.2. Hypervisor Memory-Management Fence Instructions 0 6 7 11 12 14 15 19 20 24 25 31 opcode rd funct3 rs1 rs2 funct7 7 SYSTEM SYSTEM 5 0 0 3 PRIV PRIV 5 vaddr gaddr 5 asid vmid 7 HFENCE.VVMA HFENCE.GVMA The hypervisor memory-management fence instructions, HFENCE.VVMA and HFENCE.GVMA, perform a function similar to SFENCE.VMA (Section 12.2.1), except applying to the VS-level memory-management data structures controlled by CSR vsatp (HFENCE.VVMA) or the guest-physical memory-management data structures controlled by CSR hgatp (HFENCE.GVMA). Instruction SFENCE.VMA applies only to the memory-management data structures controlled by the current satp (either the HS-level satp when V=0 or vsatp when V=1). HFENCE.VVMA is valid only in M-mode or HS-mode. Its effect is much the same as temporarily entering VS-mode and executing SFENCE.VMA. Executing an HFENCE.VVMA guarantees that any previous stores already visible to the current hart are ordered before all implicit reads by that hart done for VS-stage address translation for instructions that ⚫are subsequent to the HFENCE.VVMA, and ⚫execute when hgatp.VMID has the same setting as it did when HFENCE.VVMA executed. Implicit reads need not be ordered when hgatp.VMID is different than at the time HFENCE.VVMA executed. If operand rs1≠x0, it specifies a single guest virtual address, and if operand rs2≠x0, it specifies a single guest address-space identifier (ASID).  An HFENCE.VVMA instruction applies only to a single virtual machine, identified by 21.3. Hypervisor Instructions | Page 176 The RISC-V Instruction Set Manual: Volume II | © RISC-V International
```

**New:**
```
considered a variant of HLV.W, as sign extension is irrelevant for 32-bit values.) The memory accesses performed by the HLVX.* instructions are not subject to pointer masking (see Pointer Masking Extensions).  HLVX.* instructions, designed for emulating implicit access to fetch instructions from guest memory, perform memory accesses that are exempt from pointer masking to facilitate this emulation. For the same reason, pointer masking does not apply when MXR is set. Attempts to execute a virtual-machine load/store instruction (HLV, HLVX, or HSV) when V=1 cause a virtual-instruction exception. Attempts to execute one of these same instructions from U-mode when hstatus.HU=0 cause an illegal-instruction exception. 15.3.2. Hypervisor Memory-Management Fence Instructions 0 6 7 11 12 14 15 19 20 24 25 31 opcode rd funct3 rs1 rs2 funct7 7 SYSTEM SYSTEM 5 0 0 3 PRIV PRIV 5 vaddr gaddr 5 asid vmid 7 HFENCE.VVMA HFENCE.GVMA The hypervisor memory-management fence instructions, HFENCE.VVMA and HFENCE.GVMA, perform a function similar to SFENCE.VMA (Supervisor Memory-Management Fence Instruction), except applying to the VS-level memory-management data structures controlled by CSR vsatp (HFENCE.VVMA) or the guest-physical memory-management data structures controlled by CSR hgatp (HFENCE.GVMA). Instruction SFENCE.VMA applies only to the memory-management data structures controlled by the current satp (either the HS-level satp when V=0 or vsatp when V=1). HFENCE.VVMA is valid only in M-mode or HS-mode. Its effect is much the same as temporarily entering VS-mode and executing SFENCE.VMA. Executing an HFENCE.VVMA guarantees that any previous stores already visible to the current hart are ordered before all implicit reads by that hart done for VS-stage address translation for instructions that ⚫are subsequent to the HFENCE.VVMA, and ⚫execute when hgatp.VMID has the same setting as it did when HFENCE.VVMA executed. Implicit reads need not be ordered when hgatp.VMID is different than at the time HFENCE.VVMA executed. If operand rs1≠x0, it specifies a single guest virtual address, and if operand rs2≠x0, it specifies a single guest address-space identifier (ASID).  An HFENCE.VVMA instruction applies only to a single virtual machine, identified by the setting of hgatp.VMID when HFENCE.VVMA executes. When rs2≠x0, bits XLEN-1:ASIDMAX of the value held in rs2 are reserved for future standard use. Until their use is defined by a standard extension, they should be zeroed by software and ignored by current implementations. Furthermore, if ASIDLEN < ASIDMAX, the implementation shall ignore bits ASIDMAX-1:ASIDLEN of the value held in rs2.  Simpler implementations of HFENCE.VVMA can ignore the guest virtual address in rs1 and the guest ASID value in rs2, as well as hgatp.VMID, and always perform a global fence for the VS-level memory management of all virtual machines, or even a global fence for all memory-management data structures. Neither mstatus.TVM nor hstatus.VTVM causes HFENCE.VVMA to trap. 15.3. Hypervisor Instructions | Page 168 The RISC-V Instruction Set Manual, Volume II | © RISC-V International
```

**Detail:** Changed 'hsv.d are not valid for rv32, of course. instructions hlvx.hu and hlvx.wu are the same as hlv.hu and hlv.wu, except that execute permission takes the place of read permission during address translation. that is, the memory being read must be executable in both stages of address translation, but read permission is not required. for the supervisor physical address that results from address translation, the supervisor physical memory attributes must grant both execute and read permissions. (the supervisor physical memory attributes are the machine’s physical memory attributes as modified by physical memory protection, section 3.7, for supervisor level.)  hlvx cannot override machine-level physical memory protection (pmp), so attempting to read memory that pmp designates as execute-only still results in an access-fault exception. although hlvx instructions’ explicit memory accesses require execute permissions, they still raise the same exceptions as other load instructions, rather than raising fetch exceptions instead. hlvx.wu is valid for rv32, even though lwu and hlv.wu are not. (for rv32, hlvx.wu can be' to ''

</details>

<details>
<summary>🔴 **CHG-0270** Requirement added `If hgatp.MODE is changed for a given VMID, an HFENCE.GVMA with rs1=x0 (and rs2 set to either x0 or the VMID) must be ...` (p. 176) — 0% similar</summary>

**Page:** ? → 176

**Preview:** If hgatp.MODE is changed for a given VMID, an HFENCE.GVMA with rs1=x0 (and rs2 set to either x0 or the VMID) must be ...

**New:**
```
If hgatp.MODE is changed for a given VMID, an HFENCE.GVMA with rs1=x0 (and rs2 set to either x0 or the VMID) must be executed to order subsequent guest translations with the MODE change—even if the old MODE or new MODE is Bare.
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0534** Page modified `Page 185` (p. 177) — 56% similar</summary>

**Page:** 185 → 177

**Old:**
```
the VMID) must be executed to order subsequent guest translations with the MODE change—even if the old MODE or new MODE is Bare. Attempts to execute HFENCE.VVMA or HFENCE.GVMA when V=1 cause a virtual-instruction exception, while attempts to do the same in U-mode cause an illegal-instruction exception. Attempting to execute HFENCE.GVMA in HS-mode when mstatus.TVM=1 also causes an illegal-instruction exception. 21.4. Machine-Level CSRs The hypervisor extension augments or modifies machine CSRs mstatus, mstatush, mideleg, mip, and mie, and adds CSRs mtval2 and mtinst. 21.4.1. Machine Status (mstatus and mstatush) Registers The hypervisor extension adds two fields, MPV and GVA, to the machine-level mstatus or mstatush CSR, and modifies the behavior of several existing mstatus fields. Figure 111 shows the modified mstatus register when the hypervisor extension is implemented and MXLEN=64. When MXLEN=32, the hypervisor extension adds MPV and GVA not to mstatus but to mstatush. Figure 112 shows the mstatush register when the hypervisor extension is implemented and MXLEN=32. 63 62 40 39 38 37 36 35 34 33 32 SD WPRI MPV GVA MBE SBE SXL[1:0] UXL[1:0] 1 23 1 1 1 1 2 2 31 23 22 21 20 19 18 17 16 15 14 13 WPRI TSR TW TVM MXR SUM MPRV XS[1:0] FS[1:0] 9 1 1 1 1 1 1 2 2 12 11 10 9 8 7 6 5 4 3 2 1 0 MPP[1:0] VS[1:0] SPP MPIE UBE SPIE WPRI MIE WPRI SIE WPRI 2 2 1 1 1 1 1 1 1 1 1 Figure 111. Machine status (mstatus) register for RV64 when the hypervisor extension is implemented. 31 8 7 6 5 4 3 0 WPRI MPV GVA MBE SBE WPRI 24 1 1 1 1 4 Figure 112. Additional machine status (mstatush) register for RV32 when the hypervisor extension is implemented. The format of mstatus is unchanged for RV32. The MPV bit (Machine Previous Virtualization Mode) is written by the implementation whenever a trap is taken into M-mode. Just as the MPP field is set to the (nominal) privilege mode at the time of the trap, the MPV bit is set to the value of the virtualization mode V at the time of the trap. When an MRET instruction is executed, the virtualization mode V is set to MPV, unless MPP=3, in which case V remains 0. Field GVA (Guest Virtual Address) is written by the implementation whenever a trap is taken into M-mode. For any trap (breakpoint, address misaligned, access fault, page fault, or guest-page fault) that writes a guest virtual address to mtval, GVA is set to 1. For any other trap into M-mode, GVA is set to 0. The TSR and TVM fields of mstatus affect execution only in HS-mode, not in VS-mode. The TW field affects execution in all modes except M-mode. 21.4. Machine-Level CSRs | Page 178 The RISC-V Instruction Set Manual: Volume II | © RISC-V International
```

**New:**
```
extension adds MPV and GVA not to mstatus but to mstatush. Figure 80 shows the mstatush register when the hypervisor extension is implemented and MXLEN=32. 63 62 40 39 38 37 36 35 34 33 32 SD WPRI MPV GVA MBE SBE SXL[1:0] UXL[1:0] 1 23 1 1 1 1 2 2 31 23 22 21 20 19 18 17 16 15 14 13 WPRI TSR TW TVM MXR SUM MPRV XS[1:0] FS[1:0] 9 1 1 1 1 1 1 2 2 12 11 10 9 8 7 6 5 4 3 2 1 0 MPP[1:0] VS[1:0] SPP MPIE UBE SPIE WPRI MIE WPRI SIE WPRI 2 2 1 1 1 1 1 1 1 1 1 Figure 79. Machine status (mstatus) register for RV64 when the hypervisor extension is implemented. 31 8 7 6 5 4 3 0 WPRI MPV GVA MBE SBE WPRI 24 1 1 1 1 4 Figure 80. Additional machine status (mstatush) register for RV32 when the hypervisor extension is implemented. The format of mstatus is unchanged for RV32. The MPV bit (Machine Previous Virtualization Mode) is written by the implementation whenever a trap is taken into M-mode. Just as the MPP field is set to the (nominal) privilege mode at the time of the trap, the MPV bit is set to the value of the virtualization mode V at the time of the trap. When an MRET instruction is executed, the virtualization mode V is set to MPV, unless MPP=3, in which case V remains 0. Field GVA (Guest Virtual Address) is written by the implementation whenever a trap is taken into M-mode. For any trap (breakpoint, address misaligned, access fault, page fault, or guest-page fault) that writes a guest virtual address to mtval, GVA is set to 1. For any other trap into M-mode, GVA is set to 0. The TSR and TVM fields of mstatus affect execution only in HS-mode, not in VS-mode. The TW field affects execution in all modes except M-mode. Setting TVM=1 prevents HS-mode from accessing hgatp or executing HFENCE.GVMA or HINVAL.GVMA, but has no effect on accesses to vsatp or instructions HFENCE.VVMA or HINVAL.VVMA.  TVM exists in mstatus to allow machine-level software to modify the address translations managed by a supervisor-level OS, usually for the purpose of inserting another stage of address translation below that controlled by the OS. The instruction traps enabled by TVM=1 permit machine level to co-opt both satp and hgatp and substitute shadow page tables that merge the OS’s chosen page translations with M-level’s lower-stage translations, all without the OS being aware. M-level software needs this ability not only to emulate the hypervisor extension if not already supported, but also to emulate any future RISC-V extensions that may modify or add address translation stages, perhaps, for example, to improve support for nested hypervisors, i.e., running hypervisors atop other hypervisors. However, setting TVM=1 does not cause traps for accesses to vsatp or instructions HFENCE.VVMA or HINVAL.VVMA, or for any actions taken in VS-mode, because M-level software is not expected to need to involve itself in VS-stage address translation. For virtual machines, it should be sufficient, and in all likelihood faster as well, to leave VS-stage address translation alone and merge all other translation stages into G-stage shadow page tables controlled by hgatp. This assumption does place some constraints on possible future RISC-V 15.4. Machine-Level CSRs | Page 170 The RISC-V Instruction Set Manual, Volume II | © RISC-V International
```

**Detail:** Changed 'the vmid) must be executed to order subsequent guest translations with the mode change—even if the old mode or new mode is bare. attempts to execute hfence.vvma or hfence.gvma when v=1 cause a virtual-instruction exception, while attempts to do the same in u-mode cause an illegal-instruction exception. attempting to execute hfence.gvma in hs-mode when mstatus.tvm=1 also causes an illegal-instruction exception. 21.4. machine-level csrs the hypervisor extension augments or modifies machine csrs mstatus, mstatush, mideleg, mip, and mie, and adds csrs mtval2 and mtinst. 21.4.1. machine status (mstatus and mstatush) registers the hypervisor extension adds two fields, mpv and gva, to the machine-level mstatus or mstatush csr, and modifies the behavior of several existing mstatus fields. figure 111 shows the modified mstatus register when the hypervisor extension is implemented and mxlen=64. when mxlen=32, the hypervisor' to ''

</details>

<details>
<summary>🔴 **CHG-0241** Requirement removed ` For a hypervisor to benefit from the extension context status, it must have its own 21.2.` (p. 178) — 0% similar</summary>

**Page:** 178 → ?

**Old:**
```
 For a hypervisor to benefit from the extension context status, it must have its own 21.2.
```

**Detail:** Removed requirement

</details>

<details>
<summary>🔴 **CHG-0535** Page modified `Page 186` (p. 178) — 57% similar</summary>

**Page:** 186 → 178

**Old:**
```
Setting TVM=1 prevents HS-mode from accessing hgatp or executing HFENCE.GVMA or HINVAL.GVMA, but has no effect on accesses to vsatp or instructions HFENCE.VVMA or HINVAL.VVMA.  TVM exists in mstatus to allow machine-level software to modify the address translations managed by a supervisor-level OS, usually for the purpose of inserting another stage of address translation below that controlled by the OS. The instruction traps enabled by TVM=1 permit machine level to co-opt both satp and hgatp and substitute shadow page tables that merge the OS’s chosen page translations with M-level’s lower-stage translations, all without the OS being aware. M-level software needs this ability not only to emulate the hypervisor extension if not already supported, but also to emulate any future RISC-V extensions that may modify or add address translation stages, perhaps, for example, to improve support for nested hypervisors, i.e., running hypervisors atop other hypervisors. However, setting TVM=1 does not cause traps for accesses to vsatp or instructions HFENCE.VVMA or HINVAL.VVMA, or for any actions taken in VS-mode, because M-level software is not expected to need to involve itself in VS-stage address translation. For virtual machines, it should be sufficient, and in all likelihood faster as well, to leave VS-stage address translation alone and merge all other translation stages into G-stage shadow page tables controlled by hgatp. This assumption does place some constraints on possible future RISC-V extensions that current machines will be able to emulate efficiently. The hypervisor extension changes the behavior of the Modify Privilege field, MPRV, of mstatus. When MPRV=0, translation and protection behave as normal. When MPRV=1, explicit memory accesses are translated and protected, and endianness is applied, as though the current virtualization mode were set to MPV and the current nominal privilege mode were set to MPP. Table 42 enumerates the cases. Table 42. Effect of MPRV on the translation and protection of explicit memory accesses. MPRV MPV MPP Effect 0--Normal access; current privilege mode applies. 1 0 0 U-level access with HS-level translation and protection only. 1 0 1 HS-level access with HS-level translation and protection only. 1-3 M-level access with no translation. 1 1 0 VU-level access with two-stage translation and protection. The HS-level MXR bit makes any executable page readable. vsstatus.MXR makes readable those pages marked executable at the VS translation stage, but only if readable at the guest-physical translation stage. 1 1 1 VS-level access with two-stage translation and protection. The HS-level MXR bit makes any executable page readable. vsstatus.MXR makes readable those pages marked executable at the VS translation stage, but only if readable at the guest-physical translation stage. vsstatus.SUM applies instead of the HS-level SUM bit. MPRV does not affect the virtual-machine load/store instructions, HLV, HLVX, and HSV. The explicit loads and stores of these instructions always act as though V=1 and the nominal privilege mode were hstatus.SPVP, overriding MPRV. The mstatus register is a superset of the HS-level sstatus register but is not a superset of vsstatus. 21.4. Machine-Level CSRs | Page 179 The RISC-V Instruction Set Manual: Volume II | © RISC-V International
```

**New:**
```
extensions that current machines will be able to emulate efficiently. The hypervisor extension changes the behavior of the Modify Privilege field, MPRV, of mstatus. When MPRV=0, translation and protection behave as normal. When MPRV=1, explicit memory accesses are translated and protected, and endianness is applied, as though the current virtualization mode were set to MPV and the current nominal privilege mode were set to MPP. Table 49 enumerates the cases. Table 49. Effect of MPRV on the translation and protection of explicit memory accesses. MPRV MPV MPP Effect 0--Normal access; current privilege mode applies. 1 0 0 U-level access with HS-level translation and protection only. 1 0 1 HS-level access with HS-level translation and protection only. 1-3 M-level access with no translation. 1 1 0 VU-level access with two-stage translation and protection. The HS-level MXR bit makes any executable page readable. vsstatus.MXR makes readable those pages marked executable at the VS translation stage, but only if readable at the guest-physical translation stage. 1 1 1 VS-level access with two-stage translation and protection. The HS-level MXR bit makes any executable page readable. vsstatus.MXR makes readable those pages marked executable at the VS translation stage, but only if readable at the guest-physical translation stage. vsstatus.SUM applies instead of the HS-level SUM bit. MPRV does not affect the virtual-machine load/store instructions, HLV, HLVX, and HSV. The explicit loads and stores of these instructions always act as though V=1 and the nominal privilege mode were hstatus.SPVP, overriding MPRV. The mstatus register is a superset of the HS-level sstatus register but is not a superset of vsstatus. 15.4.2. Machine Interrupt Delegation (mideleg) Register When the hypervisor extension is implemented, bits 10, 6, and 2 of mideleg (corresponding to the standard VS-level interrupts) are each read-only one. Furthermore, if any guest external interrupts are implemented (GEILEN is nonzero), bit 12 of mideleg (corresponding to supervisor-level guest external interrupts) is also read-only one. VS-level interrupts and guest external interrupts are always delegated past M-mode to HS-mode. For bits of mideleg that are zero, the corresponding bits in hideleg, hip, and hie are read-only zeros. 15.4.3. Machine Interrupt (mip and mie) Registers The hypervisor extension gives registers mip and mie additional active bits for the hypervisor-added interrupts. Figure 81 and Figure 82 show the standard portions (bits 15:0) of registers mip and mie when the hypervisor extension is implemented. 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 0 LCOFIP SGEIP MEIP VSEIP SEIP 0 MTIP VSTIP STIP 0 MSIP VSSIP SSIP 0 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 Figure 81. Standard portion (bits 15:0) of mip. 15.4. Machine-Level CSRs | Page 171 The RISC-V Instruction Set Manual, Volume II | © RISC-V International
```

**Detail:** Changed 'setting tvm=1 prevents hs-mode from accessing hgatp or executing hfence.gvma or hinval.gvma, but has no effect on accesses to vsatp or instructions hfence.vvma or hinval.vvma.  tvm exists in mstatus to allow machine-level software to modify the address translations managed by a supervisor-level os, usually for the purpose of inserting another stage of address translation below that controlled by the os. the instruction traps enabled by tvm=1 permit machine level to co-opt both satp and hgatp and substitute shadow page tables that merge the os’s chosen page translations with m-level’s lower-stage translations, all without the os being aware. m-level software needs this ability not only to emulate the hypervisor extension if not already supported, but also to emulate any future risc-v extensions that may modify or add address translation stages, perhaps, for example, to improve support for nested hypervisors, i.e., running hypervisors atop other hypervisors. however, setting tvm=1 does not cause traps for accesses to vsatp or instructions hfence.vvma or hinval.vvma, or for any actions taken in vs-mode, because m-level software is not expected to need to involve itself in vs-stage address translation. for virtual machines, it should be sufficient, and in all likelihood faster as well, to leave vs-stage address translation alone and merge all other translation stages into g-stage shadow page tables controlled by hgatp. this assumption does place some constraints on possible future risc-v' to ''

</details>

<details>
<summary>🔴 **CHG-0536** Page modified `Page 187` (p. 179) — 49% similar</summary>

**Page:** 187 → 179

**Old:**
```
21.4.2. Machine Interrupt Delegation (mideleg) Register When the hypervisor extension is implemented, bits 10, 6, and 2 of mideleg (corresponding to the standard VS-level interrupts) are each read-only one. Furthermore, if any guest external interrupts are implemented (GEILEN is nonzero), bit 12 of mideleg (corresponding to supervisor-level guest external interrupts) is also read-only one. VS-level interrupts and guest external interrupts are always delegated past M-mode to HS-mode. For bits of mideleg that are zero, the corresponding bits in hideleg, hip, and hie are read-only zeros. 21.4.3. Machine Interrupt (mip and mie) Registers The hypervisor extension gives registers mip and mie additional active bits for the hypervisor-added interrupts. Figure 113 and Figure 114 show the standard portions (bits 15:0) of registers mip and mie when the hypervisor extension is implemented. 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 0 LCOFIP SGEIP MEIP VSEIP SEIP 0 MTIP VSTIP STIP 0 MSIP VSSIP SSIP 0 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 Figure 113. Standard portion (bits 15:0) of mip. 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 0 LCOFIE SGEIE MEIE VSEIE SEIE 0 MTIE VSTIE STIE 0 MSIE VSSIE SSIE 0 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 Figure 114. Standard portion (bits 15:0) of mie. Bits SGEIP, VSEIP, VSTIP, and VSSIP in mip are aliases for the same bits in hypervisor CSR hip, while SGEIE, VSEIE, VSTIE, and VSSIE in mie are aliases for the same bits in hie. 21.4.4. Machine Second Trap Value (mtval2) Register The mtval2 register is an MXLEN-bit read/write register formatted as shown in Figure 115. When a trap is taken into M-mode, mtval2 is written with additional exception-specific information, alongside mtval, to assist software in handling the trap. MXLEN-1 0 mtval2 MXLEN Figure 115. Machine second trap value register (mtval2). When a guest-page-fault trap is taken into M-mode, mtval2 is written with either zero or the guest physical address that faulted, shifted right by 2 bits. For other traps, mtval2 is set to zero, but a future standard or extension may redefine mtval2’s setting for other traps. If a guest-page fault is due to an implicit memory access during first-stage (VS-stage) address translation, a guest physical address written to mtval2 is that of the implicit memory access that faulted. Additional information is provided in CSR mtinst to disambiguate such situations. Otherwise, for misaligned loads and stores that cause guest-page faults, a nonzero guest physical address in mtval2 corresponds to the faulting portion of the access as indicated by the virtual address in mtval. For instruction guest-page faults on systems with variable-length instructions, a nonzero 21.4. Machine-Level CSRs | Page 180 The RISC-V Instruction Set Manual: Volume II | © RISC-V International
```

**New:**
```
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 0 LCOFIE SGEIE MEIE VSEIE SEIE 0 MTIE VSTIE STIE 0 MSIE VSSIE SSIE 0 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 Figure 82. Standard portion (bits 15:0) of mie. Bits SGEIP, VSEIP, VSTIP, and VSSIP in mip are aliases for the same bits in hypervisor CSR hip, while SGEIE, VSEIE, VSTIE, and VSSIE in mie are aliases for the same bits in hie. 15.4.4. Machine Second Trap Value (mtval2) Register The mtval2 register is an MXLEN-bit read/write register formatted as shown in Figure 83. When a trap is taken into M-mode, mtval2 is written with additional exception-specific information, alongside mtval, to assist software in handling the trap. MXLEN-1 0 mtval2 MXLEN Figure 83. Machine second trap value register (mtval2). When a guest-page-fault trap is taken into M-mode, mtval2 is written with either zero or the guest physical address that faulted, shifted right by 2 bits. For other traps, mtval2 is set to zero, but a future standard or extension may redefine mtval2’s setting for other traps. If a guest-page fault is due to an implicit memory access during first-stage (VS-stage) address translation, a guest physical address written to mtval2 is that of the implicit memory access that faulted. Additional information is provided in CSR mtinst to disambiguate such situations. Otherwise, for misaligned loads and stores that cause guest-page faults, a nonzero guest physical address in mtval2 corresponds to the faulting portion of the access as indicated by the virtual address in mtval. For instruction guest-page faults on systems with variable-length instructions, a nonzero mtval2 corresponds to the faulting portion of the instruction as indicated by the virtual address in mtval. mtval2 is a WARL register that must be able to hold zero and may be capable of holding only an arbitrary subset of other 2-bit-shifted guest physical addresses, if any. The Ssdbltrap extension (See "Ssdbltrp" Double Trap Extension) requires the implementation of the mtval2 CSR. 15.4.5. Machine Trap Instruction (mtinst) Register The mtinst register is an MXLEN-bit read/write register formatted as shown in Figure 84. When a trap is taken into M-mode, mtinst is written with a value that, if nonzero, provides information about the instruction that trapped, to assist software in handling the trap. The values that may be written to mtinst on a trap are documented in Section 15.6.3. MXLEN-1 0 mtinst MXLEN Figure 84. Machine trap instruction (mtinst) register. mtinst is a WARL register that need only be able to hold the values that the implementation may automatically write to it on a trap. 15.4. Machine-Level CSRs | Page 172 The RISC-V Instruction Set Manual, Volume II | © RISC-V International
```

**Detail:** Changed '21.4.2. machine interrupt delegation (mideleg) register when the hypervisor extension is implemented, bits 10, 6, and 2 of mideleg (corresponding to the standard vs-level interrupts) are each read-only one. furthermore, if any guest external interrupts are implemented (geilen is nonzero), bit 12 of mideleg (corresponding to supervisor-level guest external interrupts) is also read-only one. vs-level interrupts and guest external interrupts are always delegated past m-mode to hs-mode. for bits of mideleg that are zero, the corresponding bits in hideleg, hip, and hie are read-only zeros. 21.4.3. machine interrupt (mip and mie) registers the hypervisor extension gives registers mip and mie additional active bits for the hypervisor-added interrupts. figure 113 and figure 114 show the standard portions (bits 15:0) of registers mip and mie when the hypervisor extension is implemented.' to ''

</details>

<details>
<summary>🔴 **CHG-0537** Page modified `Page 188` (p. 180) — 57% similar</summary>

**Page:** 188 → 180

**Old:**
```
mtval2 corresponds to the faulting portion of the instruction as indicated by the virtual address in mtval. mtval2 is a WARL register that must be able to hold zero and may be capable of holding only an arbitrary subset of other 2-bit-shifted guest physical addresses, if any. The Ssdbltrap extension (See Chapter 23) requires the implementation of the mtval2 CSR. 21.4.5. Machine Trap Instruction (mtinst) Register The mtinst register is an MXLEN-bit read/write register formatted as shown in Figure 116. When a trap is taken into M-mode, mtinst is written with a value that, if nonzero, provides information about the instruction that trapped, to assist software in handling the trap. The values that may be written to mtinst on a trap are documented in Section 21.6.3. MXLEN-1 0 mtinst MXLEN Figure 116. Machine trap instruction (mtinst) register. mtinst is a WARL register that need only be able to hold the values that the implementation may automatically write to it on a trap. 21.5. Two-Stage Address Translation Whenever the current virtualization mode V is 1, two-stage address translation and protection is in effect. For any virtual memory access, the original virtual address is converted in the first stage by VS-level address translation, as controlled by the vsatp register, into a guest physical address. The guest physical address is then converted in the second stage by guest physical address translation, as controlled by the hgatp register, into a supervisor physical address. The two stages are known also as VS-stage and G-stage translation. Although there is no option to disable two-stage address translation when V=1, either stage of translation can be effectively disabled by zeroing the corresponding vsatp or hgatp register. The vsstatus field MXR, which makes execute-only pages readable by explicit loads, only overrides VS-stage page protection. Setting MXR at VS-level does not override guest-physical page protections. Setting MXR at HS-level, however, overrides both VS-stage and G-stage execute-only permissions. When V=1, memory accesses that would normally bypass address translation are subject to G-stage address translation alone. This includes memory accesses made in support of VS-stage address translation, such as reads and writes of VS-level page tables. Machine-level physical memory protection applies to supervisor physical addresses and is in effect regardless of virtualization mode. 21.5.1. Guest Physical Address Translation The mapping of guest physical addresses to supervisor physical addresses is controlled by CSR hgatp (Section 21.2.10). When the address translation scheme selected by the MODE field of hgatp is Bare, guest physical addresses are equal to supervisor physical addresses without modification, and no memory protection 21.5. Two-Stage Address Translation | Page 181 The RISC-V Instruction Set Manual: Volume II | © RISC-V International
```

**New:**
```
15.5. Two-Stage Address Translation Whenever the current virtualization mode V is 1, two-stage address translation and protection is in effect. For any virtual memory access, the original virtual address is converted in the first stage by VS-level address translation, as controlled by the vsatp register, into a guest physical address. The guest physical address is then converted in the second stage by guest physical address translation, as controlled by the hgatp register, into a supervisor physical address. The two stages are known also as VS-stage and G-stage translation. Although there is no option to disable two-stage address translation when V=1, either stage of translation can be effectively disabled by zeroing the corresponding vsatp or hgatp register. The vsstatus field MXR, which makes execute-only pages readable by explicit loads, only overrides VS-stage page protection. Setting MXR at VS-level does not override guest-physical page protections. Setting MXR at HS-level, however, overrides both VS-stage and G-stage execute-only permissions. When V=1, memory accesses that would normally bypass address translation are subject to G-stage address translation alone. This includes memory accesses made in support of VS-stage address translation, such as reads and writes of VS-level page tables. Machine-level physical memory protection applies to supervisor physical addresses and is in effect regardless of virtualization mode. 15.5.1. Guest Physical Address Translation The mapping of guest physical addresses to supervisor physical addresses is controlled by CSR hgatp (Section 15.2.10). When the address translation scheme selected by the MODE field of hgatp is Bare, guest physical addresses are equal to supervisor physical addresses without modification, and no memory protection applies in the trivial translation of guest physical addresses to supervisor physical addresses. When hgatp.MODE specifies a translation scheme of Sv32x4, Sv39x4, Sv48x4, or Sv57x4, G-stage address translation is a variation on the usual page-based virtual address translation scheme of Sv32, Sv39, Sv48, or Sv57, respectively. In each case, the size of the incoming address is widened by 2 bits (to 34, 41, 50, or 59 bits). To accommodate the 2 extra bits, the root page table (only) is expanded by a factor of four to be 16 KiB instead of the usual 4 KiB. Matching its larger size, the root page table also must be aligned to a 16 KiB boundary instead of the usual 4 KiB page boundary. Except as noted, all other aspects of Sv32, Sv39, Sv48, or Sv57 are adopted unchanged for G-stage translation. Non-root page tables and all page table entries (PTEs) have the same formats as documented in Sv32: Page-Based 32-bit Virtual-Memory Systems, Sv39: Page-Based 39-bit Virtual-Memory Systems, Sv48: Page-Based 48-bit Virtual-Memory Systems, and "Sv57: Page-Based 57-bit Virtual-Memory System. For Sv32x4, an incoming guest physical address is partitioned into a virtual page number (VPN) and page offset as shown in Figure 85. This partitioning is identical to that for an Sv32 virtual address as depicted in Sv32 virtual address, except with 2 more bits at the high end in VPN[1]. (Note that the fields of a partitioned guest physical address also correspond one-for-one with the structure that Sv32 assigns to a physical address, depicted in Sv32 virtual address.) 33 22 21 12 11 0 VPN[1] VPN[0] page offset 12 10 12 Figure 85. Sv32x4 virtual address (guest physical address). For Sv39x4, an incoming guest physical address is partitioned as shown in Figure 86. This partitioning is identical to that for an Sv39 virtual address as depicted in "Sv39 virtual address, except with 2 more bits at 15.5. Two-Stage Address Translation | Page 173 The RISC-V Instruction Set Manual, Volume II | © RISC-V International
```

**Detail:** Changed 'mtval2 corresponds to the faulting portion of the instruction as indicated by the virtual address in mtval. mtval2 is a warl register that must be able to hold zero and may be capable of holding only an arbitrary subset of other 2-bit-shifted guest physical addresses, if any. the ssdbltrap extension (see chapter 23) requires the implementation of the mtval2 csr. 21.4.5. machine trap instruction (mtinst) register the mtinst register is an mxlen-bit read/write register formatted as shown in figure 116. when a trap is taken into m-mode, mtinst is written with a value that, if nonzero, provides information about the instruction that trapped, to assist software in handling the trap. the values that may be written to mtinst on a trap are documented in section 21.6.3. mxlen-1 0 mtinst mxlen figure 116. machine trap instruction (mtinst) register. mtinst is a warl register that need only be able to hold the values that the implementation may automatically write to it on a trap. 21.5.' to '15.5.'

</details>

<details>
<summary>🔴 **CHG-0205** Requirement modified `Similarly, if henvcfg.PBMTE/ADUE need be world-switched, they should be switched after zeroing vsatp but before writi...` (p. 183) — 98% similar</summary>

**Page:** 192 → 183

**Preview:** Similarly, if henvcfg.PBMTE/ADUE need be world-switched, they should be switched after zeroing vsatp but before writi...

**Old:**
```
Similarly, if henvcfg.PBMTE need be world-switched, it should be switched after zeroing vsatp but before writing the new vsatp value, obviating the need to execute an HFENCE.VVMA instruction.
```

**New:**
```
Similarly, if henvcfg.PBMTE/ADUE need be world-switched, they should be switched after zeroing vsatp but before writing the new vsatp value, obviating the need to execute an HFENCE.VVMA instruction.
```

**Detail:** Changed 'henvcfg.pbmte' to 'henvcfg.pbmte/adue'

</details>

<details>
<summary>🔴 **CHG-0242** Requirement removed `HSV.D are not valid for RV32, of course.` (p. 183) — 0% similar</summary>

**Page:** 183 → ?

**Old:**
```
HSV.D are not valid for RV32, of course.
```

**Detail:** Removed requirement

</details>

<details>
<summary>🔴 **CHG-0271** Requirement added `Specifically, these cases are: ⚫PMLEN=7 and hgatp.MODE=sv57x4 ⚫PMLEN=16 and hgatp.MODE=sv57x4 ⚫PMLEN=16 and hgatp.MOD...` (p. 183) — 0% similar</summary>

**Page:** ? → 183

**Preview:** Specifically, these cases are: ⚫PMLEN=7 and hgatp.MODE=sv57x4 ⚫PMLEN=16 and hgatp.MODE=sv57x4 ⚫PMLEN=16 and hgatp.MOD...

**New:**
```
Specifically, these cases are: ⚫PMLEN=7 and hgatp.MODE=sv57x4 ⚫PMLEN=16 and hgatp.MODE=sv57x4 ⚫PMLEN=16 and hgatp.MODE=sv48x4 Implementation of an address-specific HFENCE.GVMA should either ignore the address argument, or should ignore the top masked GPA bits of entries when comparing for an address match.
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0538** Page modified `Page 191` (p. 183) — 37% similar</summary>

**Page:** 191 → 183

**Old:**
```
21.6.3. When an instruction fetch or a misaligned memory access straddles a page boundary, two different address translations are involved. When a guest-page fault occurs in such a circumstance, the faulting virtual address written to mtval/stval is the same as would be required for a regular page fault. Thus, the faulting virtual address may be a page-boundary address that is higher than the instruction’s original virtual address, if the byte at that page boundary is among the accessed bytes. When a guest-page fault is not due to an implicit memory access for VS-stage address translation, a nonzero guest physical address written to mtval2/htval shall correspond to the exact virtual address written to mtval/stval. 21.5.3. Memory-Management Fences The behavior of the SFENCE.VMA instruction is affected by the current virtualization mode V. When V=0, the virtual-address argument is an HS-level virtual address, and the ASID argument is an HS-level ASID. The instruction orders stores only to HS-level address-translation structures with subsequent HS-level address translations. When V=1, the virtual-address argument to SFENCE.VMA is a guest virtual address within the current virtual machine, and the ASID argument is a VS-level ASID within the current virtual machine. The current virtual machine is identified by the VMID field of CSR hgatp, and the effective ASID can be considered to be the combination of this VMID with the VS-level ASID. The SFENCE.VMA instruction orders stores only to the VS-level address-translation structures with subsequent VS-stage address translations for the same virtual machine, i.e., only when hgatp.VMID is the same as when the SFENCE.VMA executed. Hypervisor instructions HFENCE.VVMA and HFENCE.GVMA provide additional memory-management fences to complement SFENCE.VMA. These instructions are described in Section 21.3.2. Section 3.7.2 discusses the intersection between physical memory protection (PMP) and page-based address translation. It is noted there that, when PMP settings are modified in a manner that affects either the physical memory that holds page tables or the physical memory to which page tables point, M-mode software must synchronize the PMP settings with the virtual memory system. For HS-level address translation, this is accomplished by executing in M-mode an SFENCE.VMA instruction with rs1=x0 and rs2=x0, after the PMP CSRs are written. Synchronization with G-stage and VS-stage data structures is also needed. Executing an HFENCE.GVMA instruction with rs1=x0 and rs2=x0 suffices to flush all G-stage or VS-stage address-translation cache entries that have cached PMP settings corresponding to the final translated supervisor physical address. An HFENCE.VVMA instruction is not required. Similarly, if the setting of the PBMTE bit in menvcfg is changed, an HFENCE.GVMA instruction with rs1 =x0 and rs2=x0 suffices to synchronize with respect to the altered interpretation of G-stage and VS-stage PTEs' PBMT fields. By contrast, if the PBMTE bit in henvcfg is changed, executing an HFENCE.VVMA with rs1=x0 and rs2=x0 suffices to synchronize with respect to the altered interpretation of VS-stage PTEs' PBMT fields for the currently active VMID.  No mechanism is provided to atomically change vsatp and hgatp together. Hence, to prevent speculative execution causing one guest’s VS-stage translations to be cached under another guest’s VMID, world-switch code should zero vsatp, then swap 21.5. Two-Stage Address Translation | Page 184 The RISC-V Instruction Set Manual: Volume II | © RISC-V International
```

**New:**
```
For HS-level address translation, this is accomplished by executing in M-mode an SFENCE.VMA instruction with rs1=x0 and rs2=x0, after the PMP CSRs are written. Synchronization with G-stage and VS-stage data structures is also needed. Executing an HFENCE.GVMA instruction with rs1=x0 and rs2=x0 suffices to flush all G-stage or VS-stage address-translation cache entries that have cached PMP settings corresponding to the final translated supervisor physical address. An HFENCE.VVMA instruction is not required. Similarly, if the setting of the PBMTE or ADUE bits in menvcfg are changed, an HFENCE.GVMA instruction with rs1=x0 and rs2=x0 suffices to synchronize with respect to the altered interpretation of G-stage and VS-stage PTEs' PBMT and A/D bit fields, respectively. By contrast, if the PBMTE or ADUE bits in henvcfg are changed, executing an HFENCE.VVMA with rs1=x0 and rs2=x0 suffices to synchronize with respect to the altered interpretation of VS-stage PTEs' PBMT and A/D bit fields for the currently active VMID.  No mechanism is provided to atomically change vsatp and hgatp together. Hence, to prevent speculative execution causing one guest’s VS-stage translations to be cached under another guest’s VMID, world-switch code should zero vsatp, then swap hgatp, then finally write the new vsatp value. Similarly, if henvcfg.PBMTE/ADUE need be world-switched, they should be switched after zeroing vsatp but before writing the new vsatp value, obviating the need to execute an HFENCE.VVMA instruction. 15.5.4. Interaction with Pointer Masking Guest physical addresses (GPAs) are 2 bits wider than the corresponding virtual address translation modes, resulting in additional address translation schemes Sv32x4, Sv39x4, Sv48x4, and Sv57x4 for translating guest physical addresses to supervisor physical addresses. When running with virtualization in VS/VU mode with vsatp.MODE = Bare, this means that those two bits may be subject to pointer masking, depending on hgatp.MODE and senvcfg.PMM/henvcfg.PMM (for VU/VS mode). If vsatp.MODE != BARE, this issue does not apply.  An implementation could mask those two bits on the TLB access path, but this can have a significant timing impact. Alternatively, an implementation may choose to "waste" TLB capacity by having up to 4 duplicate entries for each page. In this case, the pointer masking operation can be applied on the TLB refill path, where it is unlikely to affect timing. To support this approach, some TLB entries need to be flushed when PMLEN changes in a way that may affect these duplicate entries. To support implementations where (XLEN-PMLEN) can be less than the GPA width supported by hgatp.MODE, hypervisors should execute an HFENCE.GVMA with rs1=x0 if the henvcfg.PMM is changed from or to a value where (XLEN-PMLEN) is less than GPA width supported by the hgatp translation mode of that guest. Specifically, these cases are: ⚫PMLEN=7 and hgatp.MODE=sv57x4 ⚫PMLEN=16 and hgatp.MODE=sv57x4 ⚫PMLEN=16 and hgatp.MODE=sv48x4 Implementation of an address-specific HFENCE.GVMA should either ignore the address argument, or should ignore the top masked GPA bits of entries when comparing for an address match. 15.5. Two-Stage Address Translation | Page 176 The RISC-V Instruction Set Manual, Volume II | © RISC-V International
```

**Detail:** Changed '21.6.3. when an instruction fetch or a misaligned memory access straddles a page boundary, two different address translations are involved. when a guest-page fault occurs in such a circumstance, the faulting virtual address written to mtval/stval is the same as would be required for a regular page fault. thus, the faulting virtual address may be a page-boundary address that is higher than the instruction’s original virtual address, if the byte at that page boundary is among the accessed bytes. when a guest-page fault is not due to an implicit memory access for vs-stage address translation, a nonzero guest physical address written to mtval2/htval shall correspond to the exact virtual address written to mtval/stval. 21.5.3. memory-management fences the behavior of the sfence.vma instruction is affected by the current virtualization mode v. when v=0, the virtual-address argument is an hs-level virtual address, and the asid argument is an hs-level asid. the instruction orders stores only to hs-level address-translation structures with subsequent hs-level address translations. when v=1, the virtual-address argument to sfence.vma is a guest virtual address within the current virtual machine, and the asid argument is a vs-level asid within the current virtual machine. the current virtual machine is identified by the vmid field of csr hgatp, and the effective asid can be considered to be the combination of this vmid with the vs-level asid. the sfence.vma instruction orders stores only to the vs-level address-translation structures with subsequent vs-stage address translations for the same virtual machine, i.e., only when hgatp.vmid is the same as when the sfence.vma executed. hypervisor instructions hfence.vvma and hfence.gvma provide additional memory-management fences to complement sfence.vma. these instructions are described in section 21.3.2. section 3.7.2 discusses the intersection between physical memory protection (pmp) and page-based address translation. it is noted there that, when pmp settings are modified in a manner that affects either the physical memory that holds page tables or the physical memory to which page tables point, m-mode software must synchronize the pmp settings with the virtual memory system.' to ''

</details>

<details>
<summary>🔴 **CHG-0243** Requirement removed `the VMID) must be executed to order subsequent guest translations with the MODE change—even if the old MODE or new MO...` (p. 185) — 0% similar</summary>

**Page:** 185 → ?

**Preview:** the VMID) must be executed to order subsequent guest translations with the MODE change—even if the old MODE or new MO...

**Old:**
```
the VMID) must be executed to order subsequent guest translations with the MODE change—even if the old MODE or new MODE is Bare.
```

**Detail:** Removed requirement

</details>

<details>
<summary>🔴 **CHG-0272** Requirement added `On a synchronous exception, if a nonzero value is written, one of the following shall be true about the value: ⚫Bit 0...` (p. 188) — 0% similar</summary>

**Page:** ? → 188

**Preview:** On a synchronous exception, if a nonzero value is written, one of the following shall be true about the value: ⚫Bit 0...

**New:**
```
On a synchronous exception, if a nonzero value is written, one of the following shall be true about the value: ⚫Bit 0 is 1, and replacing bit 1 with 1 makes the value into a valid encoding of a standard instruction.
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0213** Requirement modified ` If the conditions that necessitate a pseudoinstruction value can ever occur for M-mode, then mtinst cannot be entir...` (p. 192) — 93% similar</summary>

**Page:** 200 → 192

**Preview:**  If the conditions that necessitate a pseudoinstruction value can ever occur for M-mode, then mtinst cannot be entir...

**Old:**
```
The fact that such a page  If the conditions that necessitate a pseudoinstruction value can ever occur for M-mode, then mtinst cannot be entirely read-only zero; and likewise for HS-mode and htinst.
```

**New:**
```
 If the conditions that necessitate a pseudoinstruction value can ever occur for M-mode, then mtinst cannot be entirely read-only zero; and likewise for HS-mode and htinst.
```

**Detail:** Changed 'the fact that such a page' to ''

</details>

<details>
<summary>🔴 **CHG-0273** Requirement added `The fact that such a page table update must actually be atomic, not just a simple write, is ignored for the pseudoins...` (p. 192) — 0% similar</summary>

**Page:** ? → 192

**Preview:** The fact that such a page table update must actually be atomic, not just a simple write, is ignored for the pseudoins...

**New:**
```
The fact that such a page table update must actually be atomic, not just a simple write, is ignored for the pseudoinstruction.
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0244** Requirement removed `On a synchronous exception, if a nonzero value is written, one of the following shall be true about the value: 21.6.` (p. 196) — 0% similar</summary>

**Page:** 196 → ?

**Old:**
```
On a synchronous exception, if a nonzero value is written, one of the following shall be true about the value: 21.6.
```

**Detail:** Removed requirement

</details>

<details>
<summary>🔴 **CHG-0539** Page modified `Page 212` (p. 204) — 77% similar</summary>

**Page:** 212 → 204

**Old:**
```
24.2.4. Determining the Value of PMLEN From an implementation perspective, ignoring bits is deeply connected to the maximum virtual and physical address space supported by the processor (e.g., Bare, Sv48, Sv57). In particular, applying the above transformation is cheap if it covers only bits that are not used by any supported address translation mode (as it is equivalent to switching off validity checks). Masking NVBITS beyond those bits is more expensive as it requires ignoring them in the TLB tag, and even more expensive if the masked bits extend into the VBITS portion of the address (as it requires performing the actual sign extension). Similarly, when running in Bare or M mode, it is common for implementations to not use a particular number of bits at the top of the physical address range and fix them to zero. Applying the ignore transformation to those bits is cheap as well, since it will result in a valid physical address with all the upper bits fixed to 0. The current standard only supports PMLEN=XLEN-48 (i.e., PMLEN=16 in RV64) and PMLEN=XLEN-57 (i.e., PMLEN=7 in RV64). A setting has been reserved to potentially support other values of PMLEN in future standards. In such future standards, different supported values of PMLEN may be defined for each privilege mode (U/VU, S/HS, and M).  Future versions of the pointer masking extension may introduce the ability to freely configure the value of PMLEN. The current extension does not define the behavior if PMLEN was different from the values defined above. In particular, there is no guarantee that a future pointer masking extension would define the ignore operation in the same way for those values of PMLEN. 24.2.5. Pointer Masking and Privilege Modes Pointer masking is controlled separately for different privilege modes. The subset of supported privilege modes is determined by the set of supported pointer masking extensions. Different privilege modes may have different pointer masking settings active simultaneously and the hardware will automatically apply the pointer masking settings of the currently active privilege mode. A privilege mode’s pointer masking setting is configured by bits in configuration registers of the next-higher privilege mode. Note that the pointer masking setting that is applied only depends on the active privilege mode, not on the address that is being masked. Some operating systems (e.g., Linux) may use certain bits in the address to disambiguate between different types of addresses (e.g., kernel and user-mode addresses). Pointer masking does not take these semantics into account and is purely an arithmetic operation on the address it is given.  Linux places kernel addresses in the upper half of the address space and user addresses in the lower half of the address space. As such, the MSB is often used to identify the type of a particular address. With pointer masking enabled, this role is now played by bit XLEN-PMLEN-1 and code that checks whether a pointer is a kernel or a user address needs to inspect this bit instead. For backward compatibility, it may be desirable that the MSB still indicates whether an address is a user or a kernel address. An operating system’s ABI may mandate this, but it does not affect the pointer masking mechanism itself. For example, the Linux ABI may choose to mandate that the MSB is not used for tagging and replicates bit XLEN-PMLEN-1 bit (note that for such a mechanism to be secure, the kernel needs to check the MSB of any user mode-supplied address and ensure that this invariant holds before using it; alternatively, it can apply the transformation from Listing 1 or 2 to ensure that the MSB is set to the correct value). 24.2. Background | Page 205 The RISC-V Instruction Set Manual: Volume II | © RISC-V International
```

**New:**
```
The current standard only supports PMLEN=XLEN-48 (i.e., PMLEN=16 in RV64) and PMLEN=XLEN-57 (i.e., PMLEN=7 in RV64). A setting has been reserved to potentially support other values of PMLEN in future standards. In such future standards, different supported values of PMLEN may be defined for each privilege mode (U/VU, S/HS, and M).  Future versions of the pointer masking extension may introduce the ability to freely configure the value of PMLEN. The current extension does not define the behavior if PMLEN was different from the values defined above. In particular, there is no guarantee that a future pointer masking extension would define the ignore operation in the same way for those values of PMLEN. 18.2.5. Pointer Masking and Privilege Modes Pointer masking is controlled separately for different privilege modes. The subset of supported privilege modes is determined by the set of supported pointer masking extensions. Different privilege modes may have different pointer masking settings active simultaneously and the hardware will automatically apply the pointer masking settings of the currently active privilege mode. A privilege mode’s pointer masking setting is configured by bits in configuration registers of the next-higher privilege mode. Note that the pointer masking setting that is applied only depends on the active privilege mode, not on the address that is being masked. Some operating systems (e.g., Linux) may use certain bits in the address to disambiguate between different types of addresses (e.g., kernel and user-mode addresses). Pointer masking does not take these semantics into account and is purely an arithmetic operation on the address it is given.  Linux places kernel addresses in the upper half of the address space and user addresses in the lower half of the address space. As such, the MSB is often used to identify the type of a particular address. With pointer masking enabled, this role is now played by bit XLEN-PMLEN-1 and code that checks whether a pointer is a kernel or a user address needs to inspect this bit instead. For backward compatibility, it may be desirable that the MSB still indicates whether an address is a user or a kernel address. An operating system’s ABI may mandate this, but it does not affect the pointer masking mechanism itself. For example, the Linux ABI may choose to mandate that the MSB is not used for tagging and replicates bit XLEN-PMLEN-1 bit (note that for such a mechanism to be secure, the kernel needs to check the MSB of any user mode-supplied address and ensure that this invariant holds before using it; alternatively, it can apply the transformation from Listing 1 or 2 to ensure that the MSB is set to the correct value). 18.2.6. Memory Accesses Subject to Pointer Masking Pointer masking applies to all explicit memory accesses. Currently, in the Base and Privileged ISAs, these are: ⚫Base Instruction Set: LB, LH, LW, LBU, LHU, LWU, LD, SB, SH, SW, SD. ⚫Atomics: All instructions in RV32A and RV64A. ⚫Floating Point: FLW, FLD, FLQ, FSW, FSD, FSQ. ⚫Compressed: All instructions mapping to any of the above, and C.LWSP, C.LDSP, C.FLWSP, C.FLDSP, C.SWSP, C.SDSP, C.FSWSP, C.FSDSP. ⚫Hypervisor Extension: HLV.*, HSV.* (in some cases; see Hypervisor Status (hstatus) Register). ⚫Cache Management Operations: All instructions in Zicbom, Zicbop and Zicboz. ⚫Vector Extension: All vector load and store instructions in the ratified RVV 1.0 spec. 18.2. Background | Page 197 The RISC-V Instruction Set Manual, Volume II | © RISC-V International
```

**Detail:** Changed '24.2.4. determining the value of pmlen from an implementation perspective, ignoring bits is deeply connected to the maximum virtual and physical address space supported by the processor (e.g., bare, sv48, sv57). in particular, applying the above transformation is cheap if it covers only bits that are not used by any supported address translation mode (as it is equivalent to switching off validity checks). masking nvbits beyond those bits is more expensive as it requires ignoring them in the tlb tag, and even more expensive if the masked bits extend into the vbits portion of the address (as it requires performing the actual sign extension). similarly, when running in bare or m mode, it is common for implementations to not use a particular number of bits at the top of the physical address range and fix them to zero. applying the ignore transformation to those bits is cheap as well, since it will result in a valid physical address with all the upper bits fixed to 0.' to ''

</details>

<details>
<summary>🔴 **CHG-0245** Requirement removed `If satp.MODE (or vsatp.MODE when V=1) is set to Bare and the effective privilege mode is below M, shadow stack memory...` (p. 205) — 0% similar</summary>

**Page:** 205 → ?

**Preview:** If satp.MODE (or vsatp.MODE when V=1) is set to Bare and the effective privilege mode is below M, shadow stack memory...

**Old:**
```
If satp.MODE (or vsatp.MODE when V=1) is set to Bare and the effective privilege mode is below M, shadow stack memory accesses are prohibited, and shadow stack instructions will raise a store/AMO access-fault exception.
```

**Detail:** Removed requirement

</details>

<details>
<summary>🔴 **CHG-0274** Requirement added ` For adding Shared-region rules with executable privileges to share code segments between M-mode and S/U-mode, msecc...` (p. 212) — 0% similar</summary>

**Page:** ? → 212

**Preview:**  For adding Shared-region rules with executable privileges to share code segments between M-mode and S/U-mode, msecc...

**New:**
```
 For adding Shared-region rules with executable privileges to share code segments between M-mode and S/U-mode, mseccfg.RLB needs to be implemented, or else such rules can only be added together with mseccfg.MML being set on PMP Reset.
```

**Detail:** Added requirement

</details>

<details>
<summary>🔴 **CHG-0246** Requirement removed `Implementation of an address-specific HFENCE.GVMA should either ignore the address argument, or should ignore the top...` (p. 217) — 0% similar</summary>

**Page:** 217 → ?

**Preview:** Implementation of an address-specific HFENCE.GVMA should either ignore the address argument, or should ignore the top...

**Old:**
```
Implementation of an address-specific HFENCE.GVMA should either ignore the address argument, or should ignore the top masked GPA bits of entries when comparing for an address match.
```

**Detail:** Removed requirement

</details>

### Numeric changes (17)

<details>
<summary>🔴 **CHG-0210** Requirement modified `This register must be readable in any implementation, but a value of 0 can be returned to indicate that the field is ...` (p. 37) — 95% similar</summary>

**Page:** 35 → 37

**Preview:** This register must be readable in any implementation, but a value of 0 can be returned to indicate that the field is ...

**Old:**
```
This register must be readable in any implementation, but a value of 0 can be returned to indicate that the field is not implemented.
```

**New:**
```
This register must be readable in any implementation, but a value of 0 can be returned to indicate that the field is not 3.1.
```

**Detail:** Changed 'implemented.' to '3.1.'

</details>

<details>
<summary>🔴 **CHG-0221** Requirement modified `Hart ID (mhartid) register partial$bytefield/mhartid.edn  In certain cases, we must ensure exactly one hart runs som...` (p. 38) — 85% similar</summary>

**Page:** 36 → 38

**Preview:** Hart ID (mhartid) register partial$bytefield/mhartid.edn  In certain cases, we must ensure exactly one hart runs som...

**Old:**
```
MXLEN-1 0 Hart ID MXLEN  In certain cases, we must ensure exactly one hart runs some code (e.g., at reset), and so require one hart to have a known hart ID of zero.
```

**New:**
```
Hart ID (mhartid) register partial$bytefield/mhartid.edn  In certain cases, we must ensure exactly one hart runs some code (e.g., at reset), and so require one hart to have a known hart ID of zero.
```

**Detail:** Changed 'mxlen-1 0' to ''

</details>

<details>
<summary>🔴 **CHG-0219** Requirement modified `partial$bytefield/mconfigptrreg.edn The pointer alignment in bits must be no smaller than MXLEN: i.e., if MXLEN is 8×...` (p. 60) — 87% similar</summary>

**Page:** 59 → 60

**Preview:** partial$bytefield/mconfigptrreg.edn The pointer alignment in bits must be no smaller than MXLEN: i.e., if MXLEN is 8×...

**Old:**
```
MXLEN-1 0 mconfigptr MXLEN The pointer alignment in bits must be no smaller than MXLEN: i.e., if MXLEN is , then mconfigptr [-1:0] must be zero.
```

**New:**
```
partial$bytefield/mconfigptrreg.edn The pointer alignment in bits must be no smaller than MXLEN: i.e., if MXLEN is 8×n, then mconfigptr [log2n-1:0] must be zero.
```

**Detail:** Changed 'mxlen-1 0 mconfigptr mxlen' to 'partial$bytefield/mconfigptrreg.edn'

</details>

<details>
<summary>🔴 **CHG-0215** Requirement modified `Implementations are permitted to resume execution for any reason, even if an enabled interrupt has not 3.3.` (p. 68) — 92% similar</summary>

**Page:** 65 → 68

**Old:**
```
Implementations are permitted to resume execution for any reason, even if an enabled interrupt has not become pending.
```

**New:**
```
Implementations are permitted to resume execution for any reason, even if an enabled interrupt has not 3.3.
```

**Detail:** Changed 'become pending.' to '3.3.'

</details>

<details>
<summary>🔴 **CHG-0206** Requirement modified `In general, the PMP grain is 2G+2 bytes and must be the same across all PMP regions.` (p. 79) — 97% similar</summary>

**Page:** 76 → 79

**Old:**
```
In general, the PMP grain is bytes and must be the same across all PMP regions.
```

**New:**
```
In general, the PMP grain is 2G+2 bytes and must be the same across all PMP regions.
```

**Detail:** Changed '' to '2g+2'

</details>

<details>
<summary>🔴 **CHG-0212** Requirement modified `Undefined bits must be implemented as read-only 0, unless a custom extension is implemented and enabled (see Custom E...` (p. 108) — 93% similar</summary>

**Page:** 110 → 108

**Preview:** Undefined bits must be implemented as read-only 0, unless a custom extension is implemented and enabled (see Custom E...

**Old:**
```
Undefined bits must be implemented as read-only 0, unless a custom extension is implemented and enabled (see Section 11.6).
```

**New:**
```
Undefined bits must be implemented as read-only 0, unless a custom extension is implemented and enabled (see Custom Extensions).
```

**Detail:** Changed 'section 11.6).' to 'custom extensions).'

</details>

<details>
<summary>🔴 **CHG-0202** Requirement modified `If the feature to return the faulting instruction bits is implemented, stval must also be able to hold all values les...` (p. 128) — 99% similar</summary>

**Page:** 132 → 128

**Preview:** If the feature to return the faulting instruction bits is implemented, stval must also be able to hold all values les...

**Old:**
```
If the feature to return the faulting instruction bits is implemented, stval must also be able to hold all values less than , where is the smaller of SXLEN and ILEN.
```

**New:**
```
If the feature to return the faulting instruction bits is implemented, stval must also be able to hold all values less than 2N, where N is the smaller of SXLEN and ILEN.
```

**Detail:** Changed ',' to '2n,'

</details>

<details>
<summary>🔴 **CHG-0218** Requirement modified `⚫If software modifies a leaf PTE, it should execute SFENCE.VMA with rs1 set to a virtual 12.2.` (p. 135) — 87% similar</summary>

**Page:** 139 → 135

**Old:**
```
⚫If software modifies a leaf PTE, it should execute SFENCE.VMA with rs1 set to a virtual address within the page.
```

**New:**
```
⚫If software modifies a leaf PTE, it should execute SFENCE.VMA with rs1 set to a virtual 12.2.
```

**Detail:** Changed 'address within the page.' to '12.2.'

</details>

<details>
<summary>🔴 **CHG-0223** Requirement modified `A consequence of implementations being permitted to read the translation data structures arbitrarily early and specul...` (p. 141) — 79% similar</summary>

**Page:** 145 → 141

**Preview:** A consequence of implementations being permitted to read the translation data structures arbitrarily early and specul...

**Old:**
```
A consequence of implementations being permitted to read the translation data structures arbitrarily early and speculatively is that at any time, all page table entries 12.3.
```

**New:**
```
A consequence of implementations being permitted to read the translation data structures arbitrarily early and speculatively is that at any time, all page table entries reachable by executing the algorithm may be loaded into the address-translation cache.
```

**Detail:** Changed '12.3.' to 'reachable by executing the algorithm may be loaded into the address-translation cache.'

</details>

<details>
<summary>🔴 **CHG-0222** Requirement modified `Any level of PTE may be a leaf PTE, so in addition to 4 KiB pages, Sv48 supports 2 MiB megapages, 1 GiB gigapages, an...` (p. 144) — 82% similar</summary>

**Page:** 148 → 144

**Preview:** Any level of PTE may be a leaf PTE, so in addition to 4 KiB pages, Sv48 supports 2 MiB megapages, 1 GiB gigapages, an...

**Old:**
```
Any level of PTE may be a leaf PTE, so in addition to pages, Sv48 supports megapages, gigapages, and terapages, each of which must be virtually and physically aligned to a boundary equal to its size.
```

**New:**
```
Any level of PTE may be a leaf PTE, so in addition to 4 KiB pages, Sv48 supports 2 MiB megapages, 1 GiB gigapages, and 512 GiB terapages, each of which must be virtually and physically aligned to a boundary equal to its size.
```

**Detail:** Changed '' to '4 kib'

</details>

<details>
<summary>🔴 **CHG-0204** Requirement modified `If the encoding in pte is reserved according to Table 42, then a page-fault exception must be raised.` (p. 145) — 98% similar</summary>

**Page:** 150 → 145

**Old:**
```
If the encoding in pte is reserved according to Table 36, then a page-fault exception must be raised.
```

**New:**
```
If the encoding in pte is reserved according to Table 42, then a page-fault exception must be raised.
```

**Detail:** Changed '36,' to '42,'

</details>

<details>
<summary>🔴 **CHG-0216** Requirement modified ` Matching VS CSRs exist only for the supervisor CSRs that must be duplicated, which are mainly those that get automa...` (p. 157) — 90% similar</summary>

**Page:** 166 → 157

**Preview:**  Matching VS CSRs exist only for the supervisor CSRs that must be duplicated, which are mainly those that get automa...

**Old:**
```
 Matching VS CSRs exist only for the supervisor CSRs that must be duplicated, which are mainly those that get automatically written by traps or that impact instruction execution immediately after trap entry and/or right before SRET, when software alone 21.2.
```

**New:**
```
 Matching VS CSRs exist only for the supervisor CSRs that must be duplicated, which are mainly those that get automatically written by traps or that impact instruction execution immediately after trap entry and/or right before SRET, when software alone is unable to swap a CSR at exactly the right moment.
```

**Detail:** Changed '21.2.' to 'is unable to swap a csr at exactly the right moment.'

</details>

<details>
<summary>🔴 **CHG-0200** Requirement modified `As explained in Section 15.5.1, for the paged virtual-memory schemes (Sv32x4, Sv39x4, Sv48x4, and Sv57x4), the root p...` (p. 169) — 99% similar</summary>

**Page:** 177 → 169

**Preview:** As explained in Section 15.5.1, for the paged virtual-memory schemes (Sv32x4, Sv39x4, Sv48x4, and Sv57x4), the root p...

**Old:**
```
As explained in Section 21.5.1, for the paged virtual-memory schemes (Sv32x4, Sv39x4, Sv48x4, and Sv57x4), the root page table is 16 KiB and must be aligned to a 16-KiB boundary.
```

**New:**
```
As explained in Section 15.5.1, for the paged virtual-memory schemes (Sv32x4, Sv39x4, Sv48x4, and Sv57x4), the root page table is 16 KiB and must be aligned to a 16-KiB boundary.
```

**Detail:** Changed '21.5.1,' to '15.5.1,'

</details>

<details>
<summary>🔴 **CHG-0209** Requirement modified `(The supervisor physical memory attributes are the machine’s physical memory attributes as modified by physical memor...` (p. 174) — 95% similar</summary>

**Page:** 183 → 174

**Preview:** (The supervisor physical memory attributes are the machine’s physical memory attributes as modified by physical memor...

**Old:**
```
(The supervisor physical memory attributes are the machine’s physical memory attributes as modified by physical memory protection, Section 3.7, for supervisor level.)  HLVX cannot override machine-level physical memory protection (PMP), so attempting to read memory that PMP designates as execute-only still results in an access-fault exception.
```

**New:**
```
(The supervisor physical memory attributes are the machine’s physical memory attributes as modified by physical memory protection, Physical Memory Protection, for supervisor level.)  HLVX cannot override machine-level physical memory protection (PMP), so attempting to read memory that PMP designates as execute-only still results in an access-fault exception.
```

**Detail:** Changed 'section 3.7,' to 'physical memory protection,'

</details>

<details>
<summary>🔴 **CHG-0208** Requirement modified `The conversion of an Sv32x4, Sv39x4, Sv48x4, or Sv57x4 guest physical address is accomplished with the same algorithm...` (p. 181) — 95% similar</summary>

**Page:** 190 → 181

**Preview:** The conversion of an Sv32x4, Sv39x4, Sv48x4, or Sv57x4 guest physical address is accomplished with the same algorithm...

**Old:**
```
The conversion of an Sv32x4, Sv39x4, Sv48x4, or Sv57x4 guest physical address is accomplished with the same algorithm used for Sv32, Sv39, Sv48, or Sv57, as presented in Section 12.3.2, except that: ⚫hgatp substitutes for the usual satp; ⚫for the translation to begin, the effective privilege mode must be VS-mode or VU-mode; ⚫when checking the U bit, the current privilege mode is always taken to be U-mode; and ⚫guest-page-fault exceptions are raised instead of regular page-fault exceptions.
```

**New:**
```
The conversion of an Sv32x4, Sv39x4, Sv48x4, or Sv57x4 guest physical address is accomplished with the same algorithm used for Sv32, Sv39, Sv48, or Sv57, as presented in Virtual Address Translation Process, except that: ⚫hgatp substitutes for the usual satp; ⚫for the translation to begin, the effective privilege mode must be VS-mode or VU-mode; ⚫when checking the U bit, the current privilege mode is always taken to be U-mode; and ⚫guest-page-fault exceptions are raised instead of regular page-fault exceptions.
```

**Detail:** Changed 'section 12.3.2,' to 'virtual address translation process,'

</details>

<details>
<summary>🔴 **CHG-0217** Requirement modified `Hence, to prevent speculative execution causing one guest’s VS-stage translations to be cached under another guest’s ...` (p. 183) — 87% similar</summary>

**Page:** 191 → 183

**Preview:** Hence, to prevent speculative execution causing one guest’s VS-stage translations to be cached under another guest’s ...

**Old:**
```
Hence, to prevent speculative execution causing one guest’s VS-stage translations to be cached under another guest’s VMID, world-switch code should zero vsatp, then swap 21.5.
```

**New:**
```
Hence, to prevent speculative execution causing one guest’s VS-stage translations to be cached under another guest’s VMID, world-switch code should zero vsatp, then swap hgatp, then finally write the new vsatp value.
```

**Detail:** Changed '21.5.' to 'hgatp, then finally write the new vsatp value.'

</details>

<details>
<summary>🔴 **CHG-0203** Requirement modified `If both conditions are met, the value written to mtinst or htinst must be taken from Table 56; zero is not allowed.` (p. 191) — 98% similar</summary>

**Page:** 199 → 191

**Old:**
```
If both conditions are met, the value written to mtinst or htinst must be taken from Table 49; zero is not allowed.
```

**New:**
```
If both conditions are met, the value written to mtinst or htinst must be taken from Table 56; zero is not allowed.
```

**Detail:** Changed '49;' to '56;'

</details>

### Requirement strength changes (1)

<details>
<summary>🔴 **CHG-0214** Requirement modified `additionally apply to M-mode accesses, in which case the PMP registers themselves are locked, so that even M-mode sof...` (p. 77) — 92% similar</summary>

**Page:** 74 → 77

**Preview:** additionally apply to M-mode accesses, in which case the PMP registers themselves are locked, so that even M-mode sof...

**Old:**
```
Optionally, PMP checks may additionally apply to M-mode accesses, in which case the PMP registers themselves are locked, so that even M-mode software cannot change them until the hart is reset.
```

**New:**
```
additionally apply to M-mode accesses, in which case the PMP registers themselves are locked, so that even M-mode software cannot change them until the hart is reset.
```

**Detail:** Changed 'optionally, pmp checks may' to ''

</details>

## 🟠 Content Changes

### Modified tables (80)

<details>
<summary>🟠 **CHG-0514** Table added `0 | 1` (p. 9) — 0% similar</summary>

**Page:** ? → 9

**Preview:** 0 | 1

**New:**
```
0 | 1 Module | Version Machine ISA Smstateen Extension Smcsrind/Sscsrind Extension Smepmp Extension Smcntrpmf Extension Smrnmi Extension Smcdeleg Extension Smdbltrp Extension Smctr Extension Supervisor ISA Svade Extension Svnapot Extension Svpbmt Extension Svinval Extension Svadu Extension Svvptc Extension Ssqosid Extension Sstc Extension Sscofpmf Extension Ssdbltrp Extension Ssqosid Extension Hypervisor ISA Shlcofideleg Extension Svvptc Extension Pointer-Masking Extensions Svrsw60t59b Extension | 1.13 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.13 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
```

**Detail:** Added table

</details>

<details>
<summary>🟠 **CHG-0462** Table modified `Row 3: Machine ISA Smstateen Extension Smcsrind/Sscsrind Extension Smepmp Extension Smcntrpmf Extension Smrnmi Extension Smcdeleg Extension Smdbltrp Extension Smctr Extension Supervisor ISA Svade Extension Svnapot Extension Svpbmt Extension Svinval Extension Svadu Extension Svvptc Extension Ssqosid Extension Sstc Extension Sscofpmf Extension Ssdbltrp Extension Ssqosid Extension Hypervisor ISA Shlcofideleg Extension Svvptc Extension Pointer-Masking Extensions | 1.13 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.13 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 | Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified` (p. 10) — 95% similar</summary>

**Page:** 9 → 10

**Preview:** Row 3: Machine ISA Smstateen Extension Smcsrind/Sscsrind Extension Smepmp Extension Smcntrpmf Extension Smrnmi Extension Smcdeleg Extension Smdbltrp Extension Smctr Extension Supervisor ISA Svade Extension Svnapot Extension Svpbmt Extension Svinval Extension Svadu Extension Svvptc Extension Ssqosid Extension Sstc Extension Sscofpmf Extension Ssdbltrp Extension Ssqosid Extension Hypervisor ISA Shlcofideleg Extension Svvptc Extension Pointer-Masking Extensions | 1.13 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.13 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 | Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified Ratified

**Old:**
```
Machine ISA Smstateen Extension Smcsrind/Sscsrind Extension Smepmp Extension Smcntrpmf Extension Smrnmi Extension Smcdeleg Extension Smdbltrp Extension Smctr Supervisor ISA Svade Extension Svnapot Extension Svpbmt Extension Svinval Extension Svadu Extension Svvptc Ssqosid Sstc Extension Sscofpmf Extension Ssdbltrp Extension Ssqosid Extension Hypervisor ISA Shlcofideleg Extension Svvptc Extension Pointer Masking
```

**New:**
```
Machine ISA Smstateen Extension Smcsrind/Sscsrind Extension Smepmp Extension Smcntrpmf Extension Smrnmi Extension Smcdeleg Extension Smdbltrp Extension Smctr Extension Supervisor ISA Svade Extension Svnapot Extension Svpbmt Extension Svinval Extension Svadu Extension Svvptc Extension Ssqosid Extension Sstc Extension Sscofpmf Extension Ssdbltrp Extension Ssqosid Extension Hypervisor ISA Shlcofideleg Extension Svvptc Extension Pointer-Masking Extensions
```

**Detail:** Cell changed (row 3, col 1)

</details>

<details>
<summary>🟠 **CHG-0473** Table modified `Row 29: 10 | 10 | 11XX | 0xAC0 |-0xAFF | Custom rea | d/write |` (p. 21) — 0% similar</summary>

**Page:** 20 → 21

**Preview:** Row 29: 10 | 10 | 11XX | 0xAC0 |-0xAFF | Custom rea | d/write |

**New:**
```
10 | 10 | 11XX | 0xAC0 |-0xAFF | Custom rea | d/write |
```

**Detail:** Row added

</details>

<details>
<summary>🟠 **CHG-0477** Table removed `0 | 1 | 2 | 3` (p. 21) — 0% similar</summary>

**Page:** 21 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 10 | 10 | 11XX | 0xAC0 |-0xAFF | Custom rea | d/write | 11 | 10 | 0XXX | 0xE00 |-0xE7F | Standard re | ad-only | 11 | 10 | 10XX | 0xE80 |-0xEBF | Standard re | ad-only | 11 | 10 | 11XX | 0xEC0 |-0xEFF | Custom rea | d-only | | | | M | achine-Le | vel CSRs | | 00 | 11 | XXXX | 0x300 |-0x3FF | Standard re | ad/write | 01 | 11 | 0XXX | 0x700 |-0x77F | Standard re | ad/write | 01 | 11 | 100X | 0x780 |-0x79F | Standard re | ad/write | 01 | 11 | 1010 | 0x7A0 |-0x7AF | Standard re | ad/write deb | ug CSRs 01 | 11 | 1011 | 0x7B0 |-0x7BF | Debug-mod | e-only CSRs | 01 | 11 | 11XX | 0x7C0 |-0x7FF | Custom rea | d/write | 10 | 11 | 0XXX | 0xB00 |-0xB7F | Standard re | ad/write | 10 | 11 | 10XX | 0xB80 |-0xBBF | Standard re | ad/write | 10 | 11 | 11XX | 0xBC0 |-0xBFF | Custom rea | d/write | 11 | 11 | 0XXX | 0xF00 |-0xF7F | Standard re | ad-only | 11 | 11 | 10XX | 0xF80 |-0xFBF | Standard re | ad-only | 11 | 11 | 11XX | 0xFC0 |-0xFFF | Custom rea | d-only |
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0515** Table added `0 | 1 | 2 | 3` (p. 22) — 0% similar</summary>

**Page:** ? → 22

**Preview:** 0 | 1 | 2 | 3

**New:**
```
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 10 | 11 | 10XX | 0xB80 |-0xBBF | Standard re | ad/write | 10 | 11 | 11XX | 0xBC0 |-0xBFF | Custom rea | d/write | 11 | 11 | 0XXX | 0xF00 |-0xF7F | Standard re | ad-only | 11 | 11 | 10XX | 0xF80 |-0xFBF | Standard re | ad-only | 11 | 11 | 11XX | 0xFC0 |-0xFFF | Custom rea | d-only |
```

**Detail:** Added table

</details>

<details>
<summary>🟠 **CHG-0452** Table modified `Row 7: | | Unpri | vileged Zicfiss extension CSR` (p. 23) — 98% similar</summary>

**Page:** 22 → 23

**Preview:** Row 7: | | Unpri | vileged Zicfiss extension CSR

**Old:**
```
[row 7, col 3] Unpriv [row 7, col 4] ileged Zicfiss extension CSR [row 11, col 3] Unpri [row 11, col 4] vileged Zcmt Extension CSR
```

**New:**
```
[row 7, col 3] Unpri [row 7, col 4] vileged Zicfiss extension CSR [row 11, col 3] Unpr [row 11, col 4] ivileged Zcmt Extension CSR
```

**Detail:** 4 cells changed

</details>

<details>
<summary>🟠 **CHG-0476** Table modified `Row 17: | | D | ebug/Trace Registers` (p. 24) — 0% similar</summary>

**Page:** 23 → 24

**Preview:** Row 17: | | D | ebug/Trace Registers

**New:**
```
| | D | ebug/Trace Registers
```

**Detail:** Row added

</details>

<details>
<summary>🟠 **CHG-0457** Table modified `Row 19: | | | Virtual Supervisor Indirect` (p. 25) — 0% similar</summary>

**Page:** 24 → 25

**Preview:** Row 19: | | | Virtual Supervisor Indirect

**New:**
```
| | | Virtual Supervisor Indirect
```

**Detail:** Row added

</details>

<details>
<summary>🟠 **CHG-0478** Table removed `0 | 1 | 2 | 3` (p. 26) — 0% similar</summary>

**Page:** 26 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 Number | Privilege | Name | Description 0x30C 0x30D 0x30E 0x30F 0x31C 0x31D 0x31E 0x31F | MRW MRW MRW MRW MRW MRW MRW MRW | mstateen0 mstateen1 mstateen2 mstateen3 mstateen0h mstateen1h mstateen2h mstateen3h | Machine State Enable 0 Register. Machine State Enable 1 Register. Machine State Enable 2 Register. Machine State Enable 3 Register. Upper 32 bits of Machine State Enable 0 Register, RV32 only. Upper 32 bits of Machine State Enable 1 Register, RV32 only. Upper 32 bits of Machine State Enable 2 Register, RV32 only. Upper 32 bits of Machine State Enable 3 Register, RV32 only.
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0516** Table added `0 | 1 | 2 | 3` (p. 26) — 0% similar</summary>

**Page:** ? → 26

**Preview:** 0 | 1 | 2 | 3

**New:**
```
0 | 1 | 2 | 3 Number | Privilege | Name | Description 0x250 0x251 0x252 0x253 0x255 0x256 0x257 | HRW HRW HRW HRW HRW HRW HRW | vsiselect vsireg vsireg2 vsireg3 vsireg4 vsireg5 vsireg6 | Virtual supervisor indirect register select. Virtual supervisor indirect register alias. Virtual supervisor indirect register alias 2. Virtual supervisor indirect register alias 3. Virtual supervisor indirect register alias 4. Virtual supervisor indirect register alias 5. Virtual supervisor indirect register alias 6. | | | Virtual Supervisor Timer Compare 0x24D 0x25D | HRW HRW | vstimecmp vstimecmph | Virtual supervisor timer compare. Upper 32 bits of vstimecmp, RV32 only. | | Virtual Supe | rvisor Control Transfer Records Configuration 0x24E | HRW | vsctrctl | Virtual Supervisor Control Transfer Records Control Register.
```

**Detail:** Added table

</details>

<details>
<summary>🟠 **CHG-0475** Table modified `Row 3: | | M | achine Information Registers` (p. 27) — 39% similar</summary>

**Page:** 25 → 27

**Preview:** Row 3: | | M | achine Information Registers

**Old:**
```
[row 3, col 3] [row 3, col 4] Machine Information Registers [row 9, col 4] Machine Configuration [row 10, col 1] 0x30A 0x31A 0x747 0x757 [row 10, col 2] MRW MRW MRW MRW [row 10, col 3] menvcfg menvcfgh mseccfg mseccfgh [row 10, col 4] Machine environment configuration register. Upper 32 bits of menvcfg, RV32 only. Machine security configuration register. Upper 32 bits of mseccfg, RV32 only. [row 11, col 4] Machine Memory Protection [row 12, col 1] 0x3A0 0x3A1 0x3A2 0x3A3 0x3AE 0x3AF 0x3B0 0x3B1 0x3EF [row 12, col 2] MRW MRW MRW MRW MRW MRW MRW MRW MRW [row 12, col 3] pmpcfg0 pmpcfg1 pmpcfg2 pmpcfg3 ⋯ pmpcfg14 pmpcfg15 pmpaddr0 pmpaddr1 ⋯ pmpaddr63 [row 12, col 4] Physical memory protection configuration. Physical memory protection configuration, RV32 only. Physical memory protection configuration. Physical memory protection configuration, RV32 only. Physical memory protection configuration. Physical memory protection configuration, RV32 only. Physical memory protection address register. Physical memory protection address register. Physical memory protection address register. [row 13, col 4] Machine State Enable Registers
```

**New:**
```
[row 3, col 3] M [row 3, col 4] achine Information Registers [row 9, col 4] Machine Indirect [row 10, col 1] 0x350 0x351 0x352 0x353 0x355 0x356 0x357 [row 10, col 2] MRW MRW MRW MRW MRW MRW MRW [row 10, col 3] miselect mireg mireg2 mireg3 mireg4 mireg5 mireg6 [row 10, col 4] Machine indirect register select. Machine indirect register alias. Machine indirect register alias 2. Machine indirect register alias 3. Machine indirect register alias 4. Machine indirect register alias 5. Machine indirect register alias 6. [row 11, col 4] Machine Configuration [row 12, col 1] 0x30A 0x31A 0x747 0x757 [row 12, col 2] MRW MRW MRW MRW [row 12, col 3] menvcfg menvcfgh mseccfg mseccfgh [row 12, col 4] Machine environment configuration register. Upper 32 bits of menvcfg, RV32 only. Machine security configuration register. Upper 32 bits of mseccfg, RV32 only. [row 13, col 4] Machine Memory Protection
```

**Detail:** 13 cells changed

</details>

<details>
<summary>🟠 **CHG-0479** Table removed `0 | 1 | 2 | 3` (p. 27) — 0% similar</summary>

**Page:** 27 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 Number | Privilege | Name | Description | | Machine Non-| Maskable Interrupt Handling 0x740 0x741 0x742 0x744 | MRW MRW MRW MRW | mnscratch mnepc mncause mnstatus | Resumable NMI scratch register. Resumable NMI program counter. Resumable NMI cause. Resumable NMI status. | | Mach | ine Counter/Timers 0xB00 0xB02 0xB03 0xB04 0xB1F 0xB80 0xB82 0xB83 0xB84 0xB9F | MRW MRW MRW MRW MRW MRW MRW MRW MRW MRW | mcycle minstret mhpmcounter3 mhpmcounter4 ⋮ mhpmcounter31 mcycleh minstreth mhpmcounter3h mhpmcounter4h ⋮ mhpmcounter31h | Machine cycle counter. Machine instructions-retired counter. Machine performance-monitoring counter. Machine performance-monitoring counter. Machine performance-monitoring counter. Upper 32 bits of mcycle, RV32 only. Upper 32 bits of minstret, RV32 only. Upper 32 bits of mhpmcounter3, RV32 only. Upper 32 bits of mhpmcounter4, RV32 only. Upper 32 bits of mhpmcounter31, RV32 only. | | Mac | hine Counter Setup 0x320 0x323 0x324 0x33F 0x723 0x724 0x73F | MRW MRW MRW MRW MRW MRW MRW | mcountinhibit mhpmevent3 mhpmevent4 ⋮ mhpmevent31 mhpmevent3h mhpmevent4h ⋮ mhpmevent31h | Machine counter-inhibit register. Machine performance-monitoring event selector. Machine performance-monitoring event selector. Machine performance-monitoring event selector. Upper 32 bits of mhpmevent3, RV32 only. Upper 32 bits of mhpmevent4, RV32 only. Upper 32 bits of mhpmevent31, RV32 only. | | Debug/Trace Reg | isters (shared with Debug Mode) 0x7A0 0x7A1 0x7A2 0x7A3 0x7A8 | MRW MRW MRW MRW MRW | tselect tdata1 tdata2 tdata3 mcontext | Debug/Trace trigger register select. First Debug/Trace trigger data register. Second Debug/Trace trigger data register. Third Debug/Trace trigger data register. Machine-mode context register. | | Deb | ug Mode Registers 0x7B0 0x7B1 0x7B2 0x7B3 | DRW DRW DRW DRW | dcsr dpc dscratch0 dscratch1 | Debug control and status register. Debug program counter. Debug scratch register 0. Debug scratch register 1.
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0517** Table added `0 | 1 | 2 | 3` (p. 28) — 0% similar</summary>

**Page:** ? → 28

**Preview:** 0 | 1 | 2 | 3

**New:**
```
0 | 1 | 2 | 3 Number | Privilege | Name | Description 0x3A0 0x3A1 0x3A2 0x3A3 0x3AE 0x3AF 0x3B0 0x3B1 0x3EF | MRW MRW MRW MRW MRW MRW MRW MRW MRW | pmpcfg0 pmpcfg1 pmpcfg2 pmpcfg3 ⋯ pmpcfg14 pmpcfg15 pmpaddr0 pmpaddr1 ⋯ pmpaddr63 | Physical memory protection configuration. Physical memory protection configuration, RV32 only. Physical memory protection configuration. Physical memory protection configuration, RV32 only. Physical memory protection configuration. Physical memory protection configuration, RV32 only. Physical memory protection address register. Physical memory protection address register. Physical memory protection address register. | | M | achine State Enable Registers 0x30C 0x30D 0x30E 0x30F 0x31C 0x31D 0x31E 0x31F | MRW MRW MRW MRW MRW MRW MRW MRW | mstateen0 mstateen1 mstateen2 mstateen3 mstateen0h mstateen1h mstateen2h mstateen3h | Machine State Enable 0 Register. Machine State Enable 1 Register. Machine State Enable 2 Register. Machine State Enable 3 Register. Upper 32 bits of Machine State Enable 0 Register, RV32 only. Upper 32 bits of Machine State Enable 1 Register, RV32 only. Upper 32 bits of Machine State Enable 2 Register, RV32 only. Upper 32 bits of Machine State Enable 3 Register, RV32 only. | | Machin | e Non-Maskable Interrupt Handling 0x740 0x741 0x742 0x744 | MRW MRW MRW MRW | mnscratch mnepc mncause mnstatus | Resumable NMI scratch register. Resumable NMI program counter. Resumable NMI cause. Resumable NMI status. | | | Machine Counter/Timers 0xB00 0xB02 0xB03 0xB04 0xB1F 0xB80 0xB82 0xB83 0xB84 0xB9F | MRW MRW MRW MRW MRW MRW MRW MRW MRW MRW | mcycle minstret mhpmcounter3 mhpmcounter4 ⋮ mhpmcounter31 mcycleh minstreth mhpmcounter3h mhpmcounter4h ⋮ mhpmcounter31h | Machine cycle counter. Machine instructions-retired counter. Machine performance-monitoring counter. Machine performance-monitoring counter. Machine performance-monitoring counter. Upper 32 bits of mcycle, RV32 only. Upper 32 bits of minstret, RV32 only. Upper 32 bits of mhpmcounter3, RV32 only. Upper 32 bits of mhpmcounter4, RV32 only. Upper 32 bits of mhpmcounter31, RV32 only. | | | Machine Counter Setup 0x320 0x321 0x322 0x323 0x324 0x33F 0x721 0x722 0x723 0x724 0x73F | MRW MRW MRW MRW MRW MRW MRW MRW MRW MRW MRW | mcountinhibit mcyclecfg minstretcfg mhpmevent3 mhpmevent4 ⋮ mhpmevent31 mcyclecfgh minstretcfgh mhpmevent3h mhpmevent4h ⋮ mhpmevent31h | Machine counter-inhibit register. Machine cycle counter configuration register. Machine instret counter configuration register. Machine performance-monitoring event selector. Machine performance-monitoring event selector. Machine performance-monitoring event selector. Upper 32 bits of mcyclecfg, RV32 only. Upper 32 bits of minstretcfg, RV32 only. Upper 32 bits of mhpmevent3, RV32 only. Upper 32 bits of mhpmevent4, RV32 only. Upper 32 bits of mhpmevent31, RV32 only.
```

**Detail:** Added table

</details>

<details>
<summary>🟠 **CHG-0518** Table added `0 | 1 | 2 | 3` (p. 29) — 0% similar</summary>

**Page:** ? → 29

**Preview:** 0 | 1 | 2 | 3

**New:**
```
0 | 1 | 2 | 3 Number | Privilege | Name | Description | | Machine C | ontrol Transfer Records Configuration 0x34E | MRW | mctrctl | Machine Control Transfer Records Control Register. | | Debug/Tra | ce Registers (shared with Debug Mode) 0x7A0 0x7A1 0x7A2 0x7A3 0x7A8 | MRW MRW MRW MRW MRW | tselect tdata1 tdata2 tdata3 mcontext | Debug/Trace trigger register select. First Debug/Trace trigger data register. Second Debug/Trace trigger data register. Third Debug/Trace trigger data register. Machine-mode context register. | | | Debug Mode Registers 0x7B0 0x7B1 0x7B2 0x7B3 | DRW DRW DRW DRW | dcsr dpc dscratch0 dscratch1 | Debug control and status register. Debug program counter. Debug scratch register 0. Debug scratch register 1.
```

**Detail:** Added table

</details>

<details>
<summary>🟠 **CHG-0519** Table added `0 | 1 | 2 | 3` (p. 30) — 0% similar</summary>

**Page:** ? → 30

**Preview:** 0 | 1 | 2 | 3

**New:**
```
0 | 1 | 2 | 3 | 4 | 5 | 6 miselect | mireg | mireg2 | mireg3 | mireg4 | mireg5 | mireg6 0x30 | iprio0 | none | none | none | none | none … | … | … | … | … | … | … 0x3F | iprio15 | none | none | none | none | none 0x70 | eidelivery | none | none | none | none | none 0x71 | 0 | none | none | none | none | none 0x72 | eithreshold | none | none | none | none | none 0x73 | 0 | none | none | none | none | none … | … | … | … | … | … | … 0x7F | 0 | none | none | none | none | none 0x80 | eip0 | none | none | none | none | none … | … | … | … | … | … | … 0xBF | eip63 | none | none | none | none | none 0xC0 | eie0 | none | none | none | none | none … | … | … | … | … | … | … 0xFF | eie63 | none | none | none | none | none
```

**Detail:** Added table

</details>

<details>
<summary>🟠 **CHG-0520** Table added `0 | 1 | 2 | 3` (p. 30) — 0% similar</summary>

**Page:** ? → 30

**Preview:** 0 | 1 | 2 | 3

**New:**
```
0 | 1 | 2 | 3 | 4 | 5 | 6 siselect | sireg | sireg2 | sireg3 | sireg4 | sireg5 | sireg6 0x30 | iprio0 | none | none | none | none | none … | … | … | … | … | … | … 0x3F | iprio15 | none | none | none | none | none 0x40 | cycle | cyclecfg | none | cycleh | cyclecfgh | none 0x41 | none | none | none | none | none | none 0x42 | instret | instretcfg | none | instreth | instretcfgh | none 0x43 | hpmcounter3 | hpmevent3 | none | hpmcounter3h | hpmevent3h | none … | … | … | … | … | … | … 0x5F | hpmcounter31 | hpmevent31 | none | hpmcounter31 h | hpmevent31h | none 0x70 | eidelivery | none | none | none | none | none 0x71 | 0 | none | none | none | none | none 0x72 | eithreshold | none | none | none | none | none 0x73 | 0 | none | none | none | none | none … | … | … | … | … | … | … 0x7F | 0 | none | none | none | none | none 0x80 | eip0 | none | none | none | none | none … | … | … | … | … | … | … 0xBF | eip63 | none | none | none | none | none
```

**Detail:** Added table

</details>

<details>
<summary>🟠 **CHG-0480** Table removed `0 | 1 | 2` (p. 31) — 0% similar</summary>

**Page:** 31 → ?

**Preview:** 0 | 1 | 2

**Old:**
```
0 | 1 | 2 MXL[1:0] (WARL) | 0 (WARL) | Extensions[25:0] (WARL)
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0521** Table added `0 | 1 | 2 | 3` (p. 31) — 0% similar</summary>

**Page:** ? → 31

**Preview:** 0 | 1 | 2 | 3

**New:**
```
0 | 1 | 2 | 3 | 4 | 5 | 6 siselect | sireg | sireg2 | sireg3 | sireg4 | sireg5 | sireg6 0xC0 | eie0 | none | none | none | none | none … | … | … | … | … | … | … 0xFF | eie63 | none | none | none | none | none 0x200 | ctrsource0 | ctrtarget0 | ctrdata0 | 0 | 0 | 0 … | … | … | … | … | … | … 0x2FF | ctrsource255 | ctrtarget255 | ctrdata255 | 0 | 0 | 0
```

**Detail:** Added table

</details>

<details>
<summary>🟠 **CHG-0522** Table added `0 | 1 | 2 | 3` (p. 31) — 0% similar</summary>

**Page:** ? → 31

**Preview:** 0 | 1 | 2 | 3

**New:**
```
0 | 1 | 2 | 3 | 4 | 5 | 6 vsiselect | vsireg | vsireg2 | vsireg3 | vsireg4 | vsireg5 | vsireg6 0x30 | iprio0 | none | none | none | none | none … | … | … | … | … | … | … 0x3F | iprio15 | none | none | none | none | none 0x70 | eidelivery | none | none | none | none | none 0x71 | 0 | none | none | none | none | none 0x72 | eithreshold | none | none | none | none | none 0x73 | 0 | none | none | none | none | none … | … | … | … | … | … | … 0x7F | 0 | none | none | none | none | none 0x80 | eip0 | none | none | none | none | none … | … | … | … | … | … | … 0xBF | eip63 | none | none | none | none | none 0xC0 | eie0 | none | none | none | none | none … | … | … | … | … | … | … 0xFF | eie63 | none | none | none | none | none 0x200 | ctrsource0 | ctrtarget0 | ctrdata0 | 0 | 0 | 0 … | … | … | … | … | … | … 0x2FF | ctrsource255 | ctrtarget255 | ctrdata255 | 0 | 0 | 0
```

**Detail:** Added table

</details>

<details>
<summary>🟠 **CHG-0481** Table removed `0 | 1` (p. 34) — 0% similar</summary>

**Page:** 34 → ?

**Preview:** 0 | 1

**Old:**
```
0 | 1 Bank | Offset
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0482** Table removed `0 | 1 | 2 | 3` (p. 36) — 0% similar</summary>

**Page:** 36 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 SD | WPRI | SDT | SPELP | TSR | TW | TVM | MXR | SUM | MPRV | XS[1:0]
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0483** Table removed `0 | 1 | 2 | 3` (p. 36) — 0% similar</summary>

**Page:** 36 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 XS[1:0] | FS[1:0] | MPP[1:0] | VS[1:0] | SPP | MPIE | UBE | SPIE | WPRI | MIE | WPRI | SIE | WPRI
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0484** Table removed `0 | 1 | 2 | 3` (p. 36) — 0% similar</summary>

**Page:** 36 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 WPRI | MDT | MPELP | WPRI | MPV | GVA | MBE | SBE | SXL[1:0] | UXL[1:0]
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0485** Table removed `0 | 1 | 2 | 3` (p. 36) — 0% similar</summary>

**Page:** 36 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 WPRI | SDT | SPELP | TSR | TW | TVM | MXR | SUM | MPRV | XS[1:0]
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0486** Table removed `0 | 1 | 2 | 3` (p. 36) — 0% similar</summary>

**Page:** 36 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 XS[1:0] | FS[1:0] | MPP[1:0] | VS[1:0] | SPP | MPIE | UBE | SPIE | WPRI | MIE | WPRI | SIE | WPRI
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0487** Table removed `0 | 1 | 2 | 3` (p. 36) — 0% similar</summary>

**Page:** 36 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 WPRI | MDT | MPELP | WPRI | MPV | GVA | MBE | SBE | WPRI
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0488** Table removed `0 | 1` (p. 46) — 0% similar</summary>

**Page:** 46 → ?

**Preview:** 0 | 1

**Old:**
```
0 | 1 BASE[MXLEN-1:2] (WARL) | MODE (WARL)
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0453** Table modified `Row 2: | Execute ins | truction to uncon | figure unit |` (p. 47) — 98% similar</summary>

**Page:** 45 → 47

**Preview:** Row 2: | Execute ins | truction to uncon | figure unit |

**Old:**
```
[row 2, col 3] truction to unco [row 2, col 4] nfigure unit
```

**New:**
```
[row 2, col 3] truction to uncon [row 2, col 4] figure unit
```

**Detail:** 2 cells changed

</details>

<details>
<summary>🟠 **CHG-0454** Table modified `Row 2: | At conte | xt save in privile | ged code |` (p. 47) — 98% similar</summary>

**Page:** 45 → 47

**Preview:** Row 2: | At conte | xt save in privile | ged code |

**Old:**
```
[row 2, col 2] At contex [row 2, col 3] t save in privile
```

**New:**
```
[row 2, col 2] At conte [row 2, col 3] xt save in privile
```

**Detail:** 2 cells changed

</details>

<details>
<summary>🟠 **CHG-0455** Table modified `Row 2: | At contex | t restore in privil | eged code |` (p. 47) — 97% similar</summary>

**Page:** 45 → 47

**Preview:** Row 2: | At contex | t restore in privil | eged code |

**Old:**
```
[row 2, col 2] At context [row 2, col 3] restore in privil
```

**New:**
```
[row 2, col 2] At contex [row 2, col 3] t restore in privil
```

**Detail:** 2 cells changed

</details>

<details>
<summary>🟠 **CHG-0456** Table modified `Row 2: | Execute | instruction to en | able unit |` (p. 47) — 97% similar</summary>

**Page:** 45 → 47

**Preview:** Row 2: | Execute | instruction to en | able unit |

**Old:**
```
[row 2, col 2] Execute i [row 2, col 3] nstruction to en
```

**New:**
```
[row 2, col 2] Execute [row 2, col 3] instruction to en
```

**Detail:** 2 cells changed

</details>

<details>
<summary>🟠 **CHG-0460** Table modified `Row 2: | Execute | instruction to dis | able unit |` (p. 47) — 97% similar</summary>

**Page:** 45 → 47

**Preview:** Row 2: | Execute | instruction to dis | able unit |

**Old:**
```
[row 2, col 2] Execute i [row 2, col 3] nstruction to di [row 2, col 4] sable unit
```

**New:**
```
[row 2, col 2] Execute [row 2, col 3] instruction to dis [row 2, col 4] able unit
```

**Detail:** 3 cells changed

</details>

<details>
<summary>🟠 **CHG-0489** Table removed `0 | 1 | 2 | 3` (p. 49) — 0% similar</summary>

**Page:** 49 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 0 | LCOFIP | 0 | MEIP | 0 | SEIP | 0 | MTIP | 0 | STIP | 0 | MSIP | 0 | SSIP | 0
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0490** Table removed `0 | 1 | 2 | 3` (p. 49) — 0% similar</summary>

**Page:** 49 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 0 | LCOFIE | 0 | MEIE | 0 | SEIE | 0 | MTIE | 0 | STIE | 0 | MSIE | 0 | SSIE | 0
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0491** Table removed `0 | 1 | 2 | 3` (p. 53) — 0% similar</summary>

**Page:** 53 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 HPM31 | HPM30 | HPM29 | ... | HPM5 | HPM4 | HPM3 | IR | 0 | CY
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0492** Table removed `0 | 1 | 2 | 3` (p. 60) — 0% similar</summary>

**Page:** 60 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 | 4 | 5 STCE | PBMTE | ADUE | CDE | DTE | WPRI
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0464** Table modified `Row 3: 00 | Pointer masking is disabled (PMLEN = 0)` (p. 63) — 95% similar</summary>

**Page:** 215 → 63

**Preview:** Row 3: 00 | Pointer masking is disabled (PMLEN = 0)

**Old:**
```
[row 3, col 2] Pointer masking is disabled (PMLEN=0) [row 5, col 2] Pointer masking is enabled with PMLEN=XLEN-57 (PMLEN=7 on RV64) [row 6, col 2] Pointer masking is enabled with PMLEN=XLEN-48 (PMLEN=16 on RV64)
```

**New:**
```
[row 3, col 2] Pointer masking is disabled (PMLEN = 0) [row 5, col 2] Pointer masking is enabled with PMLEN = XLEN-57 (PMLEN = 7 on RV64) [row 6, col 2] Pointer masking is enabled with PMLEN = XLEN-48 (PMLEN = 16 on RV64)
```

**Detail:** 3 cells changed

</details>

<details>
<summary>🟠 **CHG-0493** Table removed `0 | 1 | 2 | 3` (p. 64) — 0% similar</summary>

**Page:** 64 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 | 4 funct12 | rs1 | funct3 | rd | opcode
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0523** Table added `0 | 1 | 2 | 3` (p. 64) — 0% similar</summary>

**Page:** ? → 64

**Preview:** 0 | 1 | 2 | 3

**New:**
```
0 | 1 | 2 | 3 Mode | SSEED | USEED | Description M |-|-| The seed CSR is always available in machine mode as normal (with a CSR read-write instruction.) Attempted read without a write raises an illegal-instruction exception regardless of mode and access control bits. U |-| 0 | Any seed CSR access raises an illegal-instruction exception. U |-| 1 | The seed CSR is accessible as normal. No exception is raised for read-write. S/HS | 0 |-| Any seed CSR access raises an illegal-instruction exception. S/HS | 1 |-| The seed CSR is accessible as normal. No exception is raised for read-write. VS/VU | 0 |-| Any seed CSR access raises an illegal-instruction exception. VS/VU | 1 |-| A read-write seed access raises a virtual-instruction exception, while other access conditions raise an illegal-instruction exception.
```

**Detail:** Added table

</details>

<details>
<summary>🟠 **CHG-0494** Table removed `0 | 1 | 2 | 3` (p. 65) — 0% similar</summary>

**Page:** 65 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 | 4 funct12 | rs1 | funct3 | rd | opcode
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0495** Table removed `0 | 1 | 2 | 3` (p. 65) — 0% similar</summary>

**Page:** 65 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 | 4 funct12 | rs1 | funct3 | rd | opcode
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0496** Table removed `0 | 1 | 2 | 3` (p. 66) — 0% similar</summary>

**Page:** 66 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 | 4 funct6 | custom | funct3 | custom | opcode
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0524** Table added `0 | 1` (p. 66) — 0% similar</summary>

**Page:** ? → 66

**Preview:** 0 | 1

**New:**
```
0 | 1 Value | Description 00 | Pointer masking is disabled (PMLEN = 0) 01 | Reserved 10 | Pointer masking is enabled with PMLEN = XLEN-57 (PMLEN = 7 on RV64) 11 | Pointer masking is enabled with PMLEN = XLEN-48 (PMLEN = 16 on RV64)
```

**Detail:** Added table

</details>

<details>
<summary>🟠 **CHG-0497** Table removed `0 | 1 | 2 | 3` (p. 74) — 0% similar</summary>

**Page:** 74 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 pmp3cfg | pmp2cfg | pmp1cfg | pmp0cfg
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0498** Table removed `0 | 1 | 2 | 3` (p. 74) — 0% similar</summary>

**Page:** 74 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 pmp7cfg | pmp6cfg | pmp5cfg | pmp4cfg
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0499** Table removed `0 | 1 | 2 | 3` (p. 74) — 0% similar</summary>

**Page:** 74 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 pmp63cfg | pmp62cfg | pmp61cfg | pmp60cfg
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0500** Table removed `0 | 1 | 2 | 3` (p. 75) — 0% similar</summary>

**Page:** 75 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 pmp7cfg | pmp6cfg | pmp5cfg | pmp4cfg | pmp3cfg | pmp2cfg | pmp1cfg | pmp0cfg
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0501** Table removed `0 | 1 | 2 | 3` (p. 75) — 0% similar</summary>

**Page:** 75 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 pmp15cfg | pmp14cfg | pmp13cfg | pmp12cfg | pmp11cfg | pmp10cfg | pmp9cfg | pmp8cfg
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0502** Table removed `0 | 1 | 2 | 3` (p. 75) — 0% similar</summary>

**Page:** 75 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 pmp63cfg | pmp62cfg | pmp61cfg | pmp60cfg | pmp59cfg | pmp58cfg | pmp57cfg | pmp56cfg
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0503** Table removed `0 | 1` (p. 75) — 0% similar</summary>

**Page:** 75 → ?

**Preview:** 0 | 1

**Old:**
```
0 | 1 0 (WARL) | address[55:2] (WARL)
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0504** Table removed `0 | 1 | 2 | 3` (p. 75) — 0% similar</summary>

**Page:** 75 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 | 4 | 5 L | 0 | A | X | W | R
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0505** Table removed `0 | 1 | 2 | 3` (p. 86) — 0% similar</summary>

**Page:** 86 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 | 4 Number | Privilege | Width | Name | Description 0x150 | SRW | XLEN | siselect | Supervisor indirect register select 0x151 | SRW | XLEN | sireg | Supervisor indirect register alias
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0471** Table modified `Row 8: 0x156 | SRW | XLEN | sireg5 | Supervisor indirect register alias 5` (p. 88) — 0% similar</summary>

**Page:** 87 → 88

**Preview:** Row 8: 0x156 | SRW | XLEN | sireg5 | Supervisor indirect register alias 5

**New:**
```
0x156 | SRW | XLEN | sireg5 | Supervisor indirect register alias 5
```

**Detail:** Row added

</details>

<details>
<summary>🟠 **CHG-0474** Table modified `Row 14: 1 | 0 | 1 | 0 | Locked Shared code region: Execu | te only on both M and S/U mode.*` (p. 93) — 0% similar</summary>

**Page:** 92 → 93

**Preview:** Row 14: 1 | 0 | 1 | 0 | Locked Shared code region: Execu | te only on both M and S/U mode.*

**New:**
```
1 | 0 | 1 | 0 | Locked Shared code region: Execu | te only on both M and S/U mode.*
```

**Detail:** Row added

</details>

<details>
<summary>🟠 **CHG-0506** Table removed `0 | 1 | 2 | 3` (p. 93) — 0% similar</summary>

**Page:** 93 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 | 4 | 5 B | its on pmp | cfg registe | r | Re | sult 1 | 0 | 1 | 0 | Locked Shared code region: E mo | xecute only on both M and S/U de.* 1 | 0 | 1 | 1 | Locked Shared code region read/execute | : Execute only on S/U mode, on M mode.* 1 | 1 | 0 | 0 | Locked Read-only region* | Access Exception 1 | 1 | 0 | 1 | Locked Read/Execute region* | Access Exception 1 | 1 | 1 | 0 | Locked Read/Write region* | Access Exception 1 | 1 | 1 | 1 | Locked Shared data region: Rea | d only on both M and S/U mode.*
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0458** Table modified `Row 4: 0x41 | | See bel | ow |` (p. 100) — 98% similar</summary>

**Page:** 102 → 100

**Preview:** Row 4: 0x41 | | See bel | ow |

**Old:**
```
[row 4, col 3] See be [row 4, col 4] low
```

**New:**
```
[row 4, col 3] See bel [row 4, col 4] ow
```

**Detail:** 2 cells changed

</details>

<details>
<summary>🟠 **CHG-0525** Table added `0 | 1` (p. 105) — 0% similar</summary>

**Page:** ? → 105

**Preview:** 0 | 1

**New:**
```
0 | 1 Field | Description M, S, U | Enable transfer recording in the selected privileged mode(s). RASEMU | Enables RAS (Return Address Stack) Emulation Mode. See RAS (Return Address Stack) Emulation Mode. MTE | Enables recording of traps to M-mode when M=0. See External Traps. STE | Enables recording of traps to S-mode when S=0. See External Traps. BPFRZ | Set sctrstatus.FROZEN on a breakpoint exception that traps to M-mode or S-mode. See Freeze. LCOFIFRZ | Set sctrstatus.FROZEN on local-counter-overflow interrupt (LCOFI) that traps to M-mode or S-mode. See Freeze. EXCINH | Inhibit recording of exceptions. See Transfer Type Filtering. INTRINH | Inhibit recording of interrupts. See Transfer Type Filtering. TRETINH | Inhibit recording of trap returns. See Transfer Type Filtering. NTBREN | Enable recording of not-taken branches. See Transfer Type Filtering. TKBRINH | Inhibit recording of taken branches. See Transfer Type Filtering. INDCALLINH | Inhibit recording of indirect calls. See Transfer Type Filtering. DIRCALLINH | Inhibit recording of direct calls. See Transfer Type Filtering. INDJMPINH | Inhibit recording of indirect jumps (without linkage). See Transfer Type Filtering. DIRJMPINH | Inhibit recording of direct jumps (without linkage). See Transfer Type Filtering. CORSWAPINH | Inhibit recording of co-routine swaps. See Transfer Type Filtering. RETINH | Inhibit recording of function returns. See Transfer Type Filtering. INDLJMPINH | Inhibit recording of other indirect jumps (with linkage). See Transfer Type Filtering. DIRLJMPINH | Inhibit recording of other direct jumps (with linkage). See Transfer Type Filtering. Custom[3:0] | WARL bits designated for custom use. The value 0 must correspond to standard behavior. See Custom Extensions.
```

**Detail:** Added table

</details>

<details>
<summary>🟠 **CHG-0526** Table added `0 | 1` (p. 106) — 0% similar</summary>

**Page:** ? → 106

**Preview:** 0 | 1

**New:**
```
0 | 1 Field | Description S | Enable transfer recording in VS-mode. U | Enable transfer recording in VU-mode. STE | Enables recording of traps to VS-mode when S=0. See External Traps.. BPFRZ | Set sctrstatus.FROZEN on a breakpoint exception that traps to VS-mode. See Freeze. LCOFIFRZ | Set sctrstatus.FROZEN on local-counter-overflow interrupt (LCOFI) that traps to VS-mode. See Freeze. Other field definitions implemented in sctrc | match those of sctrctl. The optional fields implemented in vsctrctl should match those tl.
```

**Detail:** Added table

</details>

<details>
<summary>🟠 **CHG-0507** Table removed `0 | 1` (p. 107) — 0% similar</summary>

**Page:** 107 → ?

**Preview:** 0 | 1

**Old:**
```
0 | 1 Field | Description M, S, U | Enable transfer recording in the selected privileged mode(s). RASEMU | Enables RAS (Return Address Stack) Emulation Mode. See Section 11.5.4. MTE | Enables recording of traps to M-mode when M=0. See Section 11.5.1.2. STE | Enables recording of traps to S-mode when S=0. See Section 11.5.1.2. BPFRZ | Set sctrstatus.FROZEN on a breakpoint exception that traps to M-mode or S-mode. See Section 11.5.5. LCOFIFRZ | Set sctrstatus.FROZEN on local-counter-overflow interrupt (LCOFI) that traps to M-mode or S-mode. See Section 11.5.5. EXCINH | Inhibit recording of exceptions. See Section 11.5.2. INTRINH | Inhibit recording of interrupts. See Section 11.5.2. TRETINH | Inhibit recording of trap returns. See Section 11.5.2. NTBREN | Enable recording of not-taken branches. See Section 11.5.2. TKBRINH | Inhibit recording of taken branches. See Section 11.5.2. INDCALLINH | Inhibit recording of indirect calls. See Section 11.5.2. DIRCALLINH | Inhibit recording of direct calls. See Section 11.5.2. INDJMPINH | Inhibit recording of indirect jumps (without linkage). See Section 11.5.2. DIRJMPINH | Inhibit recording of direct jumps (without linkage). See Section 11.5.2. CORSWAPINH | Inhibit recording of co-routine swaps. See Section 11.5.2. RETINH | Inhibit recording of function returns. See Section 11.5.2. INDLJMPINH | Inhibit recording of other indirect jumps (with linkage). See Section 11.5.2. DIRLJMPINH | Inhibit recording of other direct jumps (with linkage). See Section 11.5.2. Custom[3:0] | WARL bits designated for custom use. The value 0 must correspond to standard behavior. See Section 11.6.
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0469** Table modified `Row 3: WRPTR | WARL field that indicates the physical CTR buffer entry to be written next. It is incremented after new transfers are recorded (see Behavior), though there are exceptions when xctrctl.RASEMU=1, see RAS (Return Address Stack) Emulation Mode. For a given CTR depth (where depth = 2(DEPTH+4)), WRPTR wraps to 0 on an increment when the value matches depth-1, and to depth-1 on a decrement when the value is 0. Bits above those needed to represent depth-1 (e.g., bits 7:4 for a depth of 16) are read-only 0. On depth changes, WRPTR holds an unspecified but legal value.` (p. 108) — 92% similar</summary>

**Page:** 110 → 108

**Preview:** Row 3: WRPTR | WARL field that indicates the physical CTR buffer entry to be written next. It is incremented after new transfers are recorded (see Behavior), though there are exceptions when xctrctl.RASEMU=1, see RAS (Return Address Stack) Emulation Mode. For a given CTR depth (where depth = 2(DEPTH+4)), WRPTR wraps to 0 on an increment when the value matches depth-1, and to depth-1 on a decrement when the value is 0. Bits above those needed to represent depth-1 (e.g., bits 7:4 for a depth of 16) are read-only 0. On depth changes, WRPTR holds an unspecified but legal value.

**Old:**
```
[row 3, col 2] WARL field that indicates the physical CTR buffer entry to be written next. It is incremented after new transfers are recorded (see Section 11.5), though there are exceptions when x ctrctl.RASEMU=1, see Section 11.5.4. For a given CTR depth (where depth = 2(DEPTH+4)), WRPTR wraps to 0 on an increment when the value matches depth-1, and to depth-1 on a decrement when the value is 0. Bits above those needed to represent depth-1 (e.g., bits 7:4 for a depth of 16) are read-only 0. On depth changes, WRPTR holds an unspecified but legal value. [row 4, col 2] Inhibit transfer recording. See Section 11.5.5.
```

**New:**
```
[row 3, col 2] WARL field that indicates the physical CTR buffer entry to be written next. It is incremented after new transfers are recorded (see Behavior), though there are exceptions when xctrctl.RASEMU=1, see RAS (Return Address Stack) Emulation Mode. For a given CTR depth (where depth = 2(DEPTH+4)), WRPTR wraps to 0 on an increment when the value matches depth-1, and to depth-1 on a decrement when the value is 0. Bits above those needed to represent depth-1 (e.g., bits 7:4 for a depth of 16) are read-only 0. On depth changes, WRPTR holds an unspecified but legal value. [row 4, col 2] Inhibit transfer recording. See Freeze.
```

**Detail:** 2 cells changed

</details>

<details>
<summary>🟠 **CHG-0508** Table removed `0 | 1` (p. 109) — 0% similar</summary>

**Page:** 109 → ?

**Preview:** 0 | 1

**Old:**
```
0 | 1 Field | Description S | Enable transfer recording in VS-mode. U | Enable transfer recording in VU-mode. STE | Enables recording of traps to VS-mode when S=0. See Section 11.5.1.2. BPFRZ | Set sctrstatus.FROZEN on a breakpoint exception that traps to VS-mode. See Section 11.5.5. LCOFIFRZ | Set sctrstatus.FROZEN on local-counter-overflow interrupt (LCOFI) that traps to VS-mode. See Section 11.5.5. Other field definitions implemented in sctrc | match those of sctrctl. The optional fields implemented in vsctrctl should match those tl.
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0468** Table modified `Row 3: TYPE[3:0] | Identifies the type of the control flow transfer recorded in the entry, using the encodings listed in Table 33. Implementations that do not support this field will report 0. | WARL` (p. 110) — 73% similar</summary>

**Page:** 113 → 110

**Preview:** Row 3: TYPE[3:0] | Identifies the type of the control flow transfer recorded in the entry, using the encodings listed in Table 33. Implementations that do not support this field will report 0. | WARL

**Old:**
```
[row 3, col 2] Identifies the type of the control flow transfer recorded in the entry, using the encodings listed in Table 28. Implementations that do not support this field will report 0. [row 4, col 2] Cycle Count Valid. See Section 11.5.3. [row 5, col 2] Cycle Count, composed of the Cycle Count Exponent (CCE, in CC[15:12]) and Cycle Count Mantissa (CCM, in CC[11:0]). See Section 11.5.3.
```

**New:**
```
[row 3, col 2] Identifies the type of the control flow transfer recorded in the entry, using the encodings listed in Table 33. Implementations that do not support this field will report 0. [row 4, col 2] Cycle Count Valid. See Cycle Counting. [row 5, col 2] Cycle Count, composed of the Cycle Count Exponent (CCE, in CC[15:12]) and Cycle Count Mantissa (CCM, in CC[11:0]). See Cycle Counting.
```

**Detail:** 3 cells changed

</details>

<details>
<summary>🟠 **CHG-0465** Table modified `Row 4: Trap | Enabled | Recorded. | External trap. Not recorded by default, but see External Traps..` (p. 112) — 79% similar</summary>

**Page:** 115 → 112

**Preview:** Row 4: Trap | Enabled | Recorded. | External trap. Not recorded by default, but see External Traps..

**Old:**
```
External trap. Not recorded by default, but see Section 11.5.1.2.
```

**New:**
```
External trap. Not recorded by default, but see External Traps..
```

**Detail:** Cell changed (row 4, col 4)

</details>

<details>
<summary>🟠 **CHG-0527** Table added `0 | 1 | 2` (p. 126) — 0% similar</summary>

**Page:** ? → 126

**Preview:** 0 | 1 | 2

**New:**
```
0 | 1 | 2 Interrupt | Exception Code | Description 1 1 1 1 1 1 1 1 1 1 | 0 1 2-4 5 6-8 9 10-12 13 14-15 ≥16 | Reserved Supervisor software interrupt Reserved Supervisor timer interrupt Reserved Supervisor external interrupt Reserved Counter-overflow interrupt Reserved Designated for platform use
```

**Detail:** Added table

</details>

<details>
<summary>🟠 **CHG-0472** Table modified `Row 4: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 | 0 1 2 3 4 5 6 7 8 9 10-11 12 13 14 15 16-17 18 19 20-23 24-31 32-47 48-63 ≥64 | Instruction address misaligned Instruction access fault Illegal instruction Breakpoint Load address misaligned Load access fault Store/AMO address misaligned Store/AMO access fault Environment call from U-mode Environment call from S-mode Reserved Instruction page fault Load page fault Reserved Store/AMO page fault Reserved Software check Hardware error Reserved Designated for custom use Reserved Designated for custom use Reserved` (p. 127) — 0% similar</summary>

**Page:** 131 → 127

**Preview:** Row 4: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 | 0 1 2 3 4 5 6 7 8 9 10-11 12 13 14 15 16-17 18 19 20-23 24-31 32-47 48-63 ≥64 | Instruction address misaligned Instruction access fault Illegal instruction Breakpoint Load address misaligned Load access fault Store/AMO address misaligned Store/AMO access fault Environment call from U-mode Environment call from S-mode Reserved Instruction page fault Load page fault Reserved Store/AMO page fault Reserved Software check Hardware error Reserved Designated for custom use Reserved Designated for custom use Reserved

**Old:**
```
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 | 0 1 2 3 4 5 6 7 8 9 10-11 12 13 14 15 16-17 18 19 20-23 24-31 32-47 48-63 ≥64 | Instruction address misaligned Instruction access fault Illegal instruction Breakpoint Load address misaligned Load access fault Store/AMO address misaligned Store/AMO access fault Environment call from U-mode Environment call from S-mode Reserved Instruction page fault Load page fault Reserved Store/AMO page fault Reserved Software check Hardware error Reserved Designated for custom use Reserved Designated for custom use Reserved
```

**Detail:** Row removed

</details>

<details>
<summary>🟠 **CHG-0528** Table added `0 | 1` (p. 130) — 0% similar</summary>

**Page:** ? → 130

**Preview:** 0 | 1

**New:**
```
0 | 1 Value | Description 00 | Pointer masking is disabled (PMLEN = 0) 01 | Reserved 10 | Pointer masking is enabled with PMLEN = XLEN-57 (PMLEN = 7 on RV64) 11 | Pointer masking is enabled with PMLEN = XLEN-48 (PMLEN = 16 on RV64)
```

**Detail:** Added table

</details>

<details>
<summary>🟠 **CHG-0461** Table modified `Row 2: i | pte.ppn[i] | Description | pte.napot bits _` (p. 145) — 87% similar</summary>

**Page:** 150 → 145

**Preview:** Row 2: i | pte.ppn[i] | Description | pte.napot bits _

**Old:**
```
pte.napot_bits
```

**New:**
```
pte.napot bits _
```

**Detail:** Cell changed (row 2, col 4)

</details>

<details>
<summary>🟠 **CHG-0459** Table modified `Row 2: i | pte.ppn[i] | Description | pte.napot bits _` (p. 146) — 87% similar</summary>

**Page:** 151 → 146

**Preview:** Row 2: i | pte.ppn[i] | Description | pte.napot bits _

**Old:**
```
pte.napot_bits
```

**New:**
```
pte.napot bits _
```

**Detail:** Cell changed (row 2, col 4)

</details>

<details>
<summary>🟠 **CHG-0529** Table added `0 | 1` (p. 165) — 0% similar</summary>

**Page:** ? → 165

**Preview:** 0 | 1

**New:**
```
0 | 1 Value | Description 00 | Pointer masking is disabled (PMLEN = 0) 01 | Reserved 10 | Pointer masking is enabled with PMLEN = XLEN-57 (PMLEN = 7 on RV64) 11 | Pointer masking is enabled with PMLEN = XLEN-48 (PMLEN = 16 on RV64)
```

**Detail:** Added table

</details>

<details>
<summary>🟠 **CHG-0509** Table removed `0 | 1` (p. 173) — 0% similar</summary>

**Page:** 173 → ?

**Preview:** 0 | 1

**Old:**
```
0 | 1 WPRI | PMM
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0510** Table removed `0 | 1 | 2 | 3` (p. 173) — 0% similar</summary>

**Page:** 173 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 WPRI | CBZE | CBCFE | CBIE | SSE | LPE | WPRI | FIOM
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0511** Table removed `0 | 1 | 2 | 3` (p. 174) — 0% similar</summary>

**Page:** 174 → ?

**Preview:** 0 | 1 | 2 | 3

**Old:**
```
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 HPM31 | HPM30 | HPM29 | ... | HPM5 | HPM4 | HPM3 | IR | TM | CY
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0463** Table modified `Row 1: 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7` (p. 177) — 0% similar</summary>

**Page:** 185 → 177

**Preview:** Row 1: 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7

**Old:**
```
8
```

**Detail:** Cell changed (row 1, col 9)

</details>

<details>
<summary>🟠 **CHG-0467** Table modified `Row 1: 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8` (p. 177) — 49% similar</summary>

**Page:** 185 → 177

**Preview:** Row 1: 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8

**Old:**
```
[row 1, col 10] 9 [row 1, col 11] 10 [row 2, col 1] [row 2, col 2] WPRI [row 2, col 3] TSR [row 2, col 4] TW [row 2, col 5] TVM [row 2, col 6] MXR [row 2, col 7] SUM [row 2, col 8] MPRV [row 2, col 9] XS[1:0] [row 2, col 10] FS[1:0]
```

**New:**
```
[row 1, col 10] [row 1, col 11] [row 2, col 1] WPRI [row 2, col 2] TSR [row 2, col 3] TW [row 2, col 4] TVM [row 2, col 5] MXR [row 2, col 6] SUM [row 2, col 7] MPRV [row 2, col 8] XS[1:0] [row 2, col 9] FS[1:0] [row 2, col 10]
```

**Detail:** 12 cells changed

</details>

<details>
<summary>🟠 **CHG-0512** Table removed `0 | 1` (p. 178) — 0% similar</summary>

**Page:** 178 → ?

**Preview:** 0 | 1

**Old:**
```
0 | 1 SD | WPRI
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0513** Table removed `0 | 1` (p. 181) — 0% similar</summary>

**Page:** 181 → ?

**Preview:** 0 | 1

**Old:**
```
0 | 1 Interrupt | Exception Code (WLRL)
```

**Detail:** Removed table

</details>

<details>
<summary>🟠 **CHG-0470** Table modified `Row 6: 1 1 1 1 | 12 13 14-15 ≥16 | Supervisor guest external interrupt Counter-overflow interrupt Reserved Designated for platform use` (p. 184) — 94% similar</summary>

**Page:** 192 → 184

**Preview:** Row 6: 1 1 1 1 | 12 13 14-15 ≥16 | Supervisor guest external interrupt Counter-overflow interrupt Reserved Designated for platform use

**Old:**
```
Supervisor guest external interrupt Reserved for counter-overflow interrupt Reserved Designated for platform use
```

**New:**
```
Supervisor guest external interrupt Counter-overflow interrupt Reserved Designated for platform use
```

**Detail:** Cell changed (row 6, col 3)

</details>

<details>
<summary>🟠 **CHG-0466** Table modified `Row 3: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 | 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24-31 32-47 48-63 ≥64 | Instruction address misaligned Instruction access fault Illegal instruction Breakpoint Load address misaligned Load access fault Store/AMO address misaligned Store/AMO access fault Environment call from U-mode or VU-mode Environment call from HS-mode Environment call from VS-mode Environment call from M-mode Instruction page fault Load page fault Reserved Store/AMO page fault Double trap Reserved Software check Hardware error Instruction guest-page fault Load guest-page fault Virtual instruction Store/AMO guest-page fault Designated for custom use Reserved Designated for custom use Reserved` (p. 185) — 91% similar</summary>

**Page:** 193 → 185

**Preview:** Row 3: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 | 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24-31 32-47 48-63 ≥64 | Instruction address misaligned Instruction access fault Illegal instruction Breakpoint Load address misaligned Load access fault Store/AMO address misaligned Store/AMO access fault Environment call from U-mode or VU-mode Environment call from HS-mode Environment call from VS-mode Environment call from M-mode Instruction page fault Load page fault Reserved Store/AMO page fault Double trap Reserved Software check Hardware error Instruction guest-page fault Load guest-page fault Virtual instruction Store/AMO guest-page fault Designated for custom use Reserved Designated for custom use Reserved

**Old:**
```
[row 3, col 1] 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 [row 3, col 2] 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16-19 20 21 22 23 24-31 32-47 48-63 ≥64 [row 3, col 3] Instruction address misaligned Instruction access fault Illegal instruction Breakpoint Load address misaligned Load access fault Store/AMO address misaligned Store/AMO access fault Environment call from U-mode or VU-mode Environment call from HS-mode Environment call from VS-mode Environment call from M-mode Instruction page fault Load page fault Reserved Store/AMO page fault Reserved Instruction guest-page fault Load guest-page fault Virtual instruction Store/AMO guest-page fault Designated for custom use Reserved Designated for custom use Reserved
```

**New:**
```
[row 3, col 1] 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 [row 3, col 2] 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24-31 32-47 48-63 ≥64 [row 3, col 3] Instruction address misaligned Instruction access fault Illegal instruction Breakpoint Load address misaligned Load access fault Store/AMO address misaligned Store/AMO access fault Environment call from U-mode or VU-mode Environment call from HS-mode Environment call from VS-mode Environment call from M-mode Instruction page fault Load page fault Reserved Store/AMO page fault Double trap Reserved Software check Hardware error Instruction guest-page fault Load guest-page fault Virtual instruction Store/AMO guest-page fault Designated for custom use Reserved Designated for custom use Reserved
```

**Detail:** 3 cells changed

</details>

<details>
<summary>🟠 **CHG-0451** Table modified `Row 2: Exception | Zero | Transformed Standard Instruction | Custom Value | Pseudoinstructio n Value` (p. 190) — 96% similar</summary>

**Page:** 198 → 190

**Preview:** Row 2: Exception | Zero | Transformed Standard Instruction | Custom Value | Pseudoinstructio n Value

**Old:**
```
Pseudoinstructi on Value
```

**New:**
```
Pseudoinstructio n Value
```

**Detail:** Cell changed (row 2, col 5)

</details>

<details>
<summary>🟠 **CHG-0530** Table added `0 | 1 | 2 | 3` (p. 209) — 0% similar</summary>

**Page:** ? → 209

**Preview:** 0 | 1 | 2 | 3

**New:**
```
0 | 1 | 2 | 3 | 4 | 5 0001000 | 00100 | 00000 | 000 | 00000 | 1110011
```

**Detail:** Added table

</details>

### Modified notes (13)

<details>
<summary>🟠 **CHG-0275** Note modified `Note that the new count overflow interrupt will be treated as a standard local interrupt that is assigned to` — 99% similar</summary>

**Old:**
```
Note that the new count overflow interrupt will be treated as a standard local interrupt that is assigned
```

**New:**
```
Note that the new count overflow interrupt will be treated as a standard local interrupt that is assigned to
```

**Detail:** Changed '' to 'to'

</details>

<details>
<summary>🟠 **CHG-0276** Note modified `Note that the pointer masking setting that is applied only depends on the active privilege mode, not on the` — 98% similar</summary>

**Old:**
```
Note that the pointer masking setting that is applied only depends on the active privilege mode, not on
```

**New:**
```
Note that the pointer masking setting that is applied only depends on the active privilege mode, not on the
```

**Detail:** Changed '' to 'the'

</details>

<details>
<summary>🟠 **CHG-0277** Note modified `Note that this includes cases where page-based virtual memory is not in effect; i.e., although` — 95% similar</summary>

**Old:**
```
Note that this includes cases where page-based virtual memory is not in effect; i.e.,
```

**New:**
```
Note that this includes cases where page-based virtual memory is not in effect; i.e., although
```

**Detail:** Changed '' to 'although'

</details>

<details>
<summary>🟠 **CHG-0278** Note modified `Note that external trap recording does not depend on EXCINH/INTRINH. Thus, when external` — 95% similar</summary>

**Old:**
```
Note that external trap recording does not depend on EXCINH/INTRINH. Thus, when
```

**New:**
```
Note that external trap recording does not depend on EXCINH/INTRINH. Thus, when external
```

**Detail:** Changed '' to 'external'

</details>

<details>
<summary>🟠 **CHG-0279** Note modified `Note that setting UXL/SXL/MXL to 1 and back to 0 does not preserve the previous values of` — 94% similar</summary>

**Old:**
```
Note that setting UXL/SXL/MXL to 1 and back to 0 does not preserve the previous
```

**New:**
```
Note that setting UXL/SXL/MXL to 1 and back to 0 does not preserve the previous values of
```

**Detail:** Changed '' to 'values of'

</details>

<details>
<summary>🟠 **CHG-0280** Note modified `Note that load and load-reserved instructions generate load exceptions, whereas store, store-conditional,` — 94% similar</summary>

**Old:**
```
Note that load and load-reserved instructions generate load exceptions, whereas store, store-
```

**New:**
```
Note that load and load-reserved instructions generate load exceptions, whereas store, store-conditional,
```

**Detail:** Changed 'store-' to 'store-conditional,'

</details>

<details>
<summary>🟠 **CHG-0281** Note removed `important, whereas software interrupts are used for inter-processor messaging.` — 0% similar</summary>

**Old:**
```
important, whereas software interrupts are used for inter-processor messaging.
```

**Detail:** Removed note

</details>

<details>
<summary>🟠 **CHG-0282** Note removed `Note that this feature is intended to be used as a debug mechanism, or as a` — 0% similar</summary>

**Old:**
```
Note that this feature is intended to be used as a debug mechanism, or as a
```

**Detail:** Removed note

</details>

<details>
<summary>🟠 **CHG-0283** Note removed `Note also that, for basic loads and stores, the transformations replace the instruction’s immediate` — 0% similar</summary>

**Old:**
```
Note also that, for basic loads and stores, the transformations replace the instruction’s immediate
```

**Detail:** Removed note

</details>

<details>
<summary>🟠 **CHG-0284** Note added `caution. If a multi-instruction read-modify-write to sctrstatus is performed while CTR is` — 0% similar</summary>

**New:**
```
caution. If a multi-instruction read-modify-write to sctrstatus is performed while CTR is
```

**Detail:** Added note

</details>

<details>
<summary>🟠 **CHG-0285** Note added `Note that the CSR contains only bits XLEN-1 through 2 of the address BASE. When used as an address, the` — 0% similar</summary>

**New:**
```
Note that the CSR contains only bits XLEN-1 through 2 of the address BASE. When used as an address, the
```

**Detail:** Added note

</details>

<details>
<summary>🟠 **CHG-0286** Note added `Note that failing to mark a global mapping as global merely reduces performance, whereas marking a non-` — 0% similar</summary>

**New:**
```
Note that failing to mark a global mapping as global merely reduces performance, whereas marking a non-
```

**Detail:** Added note

</details>

<details>
<summary>🟠 **CHG-0287** Note added `Note that it’s still possible to register executable Shared-Region rules using initial register settings (that` — 0% similar</summary>

**New:**
```
Note that it’s still possible to register executable Shared-Region rules using initial register settings (that
```

**Detail:** Added note

</details>

## 🟡 Structural Changes

### Sections added (197)

<details>
<summary>🟡 **CHG-0002** Added `1.1` — 0% similar</summary>

**New:**
```
RISC-V Privileged Software Stack Terminology ........................................................................................................ 10
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0003** Added `1.1:7` — 0% similar</summary>

**New:**
```
RISC-V Privileged Software Stack Terminology
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0004** Added `1.2` — 0% similar</summary>

**New:**
```
Privilege Levels
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0005** Added `1.3` — 0% similar</summary>

**New:**
```
Debug Mode
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0006** Added `11.1` — 0% similar</summary>

**New:**
```
CSRs
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0007** Added `11.1.2` — 0% similar</summary>

**New:**
```
Supervisor Control Transfer Records Control Register (sctrctl)
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0008** Added `11.1.4` — 0% similar</summary>

**New:**
```
Supervisor Control Transfer Records Depth Register (sctrdepth)
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0009** Added `11.1.5` — 0% similar</summary>

**New:**
```
Supervisor Control Transfer Records Status Register (sctrstatus)
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0010** Added `11.1:96` — 0% similar</summary>

**New:**
```
CSRs | Page 98
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0011** Added `11.2` — 0% similar</summary>

**New:**
```
Entry Registers
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0012** Added `11.2.3` — 0% similar</summary>

**New:**
```
Control Transfer Record Metadata Register (ctrdata)
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0013** Added `11.5` — 0% similar</summary>

**New:**
```
Behavior
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0014** Added `11.5.1` — 0% similar</summary>

**New:**
```
Privilege Mode Transitions
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0015** Added `11.5.1.2` — 0% similar</summary>

**New:**
```
External Traps
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0016** Added `11.5.2` — 0% similar</summary>

**New:**
```
Transfer Type Filtering
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0017** Added `11.5.3` — 0% similar</summary>

**New:**
```
Cycle Counting
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0018** Added `11.5.4` — 0% similar</summary>

**New:**
```
RAS (Return Address Stack) Emulation Mode
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0019** Added `11.5.5` — 0% similar</summary>

**New:**
```
Freeze
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0020** Added `11.6` — 0% similar</summary>

**New:**
```
Custom Extensions
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0021** Added `12.1` — 0% similar</summary>

**New:**
```
Supervisor CSRs
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0022** Added `12.1.1.1` — 0% similar</summary>

**New:**
```
Base ISA Control in sstatus Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0023** Added `12.1.1.3` — 0% similar</summary>

**New:**
```
Endianness Control in sstatus Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0024** Added `12.1.10` — 0% similar</summary>

**New:**
```
Supervisor Environment Configuration (senvcfg) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0025** Added `12.1.11` — 0% similar</summary>

**New:**
```
Supervisor Address Translation and Protection (satp) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0026** Added `12.1.12` — 0% similar</summary>

**New:**
```
Supervisor Timer (stimecmp) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0027** Added `12.1.2` — 0% similar</summary>

**New:**
```
Supervisor Trap Vector Base Address (stvec) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0028** Added `12.1.3` — 0% similar</summary>

**New:**
```
Supervisor Interrupt (sip and sie) Registers
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0029** Added `12.1.4` — 0% similar</summary>

**New:**
```
Supervisor Timers and Performance Counters
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0030** Added `12.1.5` — 0% similar</summary>

**New:**
```
Counter-Enable (scounteren) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0031** Added `12.1.8` — 0% similar</summary>

**New:**
```
Supervisor Cause (scause) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0032** Added `12.1.9` — 0% similar</summary>

**New:**
```
Supervisor Trap Value (stval) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0033** Added `12.10` — 0% similar</summary>

**New:**
```
"Svadu" Extension for Hardware Updating of A/D Bits, Version 1.0
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0034** Added `12.11` — 0% similar</summary>

**New:**
```
"Svvptc" Extension for Obviating Memory-Management Instructions after Marking PTEs
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0035** Added `12.12` — 0% similar</summary>

**New:**
```
"Svrsw60t59b" Extension for PTE Reserved-for-Software Bits 60-59,
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0036** Added `12.13` — 0% similar</summary>

**New:**
```
"Ssqosid" Extension for Quality-of-Service (QoS) Identifiers, Version 1.0 | Page 145
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0037** Added `12.1:120` — 0% similar</summary>

**New:**
```
Supervisor CSRs | Page 122
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0038** Added `12.1:122` — 0% similar</summary>

**New:**
```
Supervisor CSRs | Page 124
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0039** Added `12.2` — 0% similar</summary>

**New:**
```
Supervisor Instructions
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0040** Added `12.2:125` — 0% similar</summary>

**New:**
```
Supervisor Instructions | Page 127
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0041** Added `12.2:126` — 0% similar</summary>

**New:**
```
Supervisor Instructions | Page 128
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0042** Added `12.3` — 0% similar</summary>

**New:**
```
Sv32: Page-Based 32-bit Virtual-Memory Systems
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0043** Added `12.3.2` — 0% similar</summary>

**New:**
```
Virtual Address Translation Process
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0044** Added `12.3:128` — 0% similar</summary>

**New:**
```
Sv32: Page-Based 32-bit Virtual-Memory Systems | Page 130
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0045** Added `12.3:129` — 0% similar</summary>

**New:**
```
Sv32: Page-Based 32-bit Virtual-Memory Systems | Page 131
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0046** Added `12.3:130` — 0% similar</summary>

**New:**
```
Sv32: Page-Based 32-bit Virtual-Memory Systems | Page 132
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0047** Added `12.3:132` — 0% similar</summary>

**New:**
```
Sv32: Page-Based 32-bit Virtual-Memory Systems | Page 134
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0048** Added `12.4` — 0% similar</summary>

**New:**
```
Sv39: Page-Based 39-bit Virtual-Memory System
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0049** Added `12.5` — 0% similar</summary>

**New:**
```
Sv48: Page-Based 48-bit Virtual-Memory System
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0050** Added `12.6` — 0% similar</summary>

**New:**
```
Sv57: Page-Based 57-bit Virtual-Memory System
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0051** Added `12.7` — 0% similar</summary>

**New:**
```
"Svnapot" Extension for NAPOT Translation Contiguity, Version 1.0
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0052** Added `12.7:137` — 0% similar</summary>

**New:**
```
"Svnapot" Extension for NAPOT Translation Contiguity, Version 1.0 | Page 139
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0053** Added `12.8` — 0% similar</summary>

**New:**
```
"Svpbmt" Extension for Page-Based Memory Types, Version 1.0
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0054** Added `12.9` — 0% similar</summary>

**New:**
```
"Svinval" Extension for Fine-Grained Address-Translation Cache
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0055** Added `12.9:140` — 0% similar</summary>

**New:**
```
"Svinval" Extension for Fine-Grained Address-Translation Cache Invalidation, Version 1.0 | Page 142
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0056** Added `14.1` — 0% similar</summary>

**New:**
```
Count Overflow Control
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0057** Added `14.2` — 0% similar</summary>

**New:**
```
Supervisor Count Overflow (scountovf) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0058** Added `15.1` — 0% similar</summary>

**New:**
```
Privilege Modes
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0059** Added `15.2` — 0% similar</summary>

**New:**
```
Hypervisor and Virtual Supervisor CSRs
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0060** Added `15.2.1` — 0% similar</summary>

**New:**
```
Hypervisor Status (hstatus) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0061** Added `15.2.11` — 0% similar</summary>

**New:**
```
Virtual Supervisor Status (vsstatus) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0062** Added `15.2.12` — 0% similar</summary>

**New:**
```
Virtual Supervisor Interrupt (vsip and vsie) Registers
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0063** Added `15.2.14` — 0% similar</summary>

**New:**
```
Virtual Supervisor Scratch (vsscratch) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0064** Added `15.2.18` — 0% similar</summary>

**New:**
```
Virtual Supervisor Address Translation and Protection (vsatp) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0065** Added `15.2.2` — 0% similar</summary>

**New:**
```
Hypervisor Trap Delegation (hedeleg and hideleg) Registers............................................................... 152
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0066** Added `15.2.2:149` — 0% similar</summary>

**New:**
```
Hypervisor Trap Delegation (hedeleg and hideleg) Registers
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0067** Added `15.2.3` — 0% similar</summary>

**New:**
```
Hypervisor Interrupt (hvip, hip, and hie) Registers
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0068** Added `15.2.4` — 0% similar</summary>

**New:**
```
Hypervisor Guest External Interrupt Registers (hgeip and hgeie)
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0069** Added `15.2.5` — 0% similar</summary>

**New:**
```
Hypervisor Environment Configuration Register (henvcfg)
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0070** Added `15.2.6` — 0% similar</summary>

**New:**
```
Hypervisor Counter-Enable (hcounteren) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0071** Added `15.2.8` — 0% similar</summary>

**New:**
```
Hypervisor Trap Value (htval) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0072** Added `15.2.9` — 0% similar</summary>

**New:**
```
Hypervisor Trap Instruction (htinst) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0073** Added `15.2:150` — 0% similar</summary>

**New:**
```
Hypervisor and Virtual Supervisor CSRs | Page 153
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0074** Added `15.2:152` — 0% similar</summary>

**New:**
```
Hypervisor and Virtual Supervisor CSRs | Page 155
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0075** Added `15.2:155` — 0% similar</summary>

**New:**
```
Hypervisor and Virtual Supervisor CSRs | Page 158
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0076** Added `15.2:160` — 0% similar</summary>

**New:**
```
Hypervisor and Virtual Supervisor CSRs | Page 163
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0077** Added `15.3` — 0% similar</summary>

**New:**
```
Hypervisor Instructions
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0078** Added `15.3.2` — 0% similar</summary>

**New:**
```
Hypervisor Memory-Management Fence Instructions
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0079** Added `15.4` — 0% similar</summary>

**New:**
```
Machine-Level CSRs
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0080** Added `15.4.2` — 0% similar</summary>

**New:**
```
Machine Interrupt Delegation (mideleg) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0081** Added `15.4.4` — 0% similar</summary>

**New:**
```
Machine Second Trap Value (mtval2) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0082** Added `15.4:167` — 0% similar</summary>

**New:**
```
Machine-Level CSRs | Page 170
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0083** Added `15.5` — 0% similar</summary>

**New:**
```
Two-Stage Address Translation
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0084** Added `15.5.2` — 0% similar</summary>

**New:**
```
Guest-Page Faults
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0085** Added `15.5.4` — 0% similar</summary>

**New:**
```
Interaction with Pointer Masking
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0086** Added `15.5:171` — 0% similar</summary>

**New:**
```
Two-Stage Address Translation | Page 174
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0087** Added `15.6` — 0% similar</summary>

**New:**
```
Traps
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0088** Added `15.6.2` — 0% similar</summary>

**New:**
```
Trap Entry
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0089** Added `15.6.3` — 0% similar</summary>

**New:**
```
Transformed Instruction or Pseudoinstruction for mtinst or htinst
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0090** Added `15.6.4` — 0% similar</summary>

**New:**
```
Trap Return
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0091** Added `15.6:175` — 0% similar</summary>

**New:**
```
Traps | Page 178
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0092** Added `15.6:176` — 0% similar</summary>

**New:**
```
Traps | Page 179
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0093** Added `15.6:179` — 0% similar</summary>

**New:**
```
Traps | Page 182
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0094** Added `15.6:180` — 0% similar</summary>

**New:**
```
Traps | Page 183
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0095** Added `15.6:181` — 0% similar</summary>

**New:**
```
Traps | Page 184
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0096** Added `15.6:183` — 0% similar</summary>

**New:**
```
Traps | Page 186
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0097** Added `16.1` — 0% similar</summary>

**New:**
```
Landing Pad (Zicfilp)
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0098** Added `16.1.2` — 0% similar</summary>

**New:**
```
Preserving Expected Landing Pad State on Traps
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0099** Added `16.2` — 0% similar</summary>

**New:**
```
Shadow Stack (Zicfiss)
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0100** Added `16.2.3` — 0% similar</summary>

**New:**
```
Shadow Stack Memory Protection
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0101** Added `16.2:188` — 0% similar</summary>

**New:**
```
Shadow Stack (Zicfiss) | Page 191
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0102** Added `16.2:189` — 0% similar</summary>

**New:**
```
Shadow Stack (Zicfiss) | Page 192
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0103** Added `18.1` — 0% similar</summary>

**New:**
```
Introduction......................................................................................................................................................................... 194
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0104** Added `18.1:190` — 0% similar</summary>

**New:**
```
Introduction
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0105** Added `18.2` — 0% similar</summary>

**New:**
```
Background | Page 198
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0106** Added `18.2.2` — 0% similar</summary>

**New:**
```
The “Ignore” Transformation
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0107** Added `18.2.3` — 0% similar</summary>

**New:**
```
Example
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0108** Added `18.2.5` — 0% similar</summary>

**New:**
```
Pointer Masking and Privilege Modes
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0109** Added `18.2.7` — 0% similar</summary>

**New:**
```
Pointer Masking Extensions
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0110** Added `18.2.8` — 0% similar</summary>

**New:**
```
Number of Masked Bits
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0111** Added `2.1` — 0% similar</summary>

**New:**
```
CSR Address Mapping Conventions
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0112** Added `2.1:11` — 0% similar</summary>

**New:**
```
CSR Address Mapping Conventions | Page 14
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0113** Added `2.1:12` — 0% similar</summary>

**New:**
```
CSR Address Mapping Conventions | Page 15
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0114** Added `2.2` — 0% similar</summary>

**New:**
```
CSR Listing
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0115** Added `2.2.2` — 0% similar</summary>

**New:**
```
Currently allocated RISC-V supervisor-level CSR addresses
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0116** Added `2.2.3` — 0% similar</summary>

**New:**
```
Currently allocated RISC-V hypervisor and VS CSR addresses
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0117** Added `2.2.4` — 0% similar</summary>

**New:**
```
Currently allocated RISC-V machine-level CSR addresses
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0118** Added `2.2.5` — 0% similar</summary>

**New:**
```
Currently allocated RISC-V indirect CSR (Smcsrind) mappings
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0119** Added `2.2:16` — 0% similar</summary>

**New:**
```
CSR Listing | Page 19
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0120** Added `2.2:18` — 0% similar</summary>

**New:**
```
CSR Listing | Page 21
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0121** Added `2.2:19` — 0% similar</summary>

**New:**
```
CSR Listing | Page 22
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0122** Added `2.3` — 0% similar</summary>

**New:**
```
CSR Field Specifications
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0123** Added `2.3.1` — 0% similar</summary>

**New:**
```
Reserved Writes Preserve Values, Reads Ignore Values (WPRI)
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0124** Added `2.3.2` — 0% similar</summary>

**New:**
```
Write/Read Only Legal Values (WLRL)
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0125** Added `2.3:23` — 0% similar</summary>

**New:**
```
CSR Field Specifications | Page 24
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0126** Added `2.5` — 0% similar</summary>

**New:**
```
Implicit Reads of CSRs
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0127** Added `20.1` — 0% similar</summary>

**New:**
```
Research Funding at UC Berkeley
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0128** Added `3.1` — 0% similar</summary>

**New:**
```
Machine-Level CSRs
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0129** Added `3.1.10` — 0% similar</summary>

**New:**
```
Hardware Performance Monitor
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0130** Added `3.1.12` — 0% similar</summary>

**New:**
```
Machine Counter-Inhibit (mcountinhibit) Register..................................................................................... 47
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0131** Added `3.1.12:46` — 0% similar</summary>

**New:**
```
Machine Counter-Inhibit (mcountinhibit) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0132** Added `3.1.14` — 0% similar</summary>

**New:**
```
Machine Exception Program Counter (mepc) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0133** Added `3.1.16` — 0% similar</summary>

**New:**
```
Machine Trap Value (mtval) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0134** Added `3.1.17` — 0% similar</summary>

**New:**
```
Machine Configuration Pointer (mconfigptr) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0135** Added `3.1.18` — 0% similar</summary>

**New:**
```
Machine Environment Configuration (menvcfg) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0136** Added `3.1.19` — 0% similar</summary>

**New:**
```
Machine Security Configuration (mseccfg) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0137** Added `3.1.2` — 0% similar</summary>

**New:**
```
Machine Vendor ID (mvendorid) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0138** Added `3.1.3` — 0% similar</summary>

**New:**
```
Machine Architecture ID (marchid) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0139** Added `3.1.5` — 0% similar</summary>

**New:**
```
Hart ID (mhartid) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0140** Added `3.1.6.2` — 0% similar</summary>

**New:**
```
Double Trap Control in mstatus Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0141** Added `3.1.6.3` — 0% similar</summary>

**New:**
```
Base ISA Control in mstatus Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0142** Added `3.1.6.5` — 0% similar</summary>

**New:**
```
Endianness Control in mstatus and mstatush Registers
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0143** Added `3.1.6.6` — 0% similar</summary>

**New:**
```
Virtualization Support in mstatus Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0144** Added `3.1.6.7` — 0% similar</summary>

**New:**
```
Extension Context Status in mstatus Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0145** Added `3.1.6.8` — 0% similar</summary>

**New:**
```
Previous Expected Landing Pad (ELP) State in mstatus Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0146** Added `3.1.8` — 0% similar</summary>

**New:**
```
Machine Trap Delegation (medeleg and mideleg) Registers
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0147** Added `3.1.9` — 0% similar</summary>

**New:**
```
Machine Interrupt (mip and mie) Registers
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0148** Added `3.1:27` — 0% similar</summary>

**New:**
```
Machine-Level CSRs | Page 28
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0149** Added `3.1:31` — 0% similar</summary>

**New:**
```
Machine-Level CSRs | Page 32
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0150** Added `3.1:37` — 0% similar</summary>

**New:**
```
Machine-Level CSRs | Page 38
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0151** Added `3.1:38` — 0% similar</summary>

**New:**
```
Machine-Level CSRs | Page 39
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0152** Added `3.1:39` — 0% similar</summary>

**New:**
```
Machine-Level CSRs | Page 40
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0153** Added `3.1:43` — 0% similar</summary>

**New:**
```
Machine-Level CSRs | Page 44
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0154** Added `3.1:44` — 0% similar</summary>

**New:**
```
Machine-Level CSRs | Page 45
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0155** Added `3.1:48` — 0% similar</summary>

**New:**
```
Machine-Level CSRs | Page 49
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0156** Added `3.1:49` — 0% similar</summary>

**New:**
```
Machine-Level CSRs | Page 50
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0157** Added `3.1:50` — 0% similar</summary>

**New:**
```
Machine-Level CSRs | Page 51
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0158** Added `3.1:54` — 0% similar</summary>

**New:**
```
Machine-Level CSRs | Page 55
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0159** Added `3.1:56` — 0% similar</summary>

**New:**
```
Machine-Level CSRs | Page 57
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0160** Added `3.1:57` — 0% similar</summary>

**New:**
```
Machine-Level CSRs | Page 58
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0161** Added `3.2` — 0% similar</summary>

**New:**
```
Machine-Level Memory-Mapped Registers
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0162** Added `3.3` — 0% similar</summary>

**New:**
```
Machine-Mode Privileged Instructions
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0163** Added `3.3.2` — 0% similar</summary>

**New:**
```
Trap-Return Instructions
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0164** Added `3.3.4` — 0% similar</summary>

**New:**
```
Custom SYSTEM Instructions
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0165** Added `3.5` — 0% similar</summary>

**New:**
```
Non-Maskable Interrupts
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0166** Added `3.6.1` — 0% similar</summary>

**New:**
```
Main Memory versus I/O Regions
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0167** Added `3.6.2` — 0% similar</summary>

**New:**
```
Supported Access Type PMAs
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0168** Added `3.6.3.2` — 0% similar</summary>

**New:**
```
Reservability PMA
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0169** Added `3.6.5` — 0% similar</summary>

**New:**
```
Memory-Ordering PMAs
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0170** Added `3.6.6` — 0% similar</summary>

**New:**
```
Coherence and Cacheability PMAs
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0171** Added `3.6.7` — 0% similar</summary>

**New:**
```
Idempotency PMAs
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0172** Added `3.7.1` — 0% similar</summary>

**New:**
```
Physical Memory Protection CSRs
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0173** Added `3.7.1.1` — 0% similar</summary>

**New:**
```
Address Matching
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0174** Added `3.7.1.2` — 0% similar</summary>

**New:**
```
Locking and Privilege Mode
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0175** Added `3.7.2` — 0% similar</summary>

**New:**
```
Physical Memory Protection and Paging
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0176** Added `4.1` — 0% similar</summary>

**New:**
```
State Enable Extensions
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0177** Added `4.1:74` — 0% similar</summary>

**New:**
```
State Enable Extensions | Page 75
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0178** Added `4.2` — 0% similar</summary>

**New:**
```
State Enable 0 Registers
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0179** Added `4.2:76` — 0% similar</summary>

**New:**
```
State Enable 0 Registers | Page 77
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0180** Added `4.3` — 0% similar</summary>

**New:**
```
Usage
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0181** Added `4.3:78` — 0% similar</summary>

**New:**
```
Usage | Page 79
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0182** Added `5.1` — 0% similar</summary>

**New:**
```
Introduction
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0183** Added `5.3` — 0% similar</summary>

**New:**
```
Supervisor-level CSRs
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0184** Added `5.4` — 0% similar</summary>

**New:**
```
Virtual Supervisor-level CSRs
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0185** Added `5.5` — 0% similar</summary>

**New:**
```
Access control by the state-enable CSRs
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0186** Added `5.5:83` — 0% similar</summary>

**New:**
```
Access control by the state-enable CSRs | Page 84
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0187** Added `6.1` — 0% similar</summary>

**New:**
```
Threat model........................................................................................................................................................................... 85
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0188** Added `6.1:84` — 0% similar</summary>

**New:**
```
Threat model
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0189** Added `6.2` — 0% similar</summary>

**New:**
```
Smepmp Physical Memory Protection Rules
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0190** Added `6.3` — 0% similar</summary>

**New:**
```
Smepmp software discovery
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0191** Added `7.1` — 0% similar</summary>

**New:**
```
Introduction
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0192** Added `7.3` — 0% similar</summary>

**New:**
```
Counter Behavior
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0193** Added `8.1` — 0% similar</summary>

**New:**
```
RNMI Interrupt Signals
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0194** Added `8.3` — 0% similar</summary>

**New:**
```
RNMI CSRs | Page 91
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0195** Added `8.4` — 0% similar</summary>

**New:**
```
MNRET Instruction
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0196** Added `9.1` — 0% similar</summary>

**New:**
```
Counter Delegation
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0197** Added `9.2` — 0% similar</summary>

**New:**
```
Supervisor Counter Inhibit (scountinhibit) Register
```

**Detail:** Added section

</details>

<details>
<summary>🟡 **CHG-0198** Added `9.4` — 0% similar</summary>

**New:**
```
Virtualizing Local-Counter-Overflow Interrupts
```

**Detail:** Added section

</details>

### Pages added (85)

<details>
<summary>🟡 **CHG-0633** Page added `Page 6` (p. 6) — 100% similar</summary>

**Page:** ? → 6

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0634** Page added `Page 7` (p. 7) — 100% similar</summary>

**Page:** ? → 7

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0635** Page added `Page 9` (p. 9) — 100% similar</summary>

**Page:** ? → 9

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0636** Page added `Page 12` (p. 12) — 100% similar</summary>

**Page:** ? → 12

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0637** Page added `Page 15` (p. 15) — 100% similar</summary>

**Page:** ? → 15

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0638** Page added `Page 16` (p. 16) — 100% similar</summary>

**Page:** ? → 16

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0639** Page added `Page 18` (p. 18) — 100% similar</summary>

**Page:** ? → 18

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0640** Page added `Page 19` (p. 19) — 100% similar</summary>

**Page:** ? → 19

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0641** Page added `Page 21` (p. 21) — 100% similar</summary>

**Page:** ? → 21

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0642** Page added `Page 26` (p. 26) — 100% similar</summary>

**Page:** ? → 26

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0643** Page added `Page 28` (p. 28) — 100% similar</summary>

**Page:** ? → 28

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0644** Page added `Page 29` (p. 29) — 100% similar</summary>

**Page:** ? → 29

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0645** Page added `Page 30` (p. 30) — 100% similar</summary>

**Page:** ? → 30

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0646** Page added `Page 31` (p. 31) — 100% similar</summary>

**Page:** ? → 31

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0647** Page added `Page 32` (p. 32) — 100% similar</summary>

**Page:** ? → 32

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0648** Page added `Page 35` (p. 35) — 100% similar</summary>

**Page:** ? → 35

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0649** Page added `Page 36` (p. 36) — 100% similar</summary>

**Page:** ? → 36

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0650** Page added `Page 37` (p. 37) — 100% similar</summary>

**Page:** ? → 37

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0651** Page added `Page 38` (p. 38) — 100% similar</summary>

**Page:** ? → 38

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0652** Page added `Page 43` (p. 43) — 100% similar</summary>

**Page:** ? → 43

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0653** Page added `Page 44` (p. 44) — 100% similar</summary>

**Page:** ? → 44

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0654** Page added `Page 45` (p. 45) — 100% similar</summary>

**Page:** ? → 45

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0655** Page added `Page 46` (p. 46) — 100% similar</summary>

**Page:** ? → 46

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0656** Page added `Page 49` (p. 49) — 100% similar</summary>

**Page:** ? → 49

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0657** Page added `Page 50` (p. 50) — 100% similar</summary>

**Page:** ? → 50

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0658** Page added `Page 51` (p. 51) — 100% similar</summary>

**Page:** ? → 51

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0659** Page added `Page 52` (p. 52) — 100% similar</summary>

**Page:** ? → 52

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0660** Page added `Page 53` (p. 53) — 100% similar</summary>

**Page:** ? → 53

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0661** Page added `Page 54` (p. 54) — 100% similar</summary>

**Page:** ? → 54

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0662** Page added `Page 62` (p. 62) — 100% similar</summary>

**Page:** ? → 62

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0663** Page added `Page 64` (p. 64) — 100% similar</summary>

**Page:** ? → 64

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0664** Page added `Page 65` (p. 65) — 100% similar</summary>

**Page:** ? → 65

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0665** Page added `Page 66` (p. 66) — 100% similar</summary>

**Page:** ? → 66

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0666** Page added `Page 67` (p. 67) — 100% similar</summary>

**Page:** ? → 67

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0667** Page added `Page 68` (p. 68) — 100% similar</summary>

**Page:** ? → 68

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0668** Page added `Page 70` (p. 70) — 100% similar</summary>

**Page:** ? → 70

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0669** Page added `Page 76` (p. 76) — 100% similar</summary>

**Page:** ? → 76

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0670** Page added `Page 77` (p. 77) — 100% similar</summary>

**Page:** ? → 77

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0671** Page added `Page 78` (p. 78) — 100% similar</summary>

**Page:** ? → 78

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0672** Page added `Page 79` (p. 79) — 100% similar</summary>

**Page:** ? → 79

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0673** Page added `Page 80` (p. 80) — 100% similar</summary>

**Page:** ? → 80

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0674** Page added `Page 86` (p. 86) — 100% similar</summary>

**Page:** ? → 86

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0675** Page added `Page 90` (p. 90) — 100% similar</summary>

**Page:** ? → 90

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0676** Page added `Page 92` (p. 92) — 100% similar</summary>

**Page:** ? → 92

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0677** Page added `Page 93` (p. 93) — 100% similar</summary>

**Page:** ? → 93

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0678** Page added `Page 108` (p. 108) — 100% similar</summary>

**Page:** ? → 108

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0679** Page added `Page 109` (p. 109) — 100% similar</summary>

**Page:** ? → 109

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0680** Page added `Page 111` (p. 111) — 100% similar</summary>

**Page:** ? → 111

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0681** Page added `Page 113` (p. 113) — 100% similar</summary>

**Page:** ? → 113

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0682** Page added `Page 117` (p. 117) — 100% similar</summary>

**Page:** ? → 117

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0683** Page added `Page 118` (p. 118) — 100% similar</summary>

**Page:** ? → 118

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0684** Page added `Page 121` (p. 121) — 100% similar</summary>

**Page:** ? → 121

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0685** Page added `Page 122` (p. 122) — 100% similar</summary>

**Page:** ? → 122

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0686** Page added `Page 123` (p. 123) — 100% similar</summary>

**Page:** ? → 123

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0687** Page added `Page 124` (p. 124) — 100% similar</summary>

**Page:** ? → 124

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0688** Page added `Page 125` (p. 125) — 100% similar</summary>

**Page:** ? → 125

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0689** Page added `Page 129` (p. 129) — 100% similar</summary>

**Page:** ? → 129

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0690** Page added `Page 130` (p. 130) — 100% similar</summary>

**Page:** ? → 130

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0691** Page added `Page 131` (p. 131) — 100% similar</summary>

**Page:** ? → 131

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0692** Page added `Page 133` (p. 133) — 100% similar</summary>

**Page:** ? → 133

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0693** Page added `Page 135` (p. 135) — 100% similar</summary>

**Page:** ? → 135

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0694** Page added `Page 136` (p. 136) — 100% similar</summary>

**Page:** ? → 136

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0695** Page added `Page 137` (p. 137) — 100% similar</summary>

**Page:** ? → 137

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0696** Page added `Page 138` (p. 138) — 100% similar</summary>

**Page:** ? → 138

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0697** Page added `Page 139` (p. 139) — 100% similar</summary>

**Page:** ? → 139

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0698** Page added `Page 140` (p. 140) — 100% similar</summary>

**Page:** ? → 140

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0699** Page added `Page 144` (p. 144) — 100% similar</summary>

**Page:** ? → 144

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0700** Page added `Page 145` (p. 145) — 100% similar</summary>

**Page:** ? → 145

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0701** Page added `Page 149` (p. 149) — 100% similar</summary>

**Page:** ? → 149

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0702** Page added `Page 150` (p. 150) — 100% similar</summary>

**Page:** ? → 150

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0703** Page added `Page 151` (p. 151) — 100% similar</summary>

**Page:** ? → 151

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0704** Page added `Page 159` (p. 159) — 100% similar</summary>

**Page:** ? → 159

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0705** Page added `Page 165` (p. 165) — 100% similar</summary>

**Page:** ? → 165

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0706** Page added `Page 166` (p. 166) — 100% similar</summary>

**Page:** ? → 166

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0707** Page added `Page 169` (p. 169) — 100% similar</summary>

**Page:** ? → 169

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0708** Page added `Page 174` (p. 174) — 100% similar</summary>

**Page:** ? → 174

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0709** Page added `Page 176` (p. 176) — 100% similar</summary>

**Page:** ? → 176

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0710** Page added `Page 181` (p. 181) — 100% similar</summary>

**Page:** ? → 181

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0711** Page added `Page 182` (p. 182) — 100% similar</summary>

**Page:** ? → 182

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0712** Page added `Page 200` (p. 200) — 100% similar</summary>

**Page:** ? → 200

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0713** Page added `Page 205` (p. 205) — 100% similar</summary>

**Page:** ? → 205

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0714** Page added `Page 206` (p. 206) — 100% similar</summary>

**Page:** ? → 206

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0715** Page added `Page 207` (p. 207) — 100% similar</summary>

**Page:** ? → 207

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0716** Page added `Page 208` (p. 208) — 100% similar</summary>

**Page:** ? → 208

**Detail:** Added page

</details>

<details>
<summary>🟡 **CHG-0717** Page added `Page 211` (p. 211) — 100% similar</summary>

**Page:** ? → 211

**Detail:** Added page

</details>

### Pages removed (93)

<details>
<summary>🟡 **CHG-0540** Page removed `Page 6` (p. 6) — 100% similar</summary>

**Page:** 6 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0541** Page removed `Page 7` (p. 7) — 100% similar</summary>

**Page:** 7 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0542** Page removed `Page 11` (p. 11) — 100% similar</summary>

**Page:** 11 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0543** Page removed `Page 14` (p. 14) — 100% similar</summary>

**Page:** 14 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0544** Page removed `Page 15` (p. 15) — 100% similar</summary>

**Page:** 15 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0545** Page removed `Page 17` (p. 17) — 100% similar</summary>

**Page:** 17 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0546** Page removed `Page 18` (p. 18) — 100% similar</summary>

**Page:** 18 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0547** Page removed `Page 20` (p. 20) — 100% similar</summary>

**Page:** 20 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0548** Page removed `Page 26` (p. 26) — 100% similar</summary>

**Page:** 26 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0549** Page removed `Page 27` (p. 27) — 100% similar</summary>

**Page:** 27 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0550** Page removed `Page 28` (p. 28) — 100% similar</summary>

**Page:** 28 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0551** Page removed `Page 30` (p. 30) — 100% similar</summary>

**Page:** 30 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0552** Page removed `Page 32` (p. 32) — 100% similar</summary>

**Page:** 32 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0553** Page removed `Page 33` (p. 33) — 100% similar</summary>

**Page:** 33 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0554** Page removed `Page 34` (p. 34) — 100% similar</summary>

**Page:** 34 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0555** Page removed `Page 35` (p. 35) — 100% similar</summary>

**Page:** 35 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0556** Page removed `Page 36` (p. 36) — 100% similar</summary>

**Page:** 36 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0557** Page removed `Page 41` (p. 41) — 100% similar</summary>

**Page:** 41 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0558** Page removed `Page 42` (p. 42) — 100% similar</summary>

**Page:** 42 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0559** Page removed `Page 43` (p. 43) — 100% similar</summary>

**Page:** 43 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0560** Page removed `Page 44` (p. 44) — 100% similar</summary>

**Page:** 44 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0561** Page removed `Page 47` (p. 47) — 100% similar</summary>

**Page:** 47 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0562** Page removed `Page 48` (p. 48) — 100% similar</summary>

**Page:** 48 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0563** Page removed `Page 49` (p. 49) — 100% similar</summary>

**Page:** 49 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0564** Page removed `Page 50` (p. 50) — 100% similar</summary>

**Page:** 50 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0565** Page removed `Page 51` (p. 51) — 100% similar</summary>

**Page:** 51 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0566** Page removed `Page 52` (p. 52) — 100% similar</summary>

**Page:** 52 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0567** Page removed `Page 53` (p. 53) — 100% similar</summary>

**Page:** 53 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0568** Page removed `Page 61` (p. 61) — 100% similar</summary>

**Page:** 61 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0569** Page removed `Page 62` (p. 62) — 100% similar</summary>

**Page:** 62 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0570** Page removed `Page 63` (p. 63) — 100% similar</summary>

**Page:** 63 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0571** Page removed `Page 64` (p. 64) — 100% similar</summary>

**Page:** 64 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0572** Page removed `Page 65` (p. 65) — 100% similar</summary>

**Page:** 65 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0573** Page removed `Page 67` (p. 67) — 100% similar</summary>

**Page:** 67 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0574** Page removed `Page 73` (p. 73) — 100% similar</summary>

**Page:** 73 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0575** Page removed `Page 74` (p. 74) — 100% similar</summary>

**Page:** 74 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0576** Page removed `Page 75` (p. 75) — 100% similar</summary>

**Page:** 75 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0577** Page removed `Page 76` (p. 76) — 100% similar</summary>

**Page:** 76 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0578** Page removed `Page 77` (p. 77) — 100% similar</summary>

**Page:** 77 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0579** Page removed `Page 78` (p. 78) — 100% similar</summary>

**Page:** 78 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0580** Page removed `Page 84` (p. 84) — 100% similar</summary>

**Page:** 84 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0581** Page removed `Page 88` (p. 88) — 100% similar</summary>

**Page:** 88 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0582** Page removed `Page 90` (p. 90) — 100% similar</summary>

**Page:** 90 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0583** Page removed `Page 91` (p. 91) — 100% similar</summary>

**Page:** 91 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0584** Page removed `Page 92` (p. 92) — 100% similar</summary>

**Page:** 92 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0585** Page removed `Page 94` (p. 94) — 100% similar</summary>

**Page:** 94 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0586** Page removed `Page 110` (p. 110) — 100% similar</summary>

**Page:** 110 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0587** Page removed `Page 111` (p. 111) — 100% similar</summary>

**Page:** 111 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0588** Page removed `Page 112` (p. 112) — 100% similar</summary>

**Page:** 112 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0589** Page removed `Page 114` (p. 114) — 100% similar</summary>

**Page:** 114 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0590** Page removed `Page 116` (p. 116) — 100% similar</summary>

**Page:** 116 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0591** Page removed `Page 118` (p. 118) — 100% similar</summary>

**Page:** 118 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0592** Page removed `Page 121` (p. 121) — 100% similar</summary>

**Page:** 121 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0593** Page removed `Page 122` (p. 122) — 100% similar</summary>

**Page:** 122 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0594** Page removed `Page 125` (p. 125) — 100% similar</summary>

**Page:** 125 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0595** Page removed `Page 126` (p. 126) — 100% similar</summary>

**Page:** 126 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0596** Page removed `Page 127` (p. 127) — 100% similar</summary>

**Page:** 127 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0597** Page removed `Page 128` (p. 128) — 100% similar</summary>

**Page:** 128 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0598** Page removed `Page 129` (p. 129) — 100% similar</summary>

**Page:** 129 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0599** Page removed `Page 133` (p. 133) — 100% similar</summary>

**Page:** 133 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0600** Page removed `Page 134` (p. 134) — 100% similar</summary>

**Page:** 134 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0601** Page removed `Page 135` (p. 135) — 100% similar</summary>

**Page:** 135 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0602** Page removed `Page 137` (p. 137) — 100% similar</summary>

**Page:** 137 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0603** Page removed `Page 139` (p. 139) — 100% similar</summary>

**Page:** 139 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0604** Page removed `Page 140` (p. 140) — 100% similar</summary>

**Page:** 140 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0605** Page removed `Page 141` (p. 141) — 100% similar</summary>

**Page:** 141 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0606** Page removed `Page 142` (p. 142) — 100% similar</summary>

**Page:** 142 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0607** Page removed `Page 143` (p. 143) — 100% similar</summary>

**Page:** 143 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0608** Page removed `Page 144` (p. 144) — 100% similar</summary>

**Page:** 144 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0609** Page removed `Page 148` (p. 148) — 100% similar</summary>

**Page:** 148 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0610** Page removed `Page 149` (p. 149) — 100% similar</summary>

**Page:** 149 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0611** Page removed `Page 150` (p. 150) — 100% similar</summary>

**Page:** 150 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0612** Page removed `Page 154` (p. 154) — 100% similar</summary>

**Page:** 154 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0613** Page removed `Page 155` (p. 155) — 100% similar</summary>

**Page:** 155 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0614** Page removed `Page 156` (p. 156) — 100% similar</summary>

**Page:** 156 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0615** Page removed `Page 157` (p. 157) — 100% similar</summary>

**Page:** 157 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0616** Page removed `Page 158` (p. 158) — 100% similar</summary>

**Page:** 158 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0617** Page removed `Page 161` (p. 161) — 100% similar</summary>

**Page:** 161 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0618** Page removed `Page 162` (p. 162) — 100% similar</summary>

**Page:** 162 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0619** Page removed `Page 168` (p. 168) — 100% similar</summary>

**Page:** 168 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0620** Page removed `Page 176` (p. 176) — 100% similar</summary>

**Page:** 176 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0621** Page removed `Page 179` (p. 179) — 100% similar</summary>

**Page:** 179 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0622** Page removed `Page 184` (p. 184) — 100% similar</summary>

**Page:** 184 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0623** Page removed `Page 189` (p. 189) — 100% similar</summary>

**Page:** 189 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0624** Page removed `Page 190` (p. 190) — 100% similar</summary>

**Page:** 190 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0625** Page removed `Page 208` (p. 208) — 100% similar</summary>

**Page:** 208 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0626** Page removed `Page 213` (p. 213) — 100% similar</summary>

**Page:** 213 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0627** Page removed `Page 214` (p. 214) — 100% similar</summary>

**Page:** 214 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0628** Page removed `Page 215` (p. 215) — 100% similar</summary>

**Page:** 215 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0629** Page removed `Page 216` (p. 216) — 100% similar</summary>

**Page:** 216 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0630** Page removed `Page 217` (p. 217) — 100% similar</summary>

**Page:** 217 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0631** Page removed `Page 218` (p. 218) — 100% similar</summary>

**Page:** 218 → ?

**Detail:** Removed page

</details>

<details>
<summary>🟡 **CHG-0632** Page removed `Page 221` (p. 221) — 100% similar</summary>

**Page:** 221 → ?

**Detail:** Removed page

</details>

## 🔵 Relocations

### Moved tables (163)

<details>
<summary>🔵 **CHG-0322** Table moved `0 | 1 | 2` (p. 11) — 100% similar</summary>

**Page:** 10 → 11

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0420** Table moved `0 | 1 | 2` (p. 11) — 100% similar</summary>

**Page:** 10 → 11

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0363** Table moved `0 | 1 | 2` (p. 13) — 100% similar</summary>

**Page:** 12 → 13

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0393** Table moved `0 | 1 | 2` (p. 14) — 100% similar</summary>

**Page:** 13 → 14

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0347** Table moved `0 | 1 | 2 | 3` (p. 18) — 100% similar</summary>

**Page:** 17 → 18

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0344** Table moved `0 | 1 | 2` (p. 19) — 100% similar</summary>

**Page:** 18 → 19

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0301** Table moved `0 | 1` (p. 34) — 100% similar</summary>

**Page:** 31 → 34

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0348** Table moved `0 | 1 | 2` (p. 35) — 100% similar</summary>

**Page:** 33 → 35

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0368** Table moved `0 | 1 | 2` (p. 44) — 100% similar</summary>

**Page:** 43 → 44

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0325** Table moved `0 | 1 | 2 | 3` (p. 47) — 100% similar</summary>

**Page:** 45 → 47

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0398** Table moved `0 | 1 | 2 | 3` (p. 47) — 100% similar</summary>

**Page:** 45 → 47

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0435** Table moved `0 | 1 | 2 | 3` (p. 47) — 100% similar</summary>

**Page:** 45 → 47

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0371** Table moved `0 | 1 | 2` (p. 48) — 100% similar</summary>

**Page:** 47 → 48

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0340** Table moved `0 | 1 | 2` (p. 57) — 100% similar</summary>

**Page:** 56 → 57

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0324** Table moved `0 | 1 | 2` (p. 58) — 100% similar</summary>

**Page:** 57 → 58

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0319** Table moved `0 | 1` (p. 61) — 100% similar</summary>

**Page:** 60 → 61

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0315** Table moved `0 | 1 | 2 | 3` (p. 64) — 100% similar</summary>

**Page:** 62 → 64

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0353** Table moved `0 | 1` (p. 64) — 100% similar</summary>

**Page:** 60 → 64

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0374** Table moved `0 | 1` (p. 73) — 100% similar</summary>

**Page:** 70 → 73

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0294** Table moved `0 | 1 | 2` (p. 78) — 100% similar</summary>

**Page:** 76 → 78

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0297** Table moved `0 | 1 | 2` (p. 78) — 100% similar</summary>

**Page:** 76 → 78

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0289** Table moved `0 | 1 | 2 | 3` (p. 83) — 100% similar</summary>

**Page:** 81 → 83

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0290** Table moved `0 | 1 | 2 | 3` (p. 83) — 100% similar</summary>

**Page:** 82 → 83

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0335** Table moved `0 | 1 | 2 | 3` (p. 83) — 100% similar</summary>

**Page:** 81 → 83

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0431** Table moved `0 | 1 | 2 | 3` (p. 83) — 100% similar</summary>

**Page:** 82 → 83

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0291** Table moved `0 | 1 | 2 | 3` (p. 84) — 100% similar</summary>

**Page:** 82 → 84

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0394** Table moved `0 | 1 | 2 | 3` (p. 87) — 100% similar</summary>

**Page:** 85 → 87

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0417** Table moved `0 | 1 | 2 | 3` (p. 89) — 100% similar</summary>

**Page:** 88 → 89

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0323** Table moved `0 | 1` (p. 95) — 100% similar</summary>

**Page:** 97 → 95

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0418** Table moved `0 | 1 | 2 | 3` (p. 95) — 100% similar</summary>

**Page:** 97 → 95

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0366** Table moved `0 | 1` (p. 98) — 100% similar</summary>

**Page:** 100 → 98

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0379** Table moved `0 | 1 | 2 | 3` (p. 98) — 100% similar</summary>

**Page:** 100 → 98

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0316** Table moved `0 | 1 | 2 | 3` (p. 105) — 100% similar</summary>

**Page:** 107 → 105

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0364** Table moved `0 | 1 | 2 | 3` (p. 105) — 100% similar</summary>

**Page:** 107 → 105

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0375** Table moved `0 | 1 | 2 | 3` (p. 105) — 100% similar</summary>

**Page:** 107 → 105

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0377** Table moved `0 | 1` (p. 105) — 100% similar</summary>

**Page:** 107 → 105

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0448** Table moved `0 | 1 | 2 | 3` (p. 105) — 100% similar</summary>

**Page:** 107 → 105

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0317** Table moved `0 | 1 | 2 | 3` (p. 106) — 100% similar</summary>

**Page:** 108 → 106

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0369** Table moved `0 | 1 | 2 | 3` (p. 106) — 100% similar</summary>

**Page:** 108 → 106

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0378** Table moved `0 | 1` (p. 106) — 100% similar</summary>

**Page:** 108 → 106

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0383** Table moved `0 | 1 | 2 | 3` (p. 106) — 100% similar</summary>

**Page:** 108 → 106

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0449** Table moved `0 | 1 | 2 | 3` (p. 106) — 100% similar</summary>

**Page:** 108 → 106

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0339** Table moved `0 | 1` (p. 107) — 100% similar</summary>

**Page:** 109 → 107

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0350** Table moved `0 | 1` (p. 107) — 100% similar</summary>

**Page:** 109 → 107

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0311** Table moved `0 | 1` (p. 108) — 100% similar</summary>

**Page:** 110 → 108

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0328** Table moved `0 | 1` (p. 108) — 100% similar</summary>

**Page:** 110 → 108

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0288** Table moved `0 | 1` (p. 109) — 100% similar</summary>

**Page:** 112 → 109

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0343** Table moved `0 | 1` (p. 109) — 100% similar</summary>

**Page:** 112 → 109

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0351** Table moved `0 | 1 | 2 | 3` (p. 110) — 100% similar</summary>

**Page:** 112 → 110

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0450** Table moved `0 | 1 | 2 | 3` (p. 110) — 100% similar</summary>

**Page:** 113 → 110

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0303** Table moved `0 | 1 | 2` (p. 113) — 100% similar</summary>

**Page:** 116 → 113

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0359** Table moved `0 | 1` (p. 114) — 100% similar</summary>

**Page:** 118 → 114

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0357** Table moved `0 | 1` (p. 115) — 100% similar</summary>

**Page:** 119 → 115

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0304** Table moved `0 | 1 | 2` (p. 116) — 100% similar</summary>

**Page:** 120 → 116

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0295** Table moved `0 | 1 | 2 | 3` (p. 119) — 100% similar</summary>

**Page:** 123 → 119

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0312** Table moved `0 | 1` (p. 119) — 100% similar</summary>

**Page:** 123 → 119

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0385** Table moved `0 | 1 | 2 | 3` (p. 119) — 100% similar</summary>

**Page:** 123 → 119

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0421** Table moved `0 | 1 | 2 | 3` (p. 119) — 100% similar</summary>

**Page:** 123 → 119

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0422** Table moved `0 | 1 | 2 | 3` (p. 119) — 100% similar</summary>

**Page:** 123 → 119

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0445** Table moved `0 | 1` (p. 119) — 100% similar</summary>

**Page:** 36 → 119

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0292** Table moved `0 | 1` (p. 122) — 100% similar</summary>

**Page:** 127 → 122

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0426** Table moved `0 | 1 | 2` (p. 122) — 100% similar</summary>

**Page:** 127 → 122

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0391** Table moved `0 | 1 | 2 | 3` (p. 123) — 100% similar</summary>

**Page:** 128 → 123

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0409** Table moved `0 | 1 | 2 | 3` (p. 124) — 100% similar</summary>

**Page:** 128 → 124

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0411** Table moved `0 | 1 | 2 | 3` (p. 125) — 100% similar</summary>

**Page:** 52 → 125

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0307** Table moved `0 | 1` (p. 126) — 100% similar</summary>

**Page:** 54 → 126

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0354** Table moved `0 | 1` (p. 128) — 100% similar</summary>

**Page:** 62 → 128

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0413** Table moved `0 | 1 | 2 | 3` (p. 128) — 100% similar</summary>

**Page:** 60 → 128

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0414** Table moved `0 | 1 | 2 | 3` (p. 128) — 100% similar</summary>

**Page:** 132 → 128

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0320** Table moved `0 | 1` (p. 129) — 100% similar</summary>

**Page:** 133 → 129

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0427** Table moved `0 | 1 | 2` (p. 130) — 100% similar</summary>

**Page:** 134 → 130

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0428** Table moved `0 | 1 | 2` (p. 131) — 100% similar</summary>

**Page:** 134 → 131

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0358** Table moved `0 | 1 | 2` (p. 132) — 100% similar</summary>

**Page:** 136 → 132

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0437** Table moved `0 | 1 | 2 | 3` (p. 133) — 100% similar</summary>

**Page:** 137 → 133

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0309** Table moved `0 | 1 | 2 | 3` (p. 137) — 100% similar</summary>

**Page:** 141 → 137

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0332** Table moved `0 | 1 | 2` (p. 137) — 100% similar</summary>

**Page:** 140 → 137

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0360** Table moved `0 | 1 | 2` (p. 137) — 100% similar</summary>

**Page:** 141 → 137

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0361** Table moved `0 | 1 | 2 | 3` (p. 137) — 100% similar</summary>

**Page:** 141 → 137

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0310** Table moved `0 | 1 | 2 | 3` (p. 142) — 100% similar</summary>

**Page:** 147 → 142

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0346** Table moved `0 | 1 | 2 | 3` (p. 142) — 100% similar</summary>

**Page:** 147 → 142

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0400** Table moved `0 | 1 | 2 | 3` (p. 142) — 100% similar</summary>

**Page:** 146 → 142

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0334** Table moved `0 | 1 | 2 | 3` (p. 143) — 100% similar</summary>

**Page:** 148 → 143

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0404** Table moved `0 | 1 | 2 | 3` (p. 143) — 100% similar</summary>

**Page:** 148 → 143

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0341** Table moved `0 | 1 | 2 | 3` (p. 144) — 100% similar</summary>

**Page:** 149 → 144

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0345** Table moved `0 | 1 | 2 | 3` (p. 144) — 100% similar</summary>

**Page:** 149 → 144

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0356** Table moved `0 | 1 | 2 | 3` (p. 144) — 100% similar</summary>

**Page:** 149 → 144

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0381** Table moved `0 | 1 | 2 | 3` (p. 144) — 100% similar</summary>

**Page:** 148 → 144

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0447** Table moved `0 | 1 | 2 | 3` (p. 144) — 100% similar</summary>

**Page:** 149 → 144

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0365** Table moved `0 | 1 | 2` (p. 147) — 100% similar</summary>

**Page:** 152 → 147

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0438** Table moved `0 | 1 | 2 | 3` (p. 148) — 100% similar</summary>

**Page:** 154 → 148

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0439** Table moved `0 | 1 | 2 | 3` (p. 148) — 100% similar</summary>

**Page:** 154 → 148

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0440** Table moved `0 | 1 | 2 | 3` (p. 149) — 100% similar</summary>

**Page:** 154 → 149

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0441** Table moved `0 | 1 | 2 | 3` (p. 149) — 100% similar</summary>

**Page:** 154 → 149

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0442** Table moved `0 | 1 | 2 | 3` (p. 149) — 100% similar</summary>

**Page:** 154 → 149

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0302** Table moved `0 | 1` (p. 154) — 100% similar</summary>

**Page:** 163 → 154

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0419** Table moved `0 | 1 | 2 | 3` (p. 154) — 100% similar</summary>

**Page:** 163 → 154

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0408** Table moved `0 | 1 | 2 | 3` (p. 157) — 100% similar</summary>

**Page:** 166 → 157

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0318** Table moved `0 | 1` (p. 158) — 100% similar</summary>

**Page:** 167 → 158

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0336** Table moved `0 | 1` (p. 158) — 100% similar</summary>

**Page:** 167 → 158

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0337** Table moved `0 | 1 | 2 | 3` (p. 158) — 100% similar</summary>

**Page:** 167 → 158

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0338** Table moved `0 | 1 | 2 | 3` (p. 158) — 100% similar</summary>

**Page:** 167 → 158

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0396** Table moved `0 | 1 | 2 | 3` (p. 158) — 100% similar</summary>

**Page:** 167 → 158

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0397** Table moved `0 | 1 | 2 | 3` (p. 158) — 100% similar</summary>

**Page:** 167 → 158

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0390** Table moved `0 | 1 | 2 | 3` (p. 161) — 100% similar</summary>

**Page:** 170 → 161

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0402** Table moved `0 | 1 | 2` (p. 161) — 100% similar</summary>

**Page:** 170 → 161

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0314** Table moved `0 | 1 | 2 | 3` (p. 162) — 100% similar</summary>

**Page:** 171 → 162

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0406** Table moved `0 | 1 | 2 | 3` (p. 162) — 100% similar</summary>

**Page:** 171 → 162

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0380** Table moved `0 | 1` (p. 163) — 100% similar</summary>

**Page:** 172 → 163

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0407** Table moved `0 | 1` (p. 163) — 100% similar</summary>

**Page:** 172 → 163

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0321** Table moved `0 | 1` (p. 164) — 100% similar</summary>

**Page:** 173 → 164

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0355** Table moved `0 | 1` (p. 164) — 100% similar</summary>

**Page:** 132 → 164

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0376** Table moved `0 | 1 | 2 | 3` (p. 164) — 100% similar</summary>

**Page:** 173 → 164

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0415** Table moved `0 | 1 | 2 | 3` (p. 164) — 100% similar</summary>

**Page:** 133 → 164

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0412** Table moved `0 | 1 | 2 | 3` (p. 166) — 100% similar</summary>

**Page:** 129 → 166

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0293** Table moved `0 | 1 | 2 | 3` (p. 168) — 100% similar</summary>

**Page:** 177 → 168

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0399** Table moved `0 | 1 | 2 | 3` (p. 168) — 100% similar</summary>

**Page:** 176 → 168

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0386** Table moved `0 | 1 | 2 | 3` (p. 169) — 100% similar</summary>

**Page:** 178 → 169

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0423** Table moved `0 | 1 | 2 | 3` (p. 169) — 100% similar</summary>

**Page:** 178 → 169

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0425** Table moved `0 | 1 | 2` (p. 169) — 100% similar</summary>

**Page:** 177 → 169

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0296** Table moved `0 | 1 | 2 | 3` (p. 170) — 100% similar</summary>

**Page:** 178 → 170

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0313** Table moved `0 | 1` (p. 170) — 100% similar</summary>

**Page:** 178 → 170

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0424** Table moved `0 | 1 | 2 | 3` (p. 170) — 100% similar</summary>

**Page:** 178 → 170

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0446** Table moved `0 | 1` (p. 170) — 100% similar</summary>

**Page:** 123 → 170

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0392** Table moved `0 | 1 | 2 | 3` (p. 171) — 100% similar</summary>

**Page:** 180 → 171

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0410** Table moved `0 | 1 | 2 | 3` (p. 171) — 100% similar</summary>

**Page:** 180 → 171

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0308** Table moved `0 | 1` (p. 172) — 100% similar</summary>

**Page:** 130 → 172

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0326** Table moved `0 | 1` (p. 172) — 100% similar</summary>

**Page:** 180 → 172

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0429** Table moved `0 | 1 | 2` (p. 173) — 100% similar</summary>

**Page:** 182 → 173

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0430** Table moved `0 | 1 | 2` (p. 173) — 100% similar</summary>

**Page:** 182 → 173

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0443** Table moved `0 | 1 | 2 | 3` (p. 174) — 100% similar</summary>

**Page:** 182 → 174

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0444** Table moved `0 | 1 | 2 | 3` (p. 175) — 100% similar</summary>

**Page:** 183 → 175

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0403** Table moved `0 | 1 | 2 | 3` (p. 177) — 100% similar</summary>

**Page:** 185 → 177

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0433** Table moved `0 | 1 | 2 | 3` (p. 177) — 100% similar</summary>

**Page:** 185 → 177

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0367** Table moved `0 | 1 | 2 | 3` (p. 178) — 100% similar</summary>

**Page:** 186 → 178

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0372** Table moved `0 | 1 | 2 | 3` (p. 178) — 100% similar</summary>

**Page:** 187 → 178

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0305** Table moved `0 | 1 | 2 | 3` (p. 179) — 100% similar</summary>

**Page:** 187 → 179

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0333** Table moved `0 | 1 | 2` (p. 180) — 100% similar</summary>

**Page:** 189 → 180

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0342** Table moved `0 | 1 | 2 | 3` (p. 181) — 100% similar</summary>

**Page:** 189 → 181

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0401** Table moved `0 | 1 | 2 | 3` (p. 181) — 100% similar</summary>

**Page:** 189 → 181

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0405** Table moved `0 | 1 | 2 | 3` (p. 181) — 100% similar</summary>

**Page:** 189 → 181

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0331** Table moved `0 | 1 | 2` (p. 187) — 100% similar</summary>

**Page:** 195 → 187

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0436** Table moved `0 | 1 | 2` (p. 187) — 100% similar</summary>

**Page:** 195 → 187

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0352** Table moved `0 | 1` (p. 188) — 100% similar</summary>

**Page:** 196 → 188

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0432** Table moved `0 | 1 | 2` (p. 188) — 100% similar</summary>

**Page:** 196 → 188

**Preview:** 0 | 1 | 2

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0298** Table moved `0 | 1 | 2 | 3` (p. 190) — 100% similar</summary>

**Page:** 198 → 190

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0388** Table moved `0 | 1 | 2 | 3` (p. 190) — 100% similar</summary>

**Page:** 198 → 190

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0373** Table moved `0 | 1` (p. 191) — 100% similar</summary>

**Page:** 199 → 191

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0384** Table moved `0 | 1 | 2 | 3` (p. 191) — 100% similar</summary>

**Page:** 199 → 191

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0395** Table moved `0 | 1 | 2 | 3` (p. 191) — 100% similar</summary>

**Page:** 199 → 191

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0299** Table moved `0 | 1` (p. 192) — 100% similar</summary>

**Page:** 200 → 192

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0416** Table moved `0 | 1` (p. 192) — 100% similar</summary>

**Page:** 200 → 192

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0306** Table moved `0 | 1` (p. 194) — 100% similar</summary>

**Page:** 202 → 194

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0370** Table moved `0 | 1` (p. 194) — 100% similar</summary>

**Page:** 202 → 194

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0434** Table moved `0 | 1` (p. 196) — 100% similar</summary>

**Page:** 204 → 196

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0300** Table moved `0 | 1` (p. 203) — 100% similar</summary>

**Page:** 211 → 203

**Preview:** 0 | 1

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0327** Table moved `0 | 1 | 2 | 3` (p. 209) — 100% similar</summary>

**Page:** 219 → 209

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0329** Table moved `0 | 1 | 2 | 3` (p. 209) — 100% similar</summary>

**Page:** 219 → 209

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0330** Table moved `0 | 1 | 2 | 3` (p. 209) — 100% similar</summary>

**Page:** 219 → 209

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0349** Table moved `0 | 1 | 2 | 3` (p. 209) — 100% similar</summary>

**Page:** 219 → 209

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0362** Table moved `0 | 1 | 2 | 3` (p. 209) — 100% similar</summary>

**Page:** 219 → 209

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0382** Table moved `0 | 1 | 2 | 3` (p. 209) — 100% similar</summary>

**Page:** 219 → 209

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0387** Table moved `0 | 1 | 2 | 3` (p. 209) — 100% similar</summary>

**Page:** 219 → 209

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

<details>
<summary>🔵 **CHG-0389** Table moved `0 | 1 | 2 | 3` (p. 209) — 100% similar</summary>

**Page:** 219 → 209

**Preview:** 0 | 1 | 2 | 3

**Detail:** Content unchanged

</details>

### Page shifts (1)

<details>
<summary>🔵 **CHG-0531** Structural page shift detected `Structural page shift` (p. 167–203) — 100% similar</summary>

**Page:** 175–211 → 167–203

**Detail:** Structural page shift detected. Pages 175–211 were renumbered by -8. Content was matched successfully.

</details>

## ⚪ Metadata

### Title (1)

<details>
<summary>⚪ **CHG-0001** Modified `title` — 99% similar</summary>

**Old:**
```
The RISC-V Instruction Set Manual: Volume II: Privileged Architecture
```

**New:**
```
The RISC-V Instruction Set Manual, Volume II: Privileged Architecture
```

**Detail:** Metadata field changed: title

</details>
