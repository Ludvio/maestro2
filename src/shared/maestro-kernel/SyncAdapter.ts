import { wici, WiciPacket } from './WiciProtocol';
import { Telemetry } from './Telemetry';

/**
 * SYNC ADAPTER
 * 
 * Mandate: Bridge existing Zustand stores with the Wici Protocol.
 * Strategy: Non-Destructive Retrofitting.
 */

export interface SyncableStore {
    id: string;
    domain: string;
    applySync: (payload: any) => void;
}

export class SyncAdapter {
    private stores: Map<string, SyncableStore> = new Map();

    register(store: SyncableStore) {
        this.stores.set(store.id, store);
        Telemetry.emit('SYNC', 'Store Registered', 'INFO', { id: store.id });
    }

    /**
     * Broadcast a change from a local store
     */
    broadcast(storeId: string, payload: any) {
        const store = this.stores.get(storeId);
        if (!store) return;

        const packet = wici.createPacket(store.domain, store.id, payload);

        // In a real P2P mesh, we'd send via WebRTC/Socket here.
        // For now, we simulate a broadcast to the window (local sync)
        window.dispatchEvent(new CustomEvent('wici-broadcast', { detail: packet }));

        Telemetry.emit(store.id, 'Changes Broadcasted', 'INFO', { clock: packet.lamport_clock });
    }

    /**
     * Handle incoming broadcast
     */
    listen() {
        window.addEventListener('wici-broadcast', (event: any) => {
            const packet = event.detail as WiciPacket;
            const store = this.stores.get(packet.phase);

            if (store) {
                const { shouldUpdate } = wici.receive(packet, null);
                if (shouldUpdate) {
                    store.applySync(packet.payload);
                }
            }
        });
    }
}

export const syncAdapter = new SyncAdapter();
syncAdapter.listen();
