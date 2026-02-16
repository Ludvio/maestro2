<!-- Description: The Supreme Engineering Standard for Maestro. Mandates RFC and Simulation loops. -->
<!-- Orchestration: System | Global -->
# GROMADA ENGINEERING STANDARD (v2.0)

> **Mandate**: All "Design Phase" deliverables (Layer D) must adhere to the **RF-Deep-Dive** protocol. Simple "Implementation Plans" are deprecated for complex features.

## 1. The 300-Line Rule (Quantity as Proxy for Quality)
An RFC describing a distributed system component (e.g. Trade, Consensus, Sync) MUST be at least **300 lines of structured text**.
*   **Why?**: You cannot adequately describe failure modes, data schemas, security threats, and alternative architectures in less space.
*   **Enforcement**: Use `wc -l` before committing. If $<300$, expand the "Failure Modes" or "Alternatives" sections.

## 2. Required Analysis Sections (The "Brain" of the RFC)
Every RFC must contain these specific H2 headers:

### 2.1 "Non-Goals" (The Scope Fence)
*   List at least 3 things we are NOT doing.
*   *Example*: "We are not building a GPS tracker."

### 2.2 "Alternatives Considered" (The Trade-offs)
*   List at least 2 other ways to solve the problem.
*   Explain why they were rejected (e.g., "Too centralized", "Too expensive").
*   *Format*: Description / Pros / Cons / Verdict.

### 2.3 "Failure Modes & Edge Cases" (The Murphy's Law)
*   Analyze at least 3 scenarios where things go wrong.
*   *Example*: "What if the battery dies during the signature process?"

## 3. Workflow Integration (The Iteration Loop)

### 3.1 Architecture Phase (Concept)
1.  **Layer 0 (Reflection)**: Why do we need this?
2.  **Layer A (Milestone)**: What exactly is it?
3.  **Layer B (ADR)**: Key decisions (e.g., P2P vs Client-Server).

### 3.2 Design & Validation Phase (The Loop)
This is where the agentic iteration happens.

4.  **Layer D (RFC)**: Deep technical design (v1.0).
5.  **Layer S (Simulation) [NEW]**:
    *   **Action**: Create a standalone script `prototypes/phase_X_sim.ts`.
    *   **Goal**: Prove the RFC's algorithm handles the edge cases defined in logical steps 2.5.
    *   **Loop Rule**: If the simulation reveals a flaw (e.g., race condition), you MUST **UPDATE the RFC (v1.1)** before proceeding. Do not hack the simulation to pass. Fix the Design Doc first.
    *   *Exit Criteria*: `ts-node prototypes/phase_X_sim.ts` returns `SUCCESS` and matches RFC logic.

### 3.3 Implementation Phase (Code)
Only proceed here after Layer S passes.

6.  **Layer E (Contracts)**: API Definitions.
7.  **Layer F (Red Team)**: Security Exploits.
8.  **Layer G (Verification)**: Test Plan.
9.  **Layer H (Log)**: Continuous Improvement.

## 4. The "Systemic Coherence" Mandate (Formerly Frankenstein Check)
**Rule**: No feature exists in isolation. Every Phase MUST close a loop.
1.  **The Loop Check**: Layer D (RFC) must define a Trigger -> Action -> Reward cycle involving at least 2 other phases.
2.  **The Retrofit Protocol**: If a new feature requires data from an old phase, you MUST refactor the old phase first. "Hacking around" legacy code is forbidden.
3.  **The Coherence Matrix**: Technical, Economic, Social, Legal, and Natural dimensions must be defined.

## 5. Layer S: The Simulation Oracle
Code correctness (Unit Tests) is not enough. We require **Systemic Verification**.
*   **Mandate**: Every Phase must have a `tests/evals/eval_phase_XX.ts` script based on `SIMULATION_TEMPLATE.ts`.
*   **Success**: The script must run for 365 virtual days without breaking Invariants (e.g. "No Starvation", "No Negative Trust").
*   **Gate**: You cannot proceed to Layer I (UI/Store) until Layer S (Simulation) passes.

