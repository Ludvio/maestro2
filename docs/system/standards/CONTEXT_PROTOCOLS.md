# CONTEXT PROTECTION PROTOCOLS (Anthropic-Style)

> **Mandate**: This standard exists to prevent "Context Poisoning" (the agent having to read 1000s of lines for a simple fix) and to ensure "Deterministic Implementation".

## 1. The "Interface-Lockdown" Protocol
Agents are FORBIDDEN from reading full `.tsx` files if they only need to understand a component's inputs/outputs.
*   **The Action**: Every Phase MUST export a `Phase[XX]Contract.ts` that defines its public API.
*   **Verification**: If an agent is caught reading a full file without first checking the contract, it is a **Process Violation**.
*   **Goal**: Keep the agent's working memory focused on *integration* rather than *implementation details*.

## 2. Shadow Code Prohibition
*   **Rule**: NO code may exist in the `src/` directory without a corresponding invariant test in `tests/e2e/`.
*   **Enforcement**: The `milestone_check.py` will soon include a coverage check. If a new function is added without a Layer P proof, the grid turns RED.
*   **Logic**: Every function is a liability until proven innocent by a test.

## 3. Adversarial State Injection (The "Crucible")
*   **Standard**: System robustness is measured by its reaction to "Poisoned Context".
*   **Test Case**: Every Store must have one test that purposefully injects invalid JSON into `localStorage`.
*   **Expected Result**: The app must either reset to defaults or repair the schema automatically. "White Screen" is an automatic FAILURE.

## 4. Atomic Change Budget (The 150-Line Rule)
*   **Max modification per session**: 150 lines of code.
*   **Why?**: Beyond 150 lines, the probability of "Silent Regressions" (like the useSyncStore crash) increases exponentially.
*   **Refactor Requirement**: If a feature requires >150 lines, it MUST be implemented as a series of atomic "Milestones" with full TSC verification between each.

## 5. Registry-based Architecture (The "Map")
All global state (Zustand) and Page mappings must be registered in `docs/registry/MANIFEST.json`.
*   **Protocol**: Before creating a new file, check the MANIFEST. If it's not registered, it doesn't exist for the Peer Network or the Orchestrator.

---
**Signed**: Antigravity (Lead Architect)
