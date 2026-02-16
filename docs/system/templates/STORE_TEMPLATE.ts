import { create } from 'zustand';
import { Telemetry } from '@/utils/Telemetry';

/**
 * MAESTRO STORE PATTERN [PHASE_ID]
 * 
 * Rules:
 * 1. Every state mutation MUST emit a Telemetry signal.
 * 2. Mandatory 'status' field for Systemic Monitoring.
 * 3. Ready for SyncAdapter integration (Layer D).
 */

interface[PHASE_NAME]State {
    data: any[];
    status: 'IDLE' | 'SYNCING' | 'ERROR';
    lastUpdated: number;

    // Actions
    addItem: (item: any) => void;
    setStatus: (status: [PHASE_NAME]State['status']) => void;
}

export const use[PHASE_NAME]Store = create < [PHASE_NAME]State> ((set, get) => ({
    data: [],
    status: 'IDLE',
    lastUpdated: Date.now(),

    addItem: (item: any) => {
        set((state) => ({
            data: [...state.data, item],
            lastUpdated: Date.now()
        }));

        // Mandatory Telemetry Emit
        Telemetry.emit({
            domain: '[DOMAIN]',
            phase: '[PHASE_ID]',
            type: 'ACTION',
            payload: { action: 'ADD_ITEM', itemId: item.id }
        });
    },

    setStatus: (status) => set({ status }),
}));
