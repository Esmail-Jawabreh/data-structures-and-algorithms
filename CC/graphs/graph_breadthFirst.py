from collections import deque


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        """
        Add a node to the graph.

        Args:
            node: The node to be added to the graph.
        """
        self.nodes[node] = []

    def add_edge(self, node1, node2):
        """
        Add an edge between two nodes in the graph.

        Args:
            node1: The first node of the edge.
            node2: The second node of the edge.
        """
        self.nodes[node1].append(node2)
        self.nodes[node2].append(node1)

    def breadth_first(self, start_node):
        """
        Perform a breadth-first search on the graph starting from a given node.

        Args:
            start_node: The node to start the breadth-first search from.

        Returns:
            A list containing the nodes visited in breadth-first order.
        """
        visited = set()
        queue = deque([start_node])
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                neighbors = self.nodes[node]
                queue.extend(neighbors)

        return result
