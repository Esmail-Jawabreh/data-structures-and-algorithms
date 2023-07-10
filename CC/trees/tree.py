from CC.trees.theNode import Node


class Tree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        return self._pre_order(self.root)

    def _pre_order(self, root: Node):
        """function that takes a root node as a starting point and returns a list of the values in the tree in the order they were encountered."""
        arr = []
        if root is None:
            return arr

        if root is not None:
            arr.append(root.value)

        if root.left is not None:
            left = self._pre_order(root.left)
            arr.extend(left)

        if root.right is not None:
            right = self._pre_order(root.right)
            arr.extend(right)

        return arr

    def in_order(self):
        return self._in_order(self.root)

    def _in_order(self, root: Node):
        """
        function that takes a root node as a starting point and returns a list of the values in the tree in the order they were encountered.
        """
        arr2 = []

        if root.left is not None:
            left = self._pre_order(root.left)
            arr2.extend(left)

        if root is not None:
            arr2.append(root.value)

        if root.right is not None:
            right = self._in_order(root.right)
            arr2.extend(right)
        return arr2

    def post_order(self):
        return self._post_order(self.root)

    def _post_order(self, root: Node):
        """
        function that takes a root node as a starting point and returns a list of the values in the tree in the order they were encountered.
        """
        arr3 = []

        if root.left is not None:
            left = self._in_order(root.left)
            arr3.extend(left)

        if root.right is not None:
            right = self._in_order(root.right)
            arr3.extend(right)

        if root is not None:
            arr3.append(root.value)

        return arr3

    def maximum(self):
        """
        function that takes a root node as a starting point and returns a list of the values in the tree in the order they were encountered.
        """
        if self.root is None:
            return None
        else:
            return self._maximum(self.root, maximum=self.root.value)

    def _maximum(self, root, maximum):
        """
        function that takes a root node as a starting point and returns a list of the values in the tree in the order they were encountered.
        """

        if root is not None:
            if root.value > maximum:
                maximum = root.value

        if root.left is not None:
            maximum = self._maximum(root.left, maximum)

        if root.right is not None:
            maximum = self._maximum(root.right, maximum)

        return maximum

    def breadth_first(self):
        """
        function that takes a root node as a starting point and returns a list of the values in the tree in the order they were encountered.
        """
        if self.root is None:
            return None
        else:
            return self._breadth_first(self.root)

    def _breadth_first(self, root):
        """
        function that takes a root node as a starting point and returns a list of the values in the tree in the order they were encountered.
        """
        arr = []
        queue = []
        queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            arr.append(node.value)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return arr
