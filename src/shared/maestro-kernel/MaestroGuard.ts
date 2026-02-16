import { Telemetry } from './Telemetry';

/**
 * MAESTRO IDEMPOTENCY GUARD
 * 
 * Mandate: Enforce Layer E contracts at runtime.
 * Prevents replay attacks and double-spending by validating transactions against contracts.
 */

interface IdempotencyContract {
    phase: string;
    operations: Record<string, {
        unique_key: string[]; // Fields that define uniqueness
        ttl_ms?: number;
    }>;
}

class MaestroGuard {
    private static instance: MaestroGuard;
    private processedIds: Map<string, number> = new Map(); // key -> timestamp

    private constructor() { }

    static getInstance(): MaestroGuard {
        if (!MaestroGuard.instance) {
            MaestroGuard.instance = new MaestroGuard();
        }
        return MaestroGuard.instance;
    }

    /**
     * Validate an operation against an idempotency contract.
     * Returns true if the operation is valid (new), false if it's a duplicate.
     */
    validate(contract: IdempotencyContract, operationName: string, data: Record<string, any>): boolean {
        const config = contract.operations[operationName];
        if (!config) {
            Telemetry.emit(contract.phase, 'Contract Violation', 'CRITICAL', {
                error: 'Operation not defined in contract',
                operationName
            });
            return false;
        }

        // Generate unique fingerprint based on contract keys
        const fingerprint = config.unique_key
            .map(key => data[key])
            .join('|');

        if (this.processedIds.has(fingerprint)) {
            Telemetry.emit(contract.phase, 'Duplicate Prevented', 'WARN', {
                operationName,
                fingerprint
            });
            return false;
        }

        // Record successful operation
        this.processedIds.set(fingerprint, Date.now());
        return true;
    }

    /**
     * Cleanup old IDs based on TTL
     */
    gc(ttl_ms: number = 3600000) { // Default 1 hour
        const now = Date.now();
        for (const [key, timestamp] of this.processedIds.entries()) {
            if (now - timestamp > ttl_ms) {
                this.processedIds.delete(key);
            }
        }
    }
}

export const Guard = MaestroGuard.getInstance();
