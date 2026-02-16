
# Maestro Orchestration (Python Logic)
# Orchestrates the 8-layer generation process for a development phase.

import os
import sys
import shutil

# Configuration
TEMPLATES_DIR = ".agent/skills/maestro-prime/resources/templates"
DOCS_DIR = "docs"
TESTS_DIR = "tests"

PHASE_ID = sys.argv[1] # e.g., "15"
PHASE_NAME = sys.argv[2] # e.g., "merit_ledger"

def ensure_dirs():
    """Ensures target directories exist."""
    print(">>> [Orchestrator] Ensuring directory structure...")
    os.makedirs(f"{DOCS_DIR}/phases", exist_ok=True)
    os.makedirs(f"{DOCS_DIR}/decisions", exist_ok=True)
    os.makedirs(f"{DOCS_DIR}/implementation_plans", exist_ok=True)
    os.makedirs(f"{DOCS_DIR}/idempotency_contracts", exist_ok=True)
    os.makedirs(f"{TESTS_DIR}/plans", exist_ok=True)
    os.makedirs(f"{TESTS_DIR}/red_team", exist_ok=True)

def scaffold_phase():
    """Generates the 8 mandatory artifacts from templates."""
    print(f">>> [Orchestrator] Scaffolding artifacts for Phase {PHASE_ID}: {PHASE_NAME}...")

    # Layer 1: Business Milestone
    copy_template("TEMPLATE_01_BUSINESS_MILESTONE.md", f"{DOCS_DIR}/phases/MILESTONE_{PHASE_ID}_{PHASE_NAME.upper()}.md")
    
    # Layer 2: Constitution Check (Embedded or separate depending on file)
    # Layer 3: ADR (Reasoning)
    # Note: No template for ADR currently exists in input, creating stub
    create_stub(f"{DOCS_DIR}/decisions/ADR_{PHASE_ID}_{PHASE_NAME}_REASONING.md", "# Architecture Decision Record")

    # Layer 4: Tech Plan
    copy_template("TEMPLATE_02_IMPLEMENTATION_PLAN.md", f"{DOCS_DIR}/implementation_plans/phase_{PHASE_ID}_{PHASE_NAME}.md")

    # Layer 5: Contract JSON
    copy_template("TEMPLATE_03_CONTRACT.json", f"{DOCS_DIR}/idempotency_contracts/phase_{PHASE_ID}_{PHASE_NAME}.json")

    # Layer 6: Red Team Script
    copy_template("TEMPLATE_07_RED_TEAM_ATTACK.py", f"{TESTS_DIR}/red_team/phase_{PHASE_ID}_attack.py")

    # Layer 7: Test Plan
    copy_template("TEMPLATE_04_TEST_PLAN.md", f"{TESTS_DIR}/plans/phase_{PHASE_ID}_{PHASE_NAME}.spec.md")

    # Layer 8: Improvement Log
    copy_template("TEMPLATE_06_RECURSIVE_IMPROVEMENT.md", f"{DOCS_DIR}/improvements/phase_{PHASE_ID}_log.md")

    print(f">>> [Orchestrator] All 8 artifacts scaffolded successfully.")
    print(f">>> [Orchestrator] NEXT STEP: Fill in theoretical content using the 'Constitution' and 'Tech Standard'.")

def copy_template(src_name, dest_path):
    """Copies a template file to the destination."""
    src = f"{TEMPLATES_DIR}/{src_name}"
    if not os.path.exists(src):
        # Fallback for templates not in the resources dir yet
        src = f"docs/templates/{src_name}"
    
    if os.path.exists(src):
        shutil.copy(src, dest_path)
        print(f"    [+] Created: {dest_path}")
    else:
        print(f"    [!] ERROR: Template {src_name} not found.")

def create_stub(path, content):
    with open(path, "w") as f:
        f.write(content)
    print(f"    [+] Created Stub: {path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python orchestrate_phase.py [ID] [NAME]")
        sys.exit(1)
    
    ensure_dirs()
    scaffold_phase()