## 6. Layer G: The Integration Judge
The Judge script (Layer G) must verify:
1.  **RFC Compliance**: Does `## 2. Systemic Architecture` exist?
2.  **Import Check**: Does the code actually import the dependencies listed in the RFC?
3.  **Oracle Pass**: Did the simulation return exit code 0?

## 7. Layer U: User Experience Coherence (The Four Pillars Law)
**Mandate**: Navigation is a map of life, not a database index.
1.  **The Four Pillars**: Every feature MUST reside within one of the four defined Life Zones:
    *   🏠 **GOSPODARSTWO** (Self & Resource Management)
    *   🤝 **RYNEK** (Trade & Economy)
    *   🔥 **OGNISKO** (Reputation & Community)
    *   ⚖️ **WIEC** (Law & Power)
2.  **Cognitive Load Limit**: No Pillar may contain more than 7 primary actions. 
3.  **Contextual Display**: Features should be hidden until their "Trigger" (Loop) is activated (e.g., Disputes appear only when a Trade fails).
4.  **Audit**: A `ux_integrity.py` check must pass before any new UI is implemented.

## 8. Process Consistency (SSOT)
The Judge script (Layer G) must not only verify file existence but also perform a **Greps-for-Imports** check:
1. Identify dependencies listed in Layer D.
2. Verify that `src/store/usePhaseStore.ts` actually imports and calls the dependent stores.
3. If no cross-store calls are found, the Phase remains `INCOMPLETE`.

## 6. Process Consistency (SSOT)

Maestro follows a "Self-Consistent Architecture" (Anthropic-Standard).

1. **Law of the Orchestrator**: Any change to the orchestration scripts (e.g., `checkpoint.py`, `judgement_day.py`) is considered a **Structural Process Change**.
2. **Mandatory Documentation Update**: Such changes are NOT complete until the following files are synchronized:
    - `.agent/skills/maestro-prime/SKILL.md` (Capability definition)
    - `.agent/workflows/` (The user manuals)
3. **Atomic Commit**: Ideally, a process change should be committed alongside its corresponding documentation updates in a single atomic set.
4. **Breadcrumbs**: Scripts must contain cross-reference comments pointing to the documentation they implement.

---
**Signed**: Antigravity (Lead Architect)

## 6. The API Contract Check (Pre-Phase Ritual)

Before starting any Phase N implementation (Layer I), developers must verify the public interfaces of Phase N-1 dependencies.

*   **The Check**: Does `Phase_N-1.function()` accept the data structure required for `Phase_N`?
*   **The Action**:
    *   **Yes**: Proceed.
    *   **No**: STOP. Create a **Hotfix Plan** for Phase N-1. Do not hack around the limitation. Do not use `any`.

## 7. Living Codebase Principle (Iterative Evolution)

Code from completed Phases is not a sacred relic. If a new Phase reveals a design flaw or missing feature in a completed Phase:

1.  **Refactor**: Modify the completed Phase to support the new requirement (e.g., adding `type` field to `SyncRecord`).
2.  **Regression Test**: IMMEDIATELY run the test suite for the modified Phase (e.g., `npx playwright test tests/e2e/phase_20_sync.spec.ts`).
3.  **Green Light**: Only proceed if the regression test passes.

## 9. Context Hygiene (The Anti-Poisoning Protocol)

All developers (human and agentic) must follow `docs/standards/CONTEXT_PROTOCOLS.md`.
*   **The Golden Rule**: Never read more than 100 lines if the answer can be found in an interface definition.
*   **The Artifact**: Every Phase must update `docs/registry/MANIFEST.json` upon completion.

## 10. The "Anti-Crap" Threshold (ACT)

A Phase is not "Complete" until `python scripts/milestone_check.py` returns `SUCCESS`.
*   **Composition**:
    1.  **Zero TSC Errors**: Clean build.
    2.  **Zero Console Errors**: Checked via Playwright Console Audit.
    3.  **Invariant Match**: Logic proof passes.
