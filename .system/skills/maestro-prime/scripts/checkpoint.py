# Description: Core orchestrator for Maestro phases. Manages state and layer progression.
# Orchestration: System | Global
import json
import os
import sys
from typing import Dict, Any, List, Optional, TypedDict

# !!! PROCESS CONSISTENCY WARNING !!!
# If you modify the layer structure or orchestration logic here, you MUST also update:
# 1. .agent/skills/maestro-prime/SKILL.md (The Capability Def)
# 2. .agent/workflows/generate_phase_artifacts.md (The User Manual)
# --------------------------------------------------------------------------

# Configuration
STATE_FILE = ".agent/state/active_phase.json"

class MaestroState(TypedDict):
    phaseId: Optional[int]
    phaseName: str
    completedLayers: List[str]
    nextAction: str
    artifacts: Dict[str, str]
    blockers: List[str]
    requiresSignoff: bool
    isSignedOff: bool
    reflectionNotes: str

def validate_metadata(file_path: str) -> None:
    """Check if file has the mandatory 2 lines of metadata at the top."""
    if not os.path.exists(file_path):
        return # Let other parts handle missing files
    
    try:
        with open(file_path, 'r') as f:
            lines = [f.readline().strip() for _ in range(10)]
            
        # Check first 10 lines
        content = " ".join(lines).lower()
        if "description" not in content or "orchestration" not in content:
            print(f"\n[!] ERROR: Missing mandatory metadata in {file_path}")
            print("[!] Every file MUST start with 2 lines of metadata (Description and Orchestration).")
            print("[!] Fixing this is REQUIRED before checkpointing.")
            sys.exit(1)
    except Exception as e:
        print(f"[!] Warning: Metadata validation failed for {file_path}: {e}")

def get_state() -> Dict[str, Any]:
    """Load current state or initialize."""
    default_state: Dict[str, Any] = {
        "phaseId": None,
        "phaseName": "",
        "completedLayers": [],
        "nextAction": "START",
        "artifacts": {},
        "blockers": [],
        "requiresSignoff": False,
        "isSignedOff": False,
        "reflectionNotes": ""
    }
    if not os.path.exists(STATE_FILE):
        return default_state
    try:
        with open(STATE_FILE, 'r') as f:
            data = json.load(f)
            if isinstance(data, dict):
                return data
    except Exception:
        pass
    return default_state

def update_state(phase_id: str, phase_name: str, new_layer: Optional[str] = None, new_artifact_path: Optional[str] = None) -> Dict[str, Any]:
    """Transition state to next layer."""
    if new_artifact_path:
        validate_metadata(new_artifact_path)
        
    state = get_state()
    
    # Initialize phase if new or first time
    current_id = state.get("phaseId")
    if current_id is None or current_id != int(phase_id):
        print(f"[*] Initializing/Resetting Phase {phase_id}...")
        state = {
            "phaseId": int(phase_id),
            "phaseName": phase_name,
            "completedLayers": [],
            "nextAction": "LAYER_0_REFLECTION",
            "artifacts": {},
            "blockers": [],
            "requiresSignoff": False,
            "isSignedOff": False,
            "reflectionNotes": ""
        }

    # Record completion
    if new_layer:
        completed = state.get("completedLayers")
        if isinstance(completed, list):
            if new_layer not in completed:
                completed.append(new_layer)
        
        if new_artifact_path:
            artifacts = state.get("artifacts")
            if isinstance(artifacts, dict):
                artifacts[new_layer] = new_artifact_path
        
        # Reset signoff for next layer
        state["isSignedOff"] = False

    # Determine Next Action
    layers = [
        "LAYER_0_REFLECTION", 
        "LAYER_A", 
        "LAYER_B", 
        "LAYER_C", 
        "LAYER_D", 
        "LAYER_S", 
        "LAYER_E", 
        "LAYER_F", 
        "LAYER_G", 
        "LAYER_I", 
        "LAYER_P", 
        "LAYER_H"
    ]
    
    next_action = "DONE"
    current_completed = state.get("completedLayers")
    if isinstance(current_completed, list):
        completed_set = set(current_completed)
        for layer in layers:
            if layer not in completed_set:
                next_action = layer
                break
            
    state["nextAction"] = next_action

    # Save
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=4)
        
    return state

def archive_phase():
    """Move active phase to history."""
    state = get_state()
    p_id = state.get("phaseId")
    if p_id is None:
        print("[!] No active phase to archive.")
        return

    history_dir = "docs/phases/history"
    os.makedirs(history_dir, exist_ok=True)
    archive_path = f"{history_dir}/PHASE_{p_id}_{state.get('phaseName')}.json"
    
    with open(archive_path, 'w') as f:
        json.dump(state, f, indent=4)
    
    print(f"[*] Successfully ARCHIVED Phase {p_id} to {archive_path}")
    # Reset active state
    if os.path.exists(STATE_FILE):
        os.remove(STATE_FILE)

def set_signoff(status: bool):
    """Manually approve or request signoff."""
    state = get_state()
    state["isSignedOff"] = status
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=4)
    print(f"[*] Sign-off status set to: {status}")

def print_status() -> None:
    state = get_state()
    p_id = state.get("phaseId")
    if p_id is None:
        print("\n--- No active phase found ---")
        return

    print(f"\n=== GROMADA ORCHESTRATOR STATUS ===")
    print(f"Phase: {p_id} - {state.get('phaseName', '')}")
    print(f"Next Action: {state.get('nextAction', '')}")
    
    signoff_icon = "✅" if state.get("isSignedOff") else "❌"
    print(f"Human Sign-off: {signoff_icon}")
    print("-" * 35)
    
    all_layers = [
        "LAYER_0_REFLECTION", 
        "LAYER_A", 
        "LAYER_B", 
        "LAYER_C", 
        "LAYER_D", 
        "LAYER_S", 
        "LAYER_E", 
        "LAYER_F", 
        "LAYER_G", 
        "LAYER_I", 
        "LAYER_P", 
        "LAYER_H"
    ]
    completed = state.get("completedLayers")
    completed_list = completed if isinstance(completed, list) else []
    
    artifacts = state.get("artifacts")
    artifacts_dict = artifacts if isinstance(artifacts, dict) else {}
    
    for layer in all_layers:
        status = "[DONE]" if layer in completed_list else "[PENDING]"
        path = artifacts_dict.get(layer, "")
        print(f"{status} {layer:<17} {path}")
    print("=" * 35 + "\n")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "archive":
        archive_phase()
    elif len(sys.argv) > 1 and sys.argv[1] == "sign":
        set_signoff(True)
    elif len(sys.argv) > 4:
        update_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        print_status()
    elif len(sys.argv) == 3:
        update_state(sys.argv[1], sys.argv[2])
        print_status()
    else:
        print_status()

