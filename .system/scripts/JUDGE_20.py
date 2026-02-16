import os
import sys

# Orchestration: Phase 20 | Layer G (Judge)
# Description: Automated compliance judge for Splot Sync layer.

def check_phase_20():
    print("--- JUDGE PHASE 20: Splot Sync ---")
    
    compliance = True
    
    # 1. Layer D: RFC
    rfc_path = "docs/phases/phase_20/LAYER_D_RFC.md"
    if os.path.exists(rfc_path):
        with open(rfc_path, 'r') as f:
            lines = f.readlines()
            if len(lines) >= 300:
                print(f"✅ Layer D (RFC): COMPLIANT ({len(lines)} lines)")
            else:
                print(f"❌ Layer D (RFC): NON-COMPLIANT (Found {len(lines)} lines, need 300)")
                compliance = False
    else:
        print("❌ Layer D (RFC): MISSING")
        compliance = False

    # 2. Layer E: Contract
    contract_path = "src/contracts/Phase20Contract.ts"
    if os.path.exists(contract_path):
        print("✅ Layer E (Contract): COMPLIANT")
    else:
        print("❌ Layer E (Contract): MISSING")
        compliance = False

    # 3. Layer I: Logic (Store)
    store_path = "src/store/useSyncStore.ts"
    if os.path.exists(store_path):
        print("✅ Layer I (Store): COMPLIANT")
    else:
        print("❌ Layer I (Store): MISSING")
        compliance = False

    # 4. Layer U: UI (Monitor HUD)
    ui_path = "src/components/dev/SyncMonitorHUD.tsx"
    if os.path.exists(ui_path):
        print("✅ Layer U (UI): COMPLIANT")
    else:
        print("❌ Layer U (UI): MISSING")
        compliance = False

    # 5. Layer P: Proof
    proof_path = "tests/e2e/phase_20_sync.spec.ts"
    if os.path.exists(proof_path):
        print("✅ Layer P (Proof): COMPLIANT")
    else:
        print("❌ Layer P (Proof): MISSING")
        compliance = False

    if compliance:
        print("\n--- STATUS: PHASE 20 IS 100% SUPREME ---")
        sys.exit(0)
    else:
        print("\n--- STATUS: PHASE 20 FAILED COMPLIANCE ---")
        sys.exit(1)

if __name__ == "__main__":
    check_phase_20()
