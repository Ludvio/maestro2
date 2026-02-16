jt<!-- Description: Technical Design (RFC) for Phase [XX]. -->
<!-- Orchestration: Phase [XX] | Active -->
<!-- 
RFC TEMPLATE - DEEP ENGINEERING STANDARD
MINIMUM LENGTH REQUIREMENT: 300 LINES
STATUS: DRAFT | REVIEW | ACCEPTED | REJECTED

RULES:
1. NO BUSINESS LOGIC (no if/else, no loops) in the document.
2. MANDATORY SCHEMAS (Interfaces, JSON definitions, Protobuf).
3. DETAILED ALTERNATIVES (why this is better than other ways).
4. CLEAR ROLLOUT & ROLLBACK PLAN (Chapter 5).
-->

# RFC {Number}: {Title}

| Metadata | Details |
| :--- | :--- |
| **Author** | {Agent/Name} |
| **Created** | {Date} |
| **Status** | **DRAFT** |
| **Complexity** | {Rating 1-10} |
| **Impact** | {High/Medium/Low} |
| **Layer** | LAYER_D (Technical Design & Execution) |

> **Abstract**: A strictly technical summary of the proposed changes. Limit to 3 sentences.

## 1. Introduction & Motivation
### 1.1 The Problem
Describe the problem in detail. Why is the current state insufficient?
*   Cite specific failure modes.
*   Reference specific user complaints or architectural bottlenecks.

### 1.2 The Goal (including SLOs)
What exactly are we trying to achieve?
*   **Primary Goal**: ...
*   **Secondary Goal**: ...
*   **SLO 1 (Performance)**: e.g., "Verification must take < 100ms on a 2018 smartphone".
*   **SLO 2 (Reliability)**: e.g., "99.9% of local writes must be idempotent".

### 1.3 Non-Goals (Out of Scope)
Crucial section. List at least 3 things we are NOT doing in this phase to prevent scope creep.
1.  We are NOT refactoring the entire legacy auth system.
2.  We are NOT adding support for mobile native push notifications yet.
3.  ...

### 1.4 Pattern Mining (The "Machine building the Machine")
> **S0 Step**: Does this phase implement a shared pattern from `docs/patterns/`?
*   **Pattern Reference**: [e.g. docs/patterns/STAKING.md]
*   **Customization**: How is the shared pattern modified for this specific context?

## 2. Systemic Architecture (The Living System)
> **CRITICAL**: This section defines how the new phase breathes life into the existing ecosystem. Isolated features are forbidden.

### 2.1 Systemic Loops (The "Why")
*Define how this phase closes a loop using existing features.*
*   **Trigger**: What starts the loop? (e.g. Transaction P05)
*   **Action**: What does the user do? (e.g. Echo P30)
*   **Reward**: How does the system update? (e.g. Trust P15)

### 2.2 Strict Invariants (The "Truth")
*Define hard logic rules using pseudo-code. These will be tested by Layer S.*
```typescript
// INV-[XX]-01: Trust Floor
if (user.trust_score < 0) throw new Error("Trust cannot be negative");

// INV-[XX]-02: Verify First
if (!user.isVerified) throw new Error("Must be verified to Vouch");
```

### 2.3 Retrofit Strategy (The Time-Travel Fix)
*How do we fix previous phases to support this new feature?*
*   **Phase [N] Impact**: Does Phase [N] need a new hook?
*   **Action Plan**:
    *   [ ] Update `src/store/usePhaseNStore.ts` to include `onEventX` handler.
    *   [ ] Add `newField` to Phase [N] Interface.

### 2.4 Multidimensional Coherence Matrix (The Tightness Check)
*Verify that the loop is tight across all planes of existence. Empty rows are FORBIDDEN.*

| Dimension | Trigger (Input) | Effect (Output) | Invariant (Safety) |
| :--- | :--- | :--- | :--- |
| **Economic** | e.g. "User pays Fee" | "Resource Burn" | `Balance >= Fee` |
| **Social** | e.g. "User meets Peer" | "Trust Score ++" | `Face-to-Face Verified` |
| **Legal** | e.g. "Dispute Filed" | "Law Precedent Set" | `LawID Exists` |
| **Technical**| e.g. "API Call" | "DB Write (ACID)" | `Idempotency Key` |
| **Natural**  | e.g. "Season Change" | "Resource Decay" | `Time > LastHarvest` |

