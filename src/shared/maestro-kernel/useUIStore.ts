import { create } from 'zustand';
import { Telemetry } from './Telemetry';

/**
 * MAESTRO NARRATIVE ENGINE (useUIStore)
 * 
 * Mandate: Manage the flow of narrative events and global UI state.
 * Implements INV-01-01: Global Priority Cap.
 */

export interface NarrativeEvent {
    id: string;
    phase: string;
    level: 'INFO' | 'WARN' | 'ERROR' | 'CRITICAL';
    title: string;
    message: string;
    category: string; // e.g., 'SYSTEM', 'USER', 'ECONOMY'
    timestamp: number;
    type: 'TOAST' | 'CARD';
}

interface UIState {
    activeToasts: NarrativeEvent[];
    addEvent: (event: Omit<NarrativeEvent, 'id' | 'timestamp'>) => void;
    dismissToast: (id: string) => void;
}

export const useUIStore = create<UIState>((set, get) => ({
    activeToasts: [],

    addEvent: (eventData) => {
        const id = Math.random().toString(36).substring(7);
        const timestamp = Date.now();
        const event: NarrativeEvent = { ...eventData, id, timestamp };

        // INV-01: Global Priority Cap
        // Prevents UI flood by downgrading toasts to cards if many are active.
        const currentToasts = get().activeToasts;
        if (event.type === 'TOAST' && currentToasts.length >= 3) {
            event.type = 'CARD';
            Telemetry.emit('NARRATIVE', 'Toast Overflow', 'WARN', { id });
        }

        if (event.type === 'TOAST') {
            set((state) => ({ activeToasts: [...state.activeToasts, event] }));
            // Auto-dismiss toast after 5s
            setTimeout(() => get().dismissToast(id), 5000);
        }

        // Send to Telemetry for systemic visibility
        Telemetry.emit(event.phase, event.title, event.level, { ...event });
    },

    dismissToast: (id) => set((state) => ({
        activeToasts: state.activeToasts.filter(t => t.id !== id)
    })),
}));
