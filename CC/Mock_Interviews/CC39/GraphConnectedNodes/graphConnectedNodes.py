from collections import defaultdict, deque


def are_connected(graph, node1, node2):
    adj_list = defaultdict(list)
    for node, neighbors in graph.items():
        adj_list[node].extend(neighbors)

    children = deque([node1])
    visited = set([node1])

    while children:
        current = children.popleft()
        if current == node2:
            return True

        for neighbor in adj_list[current]:
            if neighbor not in visited:
                children.append(neighbor)
                visited.add(neighbor)

    return False
