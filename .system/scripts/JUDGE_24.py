import os
import sys

# Orchestration: Phase 24 | Layer G (Judge)
# Description: Automated compliance judge for Refining & Processing layer.

def check_phase_24():
    print("--- JUDGE PHASE 24: Refining & Processing ---")
    
    compliance = True
    
    # 1. Layer D: RFC
    rfc_path = "docs/phases/phase_24/LAYER_D_RFC.md"
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
    contract_path = "src/contracts/Phase24Contract.ts"
    if os.path.exists(contract_path):
        print("✅ Layer E (Contract): COMPLIANT")
    else:
        print("❌ Layer E (Contract): MISSING")
        compliance = False

    # 3. Layer I: Logic (Store)
    store_path = "src/store/useRefiningStore.ts"
    if os.path.exists(store_path):
        print("✅ Layer I (Store): COMPLIANT")
    else:
        print("❌ Layer I (Store): MISSING")
        compliance = False

    # 4. Layer S: Simulation
    sim_path = "prototypes/phase_24_sim.ts"
    if os.path.exists(sim_path):
        print("✅ Layer S (Simulation): COMPLIANT")
    else:
        print("❌ Layer S (Simulation): MISSING")
        compliance = False

    # 5. Layer U: UI (Page)
    ui_path = "src/pages/Refinery.tsx"
    if os.path.exists(ui_path):
        print("✅ Layer U (UI): COMPLIANT")
    else:
        print("❌ Layer U (UI): MISSING")
        compliance = False

    if compliance:
        print("\n--- STATUS: PHASE 24 IS 100% SUPREME ---")
        sys.exit(0)
    else:
        print("\n--- STATUS: PHASE 24 FAILED COMPLIANCE ---")
        sys.exit(1)

if __name__ == "__main__":
    check_phase_24()
