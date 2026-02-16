import os
import subprocess
import time
import json
import sys

# Orchestration: System | Layer V (Watchman)
# Description: Non-blocking System Integrity Monitor. 
# Mandate: Run in background. Report findings via status board. NEVER block the user.

LOG_FILE = "docs/strategic/SYSTEM_HEALTH.md"

def update_health_board(phase_id, status, details):
    with open(LOG_FILE, "a") as f:
        f.write(f"\n| {time.strftime('%H:%M:%S')} | {phase_id} | {status} | {details} |")

def run_fuzzer(phase_id):
    """Run the fast Layer F fuzzer (Pure JS/TS, no browser)."""
    fuzzer_path = f"prototypes/phase_{phase_id}_fuzzer.js"
    if not os.path.exists(fuzzer_path):
        return "SKIP", "No Fuzzer found."
    
    try:
        result = subprocess.run(["node", fuzzer_path], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            return "✅ PASS", "Invariants held."
        else:
            return "❌ CRITICAL", "Invariant violation detected!"
    except Exception as e:
        return "⚠️ ERROR", str(e)

def run_background_homunculus(phase_id):
    """Trigger the slow Layer A agent in a truly detached process."""
    # This just starts it; we don't wait for completion here.
    # It will write its own results to the health board later.
    command = f"npx playwright test tests/agentic/homunculus_survival.spec.ts --project=chromium > /dev/null 2>&1 &"
    os.system(command)
    return "🚀 STARTED", "Agent Jan navigating live environment."

def main():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("# 🩺 SYSTEM HEALTH BOARD (Non-Blocking Audit)\n")
            f.write("| Time | Phase | Status | Details |\n")
            f.write("| :--- | :--- | :--- | :--- |\n")

    # Example: Check current working phase
    # In a real Maestro setup, this would iterate through all "In Progress" phases
    active_phases = ["24"] 
    
    for p in active_phases:
        # 1. Fast Check (Layer F)
        status, details = run_fuzzer(p)
        update_health_board(p, status, details)
        
        # 2. Slow Check Trigger (Layer A)
        if status == "✅ PASS":
            # Only run heavy simulation if the basic physics hold
            run_status, run_details = run_background_homunculus(p)
            update_health_board(p, run_status, run_details)

if __name__ == "__main__":
    main()
