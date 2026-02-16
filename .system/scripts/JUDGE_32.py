import os
import sys

# Orchestration: Phase 32 | Layer G (Judge)
# Mandate: Automated Vertical Compliance Check for Veche Handbook.

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
    print("⚖️ AUDITING PHASE 32 (SUPREME ARCHITECTURE STANDARD)...")
    
    complianceIndices = [
        check_line_count("docs/phases/phase_32/LAYER_D_RFC.md", 300),
        check_file("src/contracts/Phase32Contract.ts", "Contract"),
        check_file("src/store/useLawStore.ts", "Store"),
        check_file("prototypes/phase_32_sim.ts", "Simulation"),
        check_file("src/pages/LawBook.tsx", "UI Dashboard"),
        check_file("tests/e2e/phase_32_lawbook.spec.ts", "Proof (E2E)"),
        check_file("prototypes/phase_32_fuzzer.js", "Fuzzer")
    ]
    
    score = sum(complianceIndices) / len(complianceIndices) * 100
    print(f"\n--- AUDIT COMPLETE: {score:.1f}% COMPLIANCE ---")
    
    if score == 100:
        print("🏆 PHASE 32 VERIFIED: SUPREME STATUS ACHIEVED.")
        return 0
    else:
        print("⚠️ PHASE 32 INCOMPLETE: Correct violations before deployment.")
        return 1

if __name__ == "__main__":
    sys.exit(run_audit())
