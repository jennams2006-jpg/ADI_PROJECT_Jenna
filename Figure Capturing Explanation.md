# Why Figures Are Not Essential for VPlan Generation

This document explains why the high-risk figure extraction feature is not required for generating verification plans from the **AMBA AXI** and **RISC-V ISA** specifications.

## Evidence from the Specifications

### AMBA AXI

- **VALID/READY handshake:** The timing diagrams are accompanied by text that explicitly defines the handshake rules, including when transfers occur, signal stability requirements, and protocol dependencies. The diagrams simply illustrate behaviour already specified in the text.

- **Burst transactions:** Read/write burst waveforms are supported by textual descriptions covering burst types, transfer ordering, burst lengths, and response rules. The text defines all legal protocol behaviour, while the figures provide representative examples.

### RISC-V ISA

- **Instruction format diagrams:** Diagrams showing fields such as `opcode`, `rd`, `rs1`, `rs2`, and `funct3` duplicate information contained in the instruction encoding tables and accompanying descriptions, which provide all information required for extraction.

- **CSR layouts and register diagrams:** Register diagrams are supported by tables and descriptive text defining each field's encoding, purpose, and behaviour. The architectural requirements can be extracted directly from the textual definitions.

## Key Observations

- **The extracted OCR text provides sufficient context** to capture protocol behaviour, requirements, and architectural semantics without relying on figures.

- **Normative requirements are defined in text and tables.** Protocol rules, instruction semantics, encodings, signal definitions, and constraints are specified in textual descriptions and structured tables rather than in figures.

- **Figures are illustrative, not normative.** Timing diagrams, register layouts, and architecture diagrams reinforce the accompanying text by showing examples or visual layouts but do not introduce additional verification requirements.

- **Tables provide structured information** that can be directly extracted for VPlan generation, including signal definitions, instruction encodings, register fields, protocol attributes, and response codes.

- **Figure processing increases complexity with limited benefit.** Extracting information from figures requires OCR and diagram interpretation, while the same information is already available in nearby text and tables.

## Conclusion

For both the **AMBA AXI** and **RISC-V ISA** specifications, a **text-first extraction approach** captures the information required for VPlan generation. Figures improve human understanding by illustrating examples and layouts but are generally **not required** for extracting verification requirements because the normative content is already defined in the accompanying text and tables.
