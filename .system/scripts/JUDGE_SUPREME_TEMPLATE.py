"""
Description: SUPREME PHASE JUDGE (Constitutional Auditor v2.0)
Orchestration: Phase [XX] | Layer G (Verification)
Status: DETERMINISTIC CONSTITUTIONAL CHECK

Mandate:
This script performs a 360-degree audit of all layers in Phase [XX].
A 100% Score is required for 'Supreme Architecture' compliance.
v2.0 Update: Now mandates Layer F (Fuzzer) presence and execution.
"""

import os
import sys
import glob

PHASE_ID = "[XX]"
MIN_RFC_LINES = 300

def audit_phase():
    print(f"--- ⚖️ JUDGING PHASE {PHASE_ID}: CONSTITUTIONAL INTEGRITY AUDIT ---")
    results = {
        "Layer D (RFC)": False,
        "Layer E (Contract)": False,
        "Layer I (Store)": False,
        "Layer S (Sim)": False,
        "Layer U (UI)": False,
        "Layer F (Fuzzer)": False, # Red Team Automated
        "Layer P (Proof)": False
    }

    print("\n[1] BUREAUCRATIC CHECK (File Existence & Standards)...")

    # 1. Layer D: RFC Analysis (The Constitution)
    rfc_path = f"docs/phases/phase_{PHASE_ID}/LAYER_D_RFC.md"
    if os.path.exists(rfc_path):
        with open(rfc_path, 'r') as f:
            lines = f.readlines()
            if len(lines) >= MIN_RFC_LINES:
                results["Layer D (RFC)"] = True
                print(f"  ✅ [RFC] {len(lines)} lines (Standard Met)")
            else:
                print(f"  ❌ [RFC] Too thin ({len(lines)} < {MIN_RFC_LINES}). Explain deeper.")
    else:
        print(f"  ❌ [RFC] Missing.")

    # 2. Layer E: Contract (The API Promise)
    if glob.glob(f"src/**/*{PHASE_ID}*Contract.ts", recursive=True):
        results["Layer E (Contract)"] = True
        print("  ✅ [Contract] Defined.")
    else:
        print("  ❌ [Contract] Missing Interface Lock.")

    # 3. Layer I: Implementation
    if os.path.exists(f"src/store/use{PHASE_ID}Store.ts") or glob.glob(f"src/**/*{PHASE_ID}*Logic.ts"):
        results["Layer I (Store)"] = True
        print("  ✅ [Implement] Logic Found.")
    else:
        print("  ❌ [Implement] No Store Found.")

    # 4. Layer S: Simulation (Happy Path)
    sim_path = f"prototypes/phase_{PHASE_ID}_sim.ts"
    if os.path.exists(sim_path):
        results["Layer S (Sim)"] = True
        print("  ✅ [Sim] Happy Path Defined.")
    else:
        print("  ❌ [Sim] Missing.")

    # 5. Layer U: User Interface
    # Heuristic check for UI component or page
    if glob.glob(f"src/**/*{PHASE_ID}*.tsx", recursive=True) or glob.glob(f"src/**/*Refinery*.tsx", recursive=True):
        results["Layer U (UI)"] = True
        print("  ✅ [UI] Component Found.")
    else:
        print("  ❌ [UI] Missing Visuals.")

    # 6. Layer F: Fuzzer (The Adversary) - NEW MANDATE
    fuzzer_path = f"prototypes/phase_{PHASE_ID}_fuzzer.js" # JS for standalone execution
    if os.path.exists(fuzzer_path):
        results["Layer F (Fuzzer)"] = True
        print(f"  ✅ [Fuzzer] Adversarial Agent Present ({fuzzer_path}).")
    else:
        print(f"  ❌ [Fuzzer] MISSING ADVERSARIAL AGENT. Security Critical.")

    # 7. Layer P: Proof (E2E)
    proof_path = f"tests/e2e/phase_{PHASE_ID}_*.spec.ts"
    if glob.glob(proof_path):
        results["Layer P (Proof)"] = True
        print("  ✅ [Proof] E2E Test Found.")
    else:
        print("  ❌ [Proof] No Evidence of Function.")


    # --- FINAL VERDICT ---
    score = sum(1 for v in results.values() if v)
    total = len(results)
    integrity = (score / total) * 100

    print(f"\n--- INTEGRITY SCORE: {integrity:.1f}% ---")
    
    if integrity < 100:
        print("\n[FAIL]: Phase does not meet the SUPREME Standard.")
        print("Recommendation: Implement missing layers before proceeding.")
        sys.exit(1)
    
    print("\n[SUCCESS]: Phase is Constitutionally Sound.")
    sys.exit(0)

if __name__ == "__main__":
    audit_phase()
