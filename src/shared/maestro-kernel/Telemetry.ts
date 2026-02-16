/**
 * GROMADA TELEMETRY SYSTEM
 * Location: src/utils/Telemetry.ts
 * 
 * Mandate: Provide a unified way to emit systemic signals for health monitoring.
 * Used in Chapter 3.2 of the RFC standard.
 */

type SignalLevel = 'INFO' | 'WARN' | 'ERROR' | 'CRITICAL';

interface Signal {
    phase: string;
    event: string;
    level: SignalLevel;
    context?: Record<string, any>;
    timestamp: number;
}

class TelemetryEngine {
    private static instance: TelemetryEngine;
    private history: Signal[] = [];
    private readonly MAX_HISTORY = 100;

    private constructor() { }

    static getInstance(): TelemetryEngine {
        if (!TelemetryEngine.instance) {
            TelemetryEngine.instance = new TelemetryEngine();
        }
        return TelemetryEngine.instance;
    }

    /**
     * Emit a systemic signal.
     */
    emit(phase: string, event: string, level: SignalLevel = 'INFO', context?: Record<string, any>) {
        const signal: Signal = {
            phase,
            event,
            level,
            context,
            timestamp: Date.now()
        };

        this.history.unshift(signal);
        if (this.history.length > this.MAX_HISTORY) {
            this.history.pop();
        }

        // Log to console in development
        const color = this.getLevelColor(level);
        console.log(
            `%c[${phase}] %c${event}`,
            `color: ${color}; font-weight: bold`,
            'color: inherit',
            context || ''
        );

        // Here we could sync to a central monitoring node in Phase 38
    }

    private getLevelColor(level: SignalLevel): string {
        switch (level) {
            case 'CRITICAL': return '#ff0000';
            case 'ERROR': return '#ff4444';
            case 'WARN': return '#ffbb33';
            default: return '#00C851';
        }
    }

    getHistory() {
        return this.history;
    }
}

export const Telemetry = TelemetryEngine.getInstance();
