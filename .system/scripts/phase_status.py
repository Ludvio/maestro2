#!/usr/bin/env python3
"""
Maestro Phase Navigator - Antigravity Extension
Purpose: Maps phase IDs to their distributed contracts, plans, and metrics.
Usage: python3 .agent/scripts/phase_status.py [phase_id]
"""

import json
import os
import sys
from typing import List, Dict, Any, Optional

# Configuration
DOCS_ROOT = "docs"
PHASES_MAP = {
    "01": "phase_01_interaction_fixes.md",
    "02": "phase_02_persistence_logic.md",
    "03": "phase_03_auth_profiles.md",
    "04": "phase_04_barter_engine.md",
    "05": "phase_05_bulk_buy_logic.md",
    "06": "phase_06_governance_logic.md",
    "07": "phase_07_tool_library_logic.md",
    "08": "phase_08_alert_system.md",
    "09": "phase_09_legal_generation.md",
    "10": "phase_10_intelligence_prices.md",
    "11": "phase_11_demographic_layer.md",
    "12": "phase_12_polish_launch.md"
}

def load_json(path: str) -> List[Any]:
    try:
        if not os.path.exists(path):
            return []
        with open(path, 'r') as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except Exception:
        return []

def get_phase_info(phase_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve full context for a specific phase."""
    plan_file = PHASES_MAP.get(phase_id)
    if not plan_file:
        return None

    # Load Contracts
    contracts_path = os.path.join(DOCS_ROOT, "idempotency_contracts", "contracts.json")
    all_contracts = load_json(contracts_path)
    contracts = [c for c in all_contracts if isinstance(c, dict) and c.get("phase_id") == phase_id]

    # Load Metrics
    metrics_path = os.path.join(DOCS_ROOT, "observability", "metrics.json")
    all_metrics = load_json(metrics_path)
    metrics = [m for m in all_metrics if isinstance(m, dict) and m.get("phase_id") == phase_id]

    return {
        "id": phase_id,
        "plan_path": os.path.join(DOCS_ROOT, "implementation_plans", plan_file),
        "contracts": contracts,
        "metrics": metrics
    }

def print_status(phase_id: str):
    info = get_phase_info(phase_id)
    if not info:
        print(f"Phase {phase_id} not found.")
        sys.exit(1)

    print(f"=== PHASE {phase_id} CONTEXT ===")
    print(f"Plan File: {info['plan_path']}")
    
    print("\n--- 🛡️ Idempotency Contracts ---")
    if info['contracts']:
        for c in info['contracts']:
            print(f"- Action: {c.get('action')}")
            contract = c.get('contract', {})
            print(f"  Key: {contract.get('idempotency_key_source')}")
            print(f"  Behavior: {contract.get('behavior_on_retry')}")
    else:
        print("No contracts defined yet.")

    print("\n--- 🕵️ Observability Metrics ---")
    if info['metrics']:
        for m in info['metrics']:
            print(f"- Metric: {m.get('success_metric')} ({m.get('threshold')})")
            print(f"  Log Pattern: {m.get('log_pattern')}")
    else:
        print("No metrics defined yet.")

    print("\n--- 🔄 Reliability Layers ---")
    plan_path = str(info['plan_path'])
    try:
        with open(plan_path, 'r') as f:
            content = f.read()
            if "## 🔄 Idempotency & Degraded Mode" in content:
                print(content.split("## 🔄 Idempotency & Degraded Mode")[1].strip())
            else:
                print("Reliability layers not yet documented in plan.")
    except Exception as e:
        print(f"Could not read plan file for reliability details: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 phase_status.py <phase_id>")
        sys.exit(1)
    
    print_status(sys.argv[1])
