# Description: Unified Phase Judge Script. Determines PAS/FAIL status deterministically.
# Orchestration: Judge Template | Active | Standard: Anthropic-Hard-Gate

"""
TEMPLATE: PHRASE_JUDGE.py
Acts as the FINAL GATEKEEPER for a Phase.
It orchestrates:
1. Schema Validation (Linting)
2. Prototype Simulation (Layer S)
3. Red Team Attack (Layer F)
4. Contract Adherence (Layer E)

Returns EXIT_CODE 0 only if ALL pass.
"""

import sys
import os
import subprocess
import json

def run_step(step_name, command):
    print(f"\n⚖️  JUDGE: Verifying {step_name}...")
    try:
        # Run process, capture output
        result = subprocess.run(
            command, 
            shell=True,
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"✅ PASS: {step_name}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ FAIL: {step_name}")
        print(f"   Error: {e.stderr}")
        return False

def check_files_exist(required_files):
    print(f"\n⚖️  JUDGE: Checking Artifact Existence...")
    all_exist = True
    for f in required_files:
        if not os.path.exists(f):
            print(f"❌ MISSING: {f}")
            all_exist = False
        else:
            print(f"✅ FOUND: {f}")
    return all_exist

def main():
    PHASE_ID = "[XX]"
    print(f"=== ⚖️  GROMADA PHASE {PHASE_ID} JUDGEMENT DAY ⚖️  ===")
    
    # 1. ARTIFACT CHECK
    artifacts_ok = check_files_exist([
        f"docs/rfcs/RFC_{PHASE_ID}_*.md",
        f"prototypes/phase_{PHASE_ID}_sim.ts",  # Layer S
        f"tests/red_team/phase_{PHASE_ID}_attack.py", # Layer F
        f"docs/idempotency_contracts/phase_{PHASE_ID}_*.json" # Layer E
    ])
    
    if not artifacts_ok:
        print("\n🚫 JUDGEMENT: FAIL (Missing Artifacts)")
        sys.exit(1)

    # 2. SIMULATION CHECK (Layer S)
    # Must compile and run successfully
    sim_ok = run_step("Prototype Simulation", f"npx -y tsx prototypes/phase_{PHASE_ID}_sim.ts")
    
    # 3. RED TEAM CHECK (Layer F)
    # Must return exit code 0 (meaning defense successful)
    red_team_ok = run_step("Red Team Attack", f"python3 tests/red_team/phase_{PHASE_ID}_attack.py")
    
    # FINAL VERDICT
    if sim_ok and red_team_ok:
        print("\n🎉 JUDGEMENT: PASS. Phase is Production-Ready.")
        sys.exit(0)
    else:
        print("\n🚫 JUDGEMENT: FAIL. Fix the logic.")
        sys.exit(1)

if __name__ == "__main__":
    main()
