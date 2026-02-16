import os
import sys

# Orchestration: Phase 21 | Layer G (Judge)
# Description: Automated compliance judge for Identity & Trust layer.

def check_phase_21():
    print("--- JUDGE PHASE 21: Identity & Trust ---")
    
    compliance = True
    
    # 1. Layer D: RFC
    rfc_path = "docs/phases/phase_21/LAYER_D_RFC.md"
    if os.path.exists(rfc_path):
        with open(rfc_path, 'r') as f:
            lines = f.readlines()
            if len(lines) >= 300:
                print("✅ Layer D (RFC): COMPLIANT (300+ Lines)")
            else:
                print(f"❌ Layer D (RFC): NON-COMPLIANT (Found {len(lines)} lines, need 300)")
                compliance = False
    else:
        print("❌ Layer D (RFC): MISSING")
        compliance = False

    # 2. Layer E: Contract
    contract_path = "src/contracts/Phase21Contract.ts"
    if os.path.exists(contract_path):
        print("✅ Layer E (Contract): COMPLIANT")
    else:
        print("❌ Layer E (Contract): MISSING")
        compliance = False

    # 3. Layer I: Logic (Store)
    store_path = "src/store/useTrustStore.ts"
    if os.path.exists(store_path):
        print("✅ Layer I (Store): COMPLIANT")
    else:
        print("❌ Layer I (Store): MISSING")
        compliance = False

    # 4. Layer U: UI
    ui_path = "src/pages/Citizenship.tsx"
    if os.path.exists(ui_path):
        print("✅ Layer U (UI): COMPLIANT")
    else:
        print("❌ Layer U (UI): MISSING")
        compliance = False

    # 5. Layer P: Proof
    proof_path = "tests/e2e/phase_21_trust.spec.ts"
    if os.path.exists(proof_path):
        print("✅ Layer P (Proof): COMPLIANT")
    else:
        print("❌ Layer P (Proof): MISSING")
        compliance = False

    if compliance:
        print("\n--- STATUS: PHASE 21 IS 100% SUPREME ---")
        sys.exit(0)
    else:
        print("\n--- STATUS: PHASE 21 FAILED COMPLIANCE ---")
        sys.exit(1)

if __name__ == "__main__":
    check_phase_21()
