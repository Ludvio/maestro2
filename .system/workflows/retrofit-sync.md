---
description: Retrofit Phase for Sync (Splot) and Idempotency contracts using Safe Evolution.
---

# SYNC RETROFIT WORKFLOW (The Splot Protocol)

> **Goal**: Upgrade a Phase to support LCRDT (Last Creator Wins) and Offline-First Sync without breaking existing logic.
> **Standard**: `docs/standards/SAFE_EVOLUTION.md`.

## 1. Safety Audit & Scaffolding (Non-Destructive)
1.  **Check Structure**: If `MANIFEST.json` is missing or phase is in Legacy location:
    - Run `python3 .system/scripts/scaffold_phase.py [ID] [PILLAR] [NAME]`.
    - This ensures all artifacts have a home.
2.  **Analyze State**: Read `src/store/use[Phase]Store.ts`.

## 2. The Shadow Implementation (Parallel Code)
1.  **Create Protocol**: Write `src/features/sync/WiciProtocol.ts` (if base missing) or `src/features/[phase]/[Phase]SyncAdapter.ts`.
    - MUST implement `LamportClock`.
    - MUST handle `lastWriteWins` logic.
2.  **Verify Logic**: Write a unit test `tests/unit/sync_[phase].test.ts`.
    - Simulate 2 nodes updating same data. Ensure convergence.

## 3. The Gentle Hook (Integration)
1.  **Modify Store**: Open `src/store/use[Phase]Store.ts`.
2.  **Add Listener**:
    - Add `syncAdapter` to state.
    - In actions (e.g. `addResource`), append `syncAdapter.broadcast(change)`.
    - **FORBIDDEN**: Do not remove existing `localStorage` or logic.
3.  **Shadow Run**: Log differences between Old Sync (if any) and New Sync.

## 4. Verification Check
1.  **Simulate**: Run `tests/evals/eval_phase_[XX].ts` (S3).
2.  **Check Pulse**: Ensure Telemetry shows synchronization events.

---
**Trigger**: Use `/retrofit-sync Phase [XX]` to start.
