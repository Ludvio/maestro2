# 🛡️ RED TEAM STRATEGY: [PHASE_NAME] ([PHASE_ID])

> **Objective**: Identify state corruption vectors and logic violations.
> **Standard**: Adversarial Testing (Layer F).

## 1. Attack Vectors (Theory)
- **Vector A: Double-Spend / Race Condition**
  - Describe how concurrent requests might bypass validation.
- **Vector B: State Injection**
  - Malformed payload that might break types or invariants.
- **Vector C: Clock Drift (Sync Only)**
  - Manipulating Lamport clocks to overwrite legitimate state.

## 2. Invariants (The Shields)
List the rules that MUST NOT be broken:
- `INV-01`: [e.g., Balance cannot be negative]
- `INV-02`: [e.g., Resource IDs must be unique]

## 3. Automation Target
- **Script**: `./tests/red_team/phase_[ID]_attack.py`
- **Fuzzing Seed**: Define input range (e.g., merit values from -1B to +1B).

## 4. Mitigation Plan
- What should the system do when an attack is detected? (Drop packet, Log alert, Lockdown domain).
