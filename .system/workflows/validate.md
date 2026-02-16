---
description: Run deterministic milestone validation and generate visual proof of validity.
---

# /validate Workflow

This workflow executes the deterministic verification scripts and generates high-fidelity visual proof that the project milestones are valid and functioning as expected.

## Steps

1. **Check Environment**
   - Verify `npm run dev` is running on `http://localhost:5173`.
   - Ensure Playwright environment is ready (`.venv`).

2. **Execute Proof Generator**
   // turbo
   - Run the master proof script:
     `source .venv/bin/activate && python3 scripts/milestone_proof.py --all`

3. **Reporting**
   - Display the verification table.
   - List the generated "Proof" screenshots in `docs/proofs/`.

4. **Gold Standard Verification**
   - Cross-reference results with `docs/implementation_plans/` status checkboxes.
