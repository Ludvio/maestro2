
import { TrustGraph, TrustEdge } from '../src/domain/trust/TrustGraph';
import { StewardshipManager, ResourceItem } from '../src/domain/stewardship/StewardshipManager';

function assert(condition: boolean, msg: string) {
    if (!condition) {
        console.error(`❌ FAILED: ${msg}`);
        process.exit(1);
    } else {
        console.log(`✅ PASSED: ${msg}`);
    }
}

async function testRod() {
    console.log('--- Testing ROD (Web of Trust) ---');
    const graph = new TrustGraph();

    // A -> B (Family - 100%)
    graph.addEdge({
        id: '1', sourceId: 'A', targetId: 'B', level: 'Family', context: 'general', timestamp: Date.now()
    });

    // B -> C (Vouched - 80%)
    graph.addEdge({
        id: '2', sourceId: 'B', targetId: 'C', level: 'Vouched', context: 'general', timestamp: Date.now()
    });

    // C -> D (Suspicious - 10%)
    graph.addEdge({
        id: '3', sourceId: 'C', targetId: 'D', level: 'Suspicious', context: 'general', timestamp: Date.now()
    });

    // A -> C should be 100% * 80% = 80% (or slightly decayed by depth if implemented)
    // Actually our implementation multiplies: 1.0 * 0.8 = 0.8 -> 80%
    const trustAC = graph.getTrustScore('A', 'C');
    console.log(`Trust A -> C: ${trustAC}`);
    assert(trustAC === 80, 'Trust transitive calculation A->B->C');

    // A -> D should be 100% * 80% * 10% = 8%
    const trustAD = graph.getTrustScore('A', 'D');
    console.log(`Trust A -> D: ${trustAD}`);
    assert(trustAD < 10, 'Trust transitive calculation A->B->C->D (Suspicious)');
}


async function testStewardship() {
    console.log('\n--- Testing STEWARDSHIP (Custody) ---');

    const drill: ResourceItem = {
        id: 'drill-1',
        name: 'Hammer Drill',
        ownerId: 'community',
        currentCustodianId: 'A',
        chainOfCustody: [],
        state: 'Available',
        conditionScore: 100
    };

    const manager = new StewardshipManager([drill]);

    // Attempt Transfer A -> B
    const signature = "sig-valid";
    const condition = "cond-ok";

    const success = manager.transferCustody('drill-1', 'B', signature, condition);
    assert(success, 'Custody transfer should succeed');

    const updatedDrill = manager.getResource('drill-1');
    assert(updatedDrill?.currentCustodianId === 'B', 'Custodian updated to B');
    assert(updatedDrill?.state === 'InCustody', 'State updated to InCustody');
    assert(updatedDrill?.chainOfCustody.length === 1, 'Chain of custody event added');
}

async function main() {
    try {
        await testRod();
        await testStewardship();
        console.log('\n🎉 ALL WHITEHOT TESTS PASSED');
    } catch (e) {
        console.error(e);
        process.exit(1);
    }
}

main();
