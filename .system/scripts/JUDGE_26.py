import os
import sys

# Orchestration: Phase 26 | Layer G (Judge)
# Mandate: Automated Vertical Compliance Check for Circular Economy.

def check_file(path, label):
    if os.path.exists(path):
        print(f"✅ {label} found: {path}")
        return True
    else:
        print(f"❌ {label} MISSING: {path}")
        return False

def check_line_count(path, min_lines):
    if not os.path.exists(path): return False
    with open(path, 'r') as f:
        count = sum(1 for _ in f)
    if count >= min_lines:
        print(f"✅ {path} meets size requirement ({count} lines).")
        return True
    else:
        print(f"❌ {path} TOO SHORT ({count} < {min_lines} lines).")
        return False

def run_audit():
    print("⚖️ AUDITING PHASE 26 (SUPREME ARCHITECTURE STANDARD)...")
    
    complianceIndices = [
        check_line_count("docs/phases/phase_26/LAYER_D_RFC.md", 300),
        check_file("src/contracts/Phase26Contract.ts", "Contract"),
        check_file("src/store/useCircularStore.ts", "Store"),
        check_file("prototypes/phase_26_sim.ts", "Simulation"),
        check_file("src/pages/CircularHub.tsx", "UI Hub Page"),
        check_file("tests/e2e/phase_26_circular.spec.ts", "Proof (E2E)"),
        check_file("prototypes/phase_26_fuzzer.js", "Fuzzer")
    ]
    
    score = sum(complianceIndices) / len(complianceIndices) * 100
    print(f"\n--- AUDIT COMPLETE: {score:.1f}% COMPLIANCE ---")
    
    if score == 100:
        print("🏆 PHASE 26 VERIFIED: SUPREME STATUS ACHIEVED.")
        return 0
    else:
        print("⚠️ PHASE 26 INCOMPLETE: Correct violations before deployment.")
        return 1

if __name__ == "__main__":
    sys.exit(run_audit())
