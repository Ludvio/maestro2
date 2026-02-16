import os
import subprocess
import sys

def run_all_simulations():
    print("🌊 GROMADA GLOBAL SIMULATION RUNNER")
    print("-" * 40)
    
    sim_dir = "tests/evals"
    if not os.path.exists(sim_dir):
        # Fallback to prototypes if evals doesn't exist yet
        sim_dir = "prototypes"
        
    sim_files = [f for f in os.listdir(sim_dir) if f.endswith("_sim.ts") or f.startswith("eval_phase_")]
    
    if not sim_files:
        print("🟡 No simulation scripts found.")
        return True

    success_count = 0
    fail_count = 0

    for sim in sorted(sim_files):
        print(f"🚀 Running {sim}...", end=" ", flush=True)
        try:
            # Using npx ts-node to run the simulation
            result = subprocess.run(
                ["npx", "ts-node", os.path.join(sim_dir, sim)],
                capture_output=True,
                text=True,
                timeout=30 # 30 seconds timeout per sim
            )
            
            if result.returncode == 0:
                print("✅ PASSED")
                success_count += 1
            else:
                print("❌ FAILED")
                print(f"   Error: {result.stderr.splitlines()[-1] if result.stderr.splitlines() else 'Unknown error'}")
                fail_count += 1
        except subprocess.TimeoutExpired:
            print("⏰ TIMEOUT")
            fail_count += 1
        except Exception as e:
            print(f"💥 ERROR: {str(e)}")
            fail_count += 1

    print("-" * 40)
    print(f"TOTAL: {len(sim_files)} | PASSED: {success_count} | FAILED: {fail_count}")
    
    return fail_count == 0

if __name__ == "__main__":
    if not run_all_simulations():
        sys.exit(1)
    sys.exit(0)
