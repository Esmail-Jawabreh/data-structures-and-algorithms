from CC.trees.binaryTree import *


class BinarySearchTree(BinaryTree):
    def add(self, value):
        """
        Add a new node with the given value in the correct location in the binary search tree.

        Returns:
            None
        """

        if self.root is None:
            self.root = Node(value)
        else:
            self._add_helper(self.root, value)

    def _add_helper(self, node, value):
        """
        Recursive helper function to add a new node with the given value in the correct location.

        Returns:
            None
        """

        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add_helper(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add_helper(node.right, value)

    def contains(self, value):
        """
        Check if the given value is present in the binary search tree.

        Returns:
            bool: True if the value is found, False otherwise.
        """

        return self._contains_helper(self.root, value)

    def _contains_helper(self, node, value):
        """
        Recursive helper function to check if the given value is present in the binary search tree.

        Returns:
            bool: True if the value is found, False otherwise.
        """

        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._contains_helper(node.left, value)
        else:
            return self._contains_helper(node.right, value)
