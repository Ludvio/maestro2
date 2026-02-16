---
description: "The Test Plan Template. Defines end-to-end verification steps. Mandatory for 'Definition of Done'."
---

# Phase [XX] Test Plan: [Name]

> **Context**: How to verify the correctness of Phase [XX] (e.g., Merit Ledger).
> **Dependency**: Requires successful build of Phase [YY] (e.g., User Profiles).

## 1. Setup (Given)
*   **User A**: `test_giver` (Reputation: 500).
*   **User B**: `test_receiver` (Reputation: 100).
*   **Environment**: Offline Mode DISABLED (Online).
*   **Initial State**: User B has 0 `Zaslugi` from User A.

## 2. Happy Path (When)
1.  **Action**: User A navigates to User B's profile.
2.  **Input**: Clicks "Give Merit" -> Types "Helped with harvest" -> Selects "+10".
3.  **Result**: Toast "Merit Sent!" appears.
4.  **Confirm**: User B's profile updates to Show "Reputation: 110".

## 3. Expected State (Then)
*   [ ] User A's `Zaslugi` balance decreases (if applicable).
*   [ ] User B receives a notification: "You earned merit!".
*   [ ] The Ledger (`Księga`) shows a new entry: `GIVER -> RECEIVER (+10)`.

## 4. Edge Cases (The 'Red Team')
1.  **Self-Award**: User A tries to give merit to User A. -> System blocks with "Cannot award self".
2.  **Zero Value**: User A types "0" points. -> Button disabled.
3.  **Rapid Fire**: User A clicks "Send" 5 times in 1 second. -> Only 1 transaction recorded.

## 5. Automated Check (Script)
*   Run: `python scripts/test_phase_[XX].py`
*   Verify output: `SUCCESS: Phase [XX] passed all 4 invariants.`
