import os
import sys

def check_file(path, label):
    if os.path.exists(path):
        print(f"✅ {label}: FOUND ({path})")
        return True
    else:
        print(f"❌ {label}: MISSING ({path})")
        return False

print("--- PHASE 37 JUDGE: WIECZNICA ---")

results = [
    check_file("docs/phases/phase_37/LAYER_C_UX.md", "Layer C (UX)"),
    check_file("docs/phases/phase_37/LAYER_D_RFC.md", "Layer D (RFC)"),
    check_file("docs/idempotency_contracts/phase_37_veche.json", "Layer E (Contract)"),
    check_file("prototypes/phase_37_sim.ts", "Layer S (Simulation)"),
    check_file("src/store/useVecheStore.ts", "Layer I (Store)"),
    check_file("src/pages/Veche.tsx", "Layer I (UI)"),
    check_file("tests/e2e/phase_37_veche.spec.ts", "Layer P (Test Spec)")
]

if all(results):
    print("\n[JUDGE]: All artifacts present. Ready for Layer P Verification.")
    sys.exit(0)
else:
    print("\n[JUDGE]: Phase incomplete or files moved.")
    sys.exit(1)
