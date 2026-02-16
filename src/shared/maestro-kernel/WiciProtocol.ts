import { Telemetry } from './Telemetry';

/**
 * WICI PROTOCOL (Splot)
 * 
 * Mandate: Unified Peer-to-Peer Synchronization Engine.
 * Uses LCRDT (Last Creator Wins) based on Lamport Clocks.
 */

export interface WiciPacket {
    id: string;          // UUID v4
    domain: string;
    phase: string;
    node_id: string;
    lamport_clock: number;
    tag: 'DELTA' | 'SNAPSHOT';
    payload: any;
    timestamp: number;
}

export class WiciProtocol {
    private localClock: number = 0;
    private readonly nodeId: string;
    private seenPackets: Set<string> = new Set();

    constructor() {
        this.nodeId = `node-${Math.random().toString(36).substring(7)}`;
    }

    /**
     * Prepare a packet for broadcasting
     */
    createPacket(domain: string, phase: string, payload: any): WiciPacket {
        this.localClock++;
        return {
            id: crypto.randomUUID(),
            domain,
            phase,
            node_id: this.nodeId,
            lamport_clock: this.localClock,
            tag: 'DELTA',
            payload,
            timestamp: Date.now()
        };
    }

    /**
     * Process an incoming packet with LCRDT logic
     */
    receive(packet: WiciPacket, currentState: any): { shouldUpdate: boolean; newState?: any } {
        // 1. Idempotency Check
        if (this.seenPackets.has(packet.id)) {
            return { shouldUpdate: false };
        }
        this.seenPackets.add(packet.id);

        // 2. Lamport Clock Sync
        this.localClock = Math.max(this.localClock, packet.lamport_clock);

        // 3. Conflict Resolution (LCRDT - Last Creator Wins)
        // In a real generic implementation, we would compare item-level timestamps.
        // For now, we return the decision to the adapter.

        Telemetry.emit('SYNC', 'Packet Received', 'INFO', {
            from: packet.node_id,
            phase: packet.phase
        });

        return { shouldUpdate: true };
    }
}

export const wici = new WiciProtocol();
