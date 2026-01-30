from enum import Enum


class Color(Enum):
    """
    Vertex states during DFS traversal.

    WHITE: Not visited yet
    GRAY: Currently in the DFS stack (part of active path)
    BLACK: Fully processed (all descendants visited)

    A cycle exists when we encounter a GRAY vertex.
    """
    WHITE = 0
    GRAY = 1
    BLACK = 2


def has_cycle(graph: dict[int, list[int]]) -> bool:
    """
    Check if a directed graph contains a cycle.

    Uses iterative DFS with three-color marking.

    Args:
        graph: Adjacency list where key is vertex, value is list of neighbors.

    Returns:
        True if cycle exists, False otherwise.

    Example:
        >>> has_cycle({1: [2], 2: [3], 3: [1]})
        True
        >>> has_cycle({1: [2], 2: [3], 3: []})
        False
    """

    all_vertices = set(graph.keys())

    for neighbors in graph.values():
        all_vertices.update(neighbors)

    color = {v: Color.WHITE for v in all_vertices}

    def dfs_iterative(start: int) -> bool:
        stack = [(start, False)]

        while stack:
            vertex, is_exiting = stack.pop()

            if is_exiting:
                color[vertex] = Color.BLACK
                continue

            if color[vertex] != Color.WHITE:
                continue

            color[vertex] = Color.GRAY
            stack.append((vertex, True))

            for neighbor in graph.get(vertex, []):
                if color[neighbor] == Color.GRAY:
                    return True
                if color[neighbor] == Color.WHITE:
                    stack.append((neighbor, False))

        return False

    for vertex in all_vertices:
        if color[vertex] == Color.WHITE and dfs_iterative(vertex):
            return True

    return False
