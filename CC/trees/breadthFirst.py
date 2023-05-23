from CC.trees.theNode import Node
from collections import deque


def breadth_first(tree):
    """
    Performs a breadth-first search on a tree and returns a list of all values encountered in the order they were visited.

    Args:
        tree (Node): The root node of the tree to traverse.

    Returns:
        list: A list of values encountered during the breadth-first search.
    """

    # Check if the tree is empty
    if not tree:
        return []

    queue = deque()
    queue.append(tree)

    orderedValues = []

    # Perform breadth-first search
    while queue:
        node = queue.popleft()
        orderedValues.append(node.value)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return orderedValues