### 2.5 Layer N: Narrative Lifecycle (The Visibility Contract)
*Define when this feature is visible/relevant to the user. No context-less features.*
*   **Discovery Trigger**: e.g., "Feature is hidden until user has 10 Merit points."
*   **Active State**: e.g., "Appears in Sidebar only during a Dispute."
*   **Dormant State**: e.g., "Becomes Read-Only during the Winter season (P25)."

## 3. Production Readiness (The "Sleep Well" Chapter)

### 3.1 The Eval (Automated Oracle)
*Define the simulation script that proves success before merge.*
*   **Script**: `tests/evals/eval_phase_XX.ts`
*   **Scenario**: e.g. "Run 1000 transactions acting as 50 users over 1 virtual year."
*   **Success Metric**: e.g. "System Total Merit remains constant (Zero-Sum) or grows boundedly."

### 3.2 Telemetry & Signals (The Dashboard)
*What clearly visible signals does this feature emit?*
*   **Log Event**: `Log.info('PHASE_XX', 'Critical Action', { id, context })`
*   **Health Check**: Function `isHealthy()` that returns `true` if internal state is consistent.

### 3.3 The "Panic Button" (Resilience)
*If this feature bugs out in production, how do we kill it without killing the app?*
*   **Feature Flag**: `FLAGS.ENABLE_PHASE_XX`
*   **Safe Mode**: Fallback UI if API fails (e.g. Read-Only Mode).

### 3.4 Sync & Conflict Strategy (The Multiplayer Pattern)
*Defining how data synchronizes across the Mesh/Splot (Phase 20).*
*   **Idempotency Key**: What logic ensures a message can be processed 100 times but saved once?
*   **Conflict Resolution**: (e.g., LWW - Last Write Wins, or Custom Consensus logic).
*   **Offline Access**: What happens if the Splot is disconnected for 24 hours?

## 4. Detailed Design
### 2.1 Architecture Diagram (Mermaid)
Provide a `graph TD` or `sequenceDiagram` showing the data flow.

### 2.2 Data Model / Schema Changes
Describe the exact JSON structure, Database Schema, or Type interfaces.
**MANDATORY**: Define the exact structures. Do NOT write logic.
```typescript
// Interface details...
```

### 2.3 API / Protocol Definition
Define the exact function signatures or network protocol messages.
*   **Input**: ...
*   **Output**: ...
*   **Error Handling**: ...

### 2.4 Interface Contract (Context Protection)
**MANDATORY**: Define the public interface here. This is the ONLY part of the implementation that future agents should need to read to integrate with this module.
```typescript
export interface Phase[XX]Contract {
    // ... method signatures
}
```
> **Standard**: Every public method must have a TSDoc comment explaining its Invariant.

### 2.4 State Management & Persistence
How is data stored? How is it synced? How do we handle "Offline-First"?

### 2.5 Edge Cases & Failure Modes (Analysis)
Analyze at least 3 failure scenarios:
1.  **Network Partition**: What if the user goes offline during the transaction?
2.  **Sync Conflict**: Two users edit the same record.
3.  **Data Corruption**: The disk is full.

## 3. Alternatives Considered (Trade-offs)
*You must list at least 2 alternative approaches and explain why they were rejected.*

### Alternative A: {Name}
*   **Description**: ...
*   **Pros**: ...
*   **Cons**: ...
*   **Reason for Rejection**: ...

### Alternative B: {Name}
*   **Description**: ...
*   **Pros**: ...
*   **Cons**: ...
*   **Reason for Rejection**: ...

## 4. Cross-Cutting Concerns
### 4.1 Security & Privacy
*   **Threat Model**: Who is the attacker?
*   **Mitigation**: Encryption, AuthZ, Sanitzation.

### 4.2 Scalability & Performance
*   **Big O Notation**: Complexity of the core algorithm.
*   **Limits**: Maximum users? Maximum file size?
*   **Latency Budget**: Expected response time.

### 4.3 Observability
*   How will we know it's working?
*   What logs/metrics are emitted?

### 4.4 Migration Path
How do we upgrade existing data? Describe the "schema-up" migration strategy.

## 5. Implementation Plan (Phased Rollout)
### 5.1 Milestones & Tasks
Detailed breakdown of tasks.
*   [ ] **Phase 1: Interfaces**
*   [ ] **Phase 2: Core Logic**
*   [ ] **Phase 4: Migration/Cleanup**

### 5.2 Verification Plan (Testing)
*   Describe the Red Team test cases.
*   Describe the Manual Audit steps to verify SLOs.

### 5.3 Rollback Strategy
If the deployment fails, how do we return to the previous stable state?
1. Step 1: ...
2. Step 2: ...

## 6. Conclusion
Final thoughts on the impact of this change.
