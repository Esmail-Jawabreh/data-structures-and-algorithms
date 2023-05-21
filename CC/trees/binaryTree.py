class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder_traversal(self, node):
        """
        Perform a preorder traversal of the binary tree.

        Returns:
            list: List of values in preorder traversal order.
        """

        if node is None:
            return []
        result = [node.value]
        result += self.preorder_traversal(node.left)
        result += self.preorder_traversal(node.right)
        return result

    def inorder_traversal(self, node):
        """
        Perform an inorder traversal of the binary tree.

        Returns:
            list: List of values in inorder traversal order.
        """

        if node is None:
            return []
        result = self.inorder_traversal(node.left)
        result.append(node.value)
        result += self.inorder_traversal(node.right)
        return result

    def postorder_traversal(self, node):
        """
        Perform a postorder traversal of the binary tree.

        Returns:
            list: List of values in postorder traversal order.
        """

        if node is None:
            return []
        result = self.postorder_traversal(node.left)
        result += self.postorder_traversal(node.right)
        result.append(node.value)
        return result
