from CC.hashTables.hashTables import Hashtable
from CC.trees.tree import Tree
from CC.trees.theNode import Node


def tree_intersection(first, second):
    """
    Find the common values between two binary search trees.

    Arguments:
    - first (BinarySearchTree): The first binary search tree.
    - second (BinarySearchTree): The second binary search tree.

    Returns:
    - list: A list of common values found in both binary search trees.
    """
    hash = Hashtable()
    commen = []

    tree1 = first.in_order()
    tree2 = second.in_order()

    for node1 in tree1:
        hash.set(node1, True)

    for node2 in tree2:
        if hash.has(node2):
            commen.append(node2)
    return commen
