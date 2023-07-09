from CC.trees.binaryTree import *
from CC.trees.theNode import *


def in_order(root):
    """
    Perform an in-order traversal of the binary tree rooted at `root`.

    This function traverses the binary tree and stores the value of each node in a dictionary (hashmap) as a key-value pair.
    The resulting dictionary is returned at the end.

    Args:
        root: The root node of the binary tree.

    Returns:
        A dictionary containing the values of each node in the binary tree.
    """
    if root == None:
        return {}
    hashmap = {}

    def recursive(root):
        if root.right:
            recursive(root.left)
        hashmap[root.value] = root.value
        if root.right:
            recursive(root.right)

    recursive(root)
    return hashmap


def tree_intersection(rootone, roottwo):
    """
    Find the intersection of two binary trees using in-order traversal.

    This function calls the `in_order` function to obtain the values of nodes in the first tree and stores them in a hashmap.
    Then, it declares a dictionary to store the intersected node values found while traversing the second tree.
    The intersected node values are added to the dictionary using a recursive function.
    Finally, the intersected node values are returned as a list.

    Args:
        rootone: The root node of the first binary tree.
        roottwo: The root node of the second binary tree.

    Returns:
        A list containing the values of nodes that are present in both binary trees.
    """
    hashmap = in_order(rootone)
    intersection_node = {}
    if roottwo.value in hashmap:
        intersection_node[roottwo.value] = roottwo.value

    def recursive(root):
        """
        Recursive helper function to find intersected nodes in the second tree.

        This function loops through the second tree to find the intersected nodes by checking if each node's value
        is present in the hashmap dictionary obtained from the first tree.

        Args:
            root: The current node being processed in the second tree.
        """
        if root.left:
            if root.left.value in hashmap:
                intersection_node[root.left.value] = root.left.value
            recursive(root.left)
        if root.right:
            if root.right.value in hashmap:
                intersection_node[root.right.value] = root.right.value
            recursive(root.right)

    recursive(roottwo)
    result = list(intersection_node.keys())

    return result
