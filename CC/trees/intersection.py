from CC.trees.theNode import Node


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        """
        Add a node with the given value to the binary tree.

        Args:
            value: The value to be added to the binary tree.
        """
        if not self.root:
            self.root = Node(value)
        else:
            self._add_recursive(value, self.root)

    def _add_recursive(self, value, current_node):
        """
        Recursively add a node with the given value to the binary tree.

        Args:
            value: The value to be added to the binary tree.
            current_node: The current node being considered during the recursive traversal.
        """
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._add_recursive(value, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._add_recursive(value, current_node.right)

    def inorder_traversal(self):
        """
        Perform an inorder traversal of the binary tree.

        Returns:
            A list containing the values of the nodes in the binary tree in inorder traversal order.
        """
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result

    def _inorder_traversal_recursive(self, current_node, result):
        """
        Recursively perform an inorder traversal of the binary tree.

        Args:
            current_node: The current node being considered during the recursive traversal.
            result: The list to store the values of the nodes in inorder traversal order.
        """
        if current_node is not None:
            self._inorder_traversal_recursive(current_node.left, result)
            result.append(current_node.value)
            self._inorder_traversal_recursive(current_node.right, result)


def tree_intersection(tree1, tree2):
    """
    Find the intersection of values between two binary trees.

    Args:
        tree1: The first binary tree.
        tree2: The second binary tree.

    Returns:
        A set of values that are found in both binary trees.
    """
    values1 = tree1.inorder_traversal()
    values2 = tree2.inorder_traversal()
    intersection = set(values1) & set(values2)
    return intersection
