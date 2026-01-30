import pytest

from cycle_detection import has_cycle


@pytest.mark.parametrize("graph,expected", [
    # simple cycle: 1 → 2 → 3 → 1
    ({1: [2], 2: [3], 3: [1]}, True),

    # no cycle: 1 → 2 → 3
    ({1: [2], 2: [3], 3: []}, False),

    # self-loop
    ({1: [1]}, True),

    # diamond shape, no cycle
    ({1: [2, 3], 2: [4], 3: [4], 4: []}, False),

    # disconnected graph with cycle in one component
    ({1: [2], 2: [], 3: [4], 4: [3]}, True),

    # disconnected graph, no cycles
    ({1: [2], 2: [], 3: [4], 4: []}, False),

    # empty graph
    ({}, False),

    # single vertex, no edges
    ({1: []}, False),

    # long chain with back edge
    ({1: [2], 2: [3], 3: [4], 4: [5], 5: [2]}, True),

    # two separate cycles
    ({1: [2], 2: [1], 3: [4], 4: [3]}, True),
])
def test_has_cycle(graph, expected):
    assert has_cycle(graph) is expected


@pytest.fixture
def large_chain():
    """Chain graph with 1000 vertices, no cycle."""
    return {i: [i + 1] for i in range(1, 1000)} | {1000: []}


@pytest.fixture
def large_chain_with_cycle():
    """Chain graph with 1000 vertices, back edge to start."""
    return {i: [i + 1] for i in range(1, 1000)} | {1000: [1]}


@pytest.fixture
def two_components_with_cycle():
    """Two disconnected components: {1→2→3} and {4→5→6→4} (cycle)."""
    return {
        1: [2], 2: [3], 3: [],
        4: [5], 5: [6], 6: [4],
    }


@pytest.fixture
def two_components_no_cycle():
    """Two disconnected components: {1→2→3} and {4→5→6}, no cycles."""
    return {
        1: [2], 2: [3], 3: [],
        4: [5], 5: [6], 6: [],
    }


def test_two_components_with_cycle(two_components_with_cycle):
    assert has_cycle(two_components_with_cycle) is True


def test_two_components_no_cycle(two_components_no_cycle):
    assert has_cycle(two_components_no_cycle) is False


def test_large_graph_no_cycle(large_chain):
    assert has_cycle(large_chain) is False


def test_large_graph_with_cycle(large_chain_with_cycle):
    assert has_cycle(large_chain_with_cycle) is True

