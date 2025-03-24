from collections import deque
from typing import Dict, List

def bfs(graph: Dict[str, List[str]], start: str) -> List[str]:
    """
    Perform a breadth-first search (BFS) on a given graph from a start node.

    :param graph: A dictionary where keys are node labels and
                  values are lists of adjacent nodes.
    :param start: The starting node label for the BFS.
    :return: A list of node labels in the order they were visited.
    """
    # Precondition: start must be a key in the graph
    assert start in graph, "Precondition: 'start' must exist in the graph."

    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            # Branching: only add neighbor if it has not been visited
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # Postcondition: The number of visited nodes must match the length of 'order'
    assert len(visited) == len(order), "Postcondition: visited/order size mismatch."

    return order
