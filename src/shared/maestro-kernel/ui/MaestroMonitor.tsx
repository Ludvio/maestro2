import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Telemetry } from '../Telemetry';
import { useUIStore, NarrativeEvent } from '../useUIStore';

/**
 * MAESTRO SYSTEM MONITOR (Telemetry HUD)
 * 
 * Mandate: Provide real-time visibility into cross-domain events.
 * Use this component to visualize the 'Systemic Pulse'.
 */

export const MaestroMonitor: React.FC = () => {
    const [events, setEvents] = useState<NarrativeEvent[]>([]);

    useEffect(() => {
        const syncHistory = () => {
            const history = Telemetry.getHistory();
            const narrativeEvents: NarrativeEvent[] = history.map(h => ({
                id: `sys-${h.timestamp}-${h.event}`,
                phase: h.phase,
                level: h.level,
                title: h.event,
                message: typeof h.context === 'string' ? h.context : JSON.stringify(h.context),
                category: (h.context?.category as string) || 'SYSTEM',
                timestamp: h.timestamp,
                type: 'CARD'
            }));
            setEvents(narrativeEvents);
        };

        const interval = setInterval(syncHistory, 1000);
        return () => clearInterval(interval);
    }, []);

    return (
        <div className="flex flex-col gap-4">
            <header className="flex justify-between items-center px-2">
                <h2 className="text-xs font-bold text-white/40 uppercase tracking-widest">Systemic Pulse</h2>
                <div className="h-2 w-2 bg-green-500 rounded-full animate-pulse" />
            </header>

            <AnimatePresence mode="popLayout">
                {events.map((ev, idx) => (
                    <motion.div
                        key={ev.id}
                        initial={{ opacity: 0, x: -10 }}
                        animate={{ opacity: 1, x: 0 }}
                        exit={{ opacity: 0, scale: 0.95 }}
                        transition={{ delay: idx * 0.05 }}
                        className="p-4 bg-white/5 border border-white/10 rounded-2xl backdrop-blur-md"
                    >
                        <div className="flex items-center gap-3 mb-2">
                            <span className={`h-2 w-2 rounded-full ${ev.level === 'CRITICAL' ? 'bg-red-500' :
                                    ev.level === 'WARN' ? 'bg-amber-500' : 'bg-blue-500'
                                }`} />
                            <span className="text-[10px] font-mono text-white/30 uppercase">
                                {ev.phase} • {new Date(ev.timestamp).toLocaleTimeString()}
                            </span>
                        </div>
                        <h4 className="text-sm font-bold text-white/90">{ev.title}</h4>
                        <p className="text-xs text-white/50 leading-relaxed truncate">{ev.message}</p>
                    </motion.div>
                ))}
            </AnimatePresence>

            {events.length === 0 && (
                <div className="py-20 text-center border-2 border-dashed border-white/5 rounded-3xl">
                    <p className="text-xs text-white/20 italic">No signals detected on the mesh.</p>
                </div>
            )}
        </div>
    );
};
