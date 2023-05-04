class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        """
        Adds a new node with the given value to the end of the linked list.

        Parameters:
        -----------
        value: Any
        The value to be added to the linked list.

        Returns:
        --------
        None
        """

        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def insert_before(self, value, new_value):
        """
        Inserts a new node with the given value before the node with the specified value.

        Parameters:
        -----------
        value: Any
            The value of the node before which the new node should be inserted.
        new_value: Any
            The value to be added to the linked list.

        Returns:
        --------
        None
        """

        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        if self.head.value == value:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.value == value:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next

    def insert_after(self, value, new_value):
        """
        Inserts a new node with the given value after the node with the specified value.

        Parameters:
        -----------
        value: Any
            The value of the node after which the new node should be inserted.
        new_value: Any
            The value to be added to the linked list.

        Returns:
        --------
        None
        """

        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node:
            if current_node.value == value:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next

    def includes(self, value):
        """
        Searches for a node with the given value in the linked list.

        Parameters:
        -----------
        value: Any
            The value to search for in the linked list.

        Returns:
        --------
        bool
            True if a node with the given value is found, False otherwise.
        """

        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def to_string(self):
        """
        Returns a string representation of the linked list.

        Returns:
        --------
        str
            A string representation of the linked list.
        """

        current_node = self.head
        result = ""
        while current_node:
            result += "{ " + str(current_node.value) + " } -> "
            current_node = current_node.next
        result += "NULL"
        return result

    def delete(self, value):
        """
        Deletes the first occurrence of a node with the given value from the linked list.

        Parameters:
        -----------
        value: Any
            The value of the node to be deleted.

        Returns:
        --------
        None
        """

        current_node = self.head
        if current_node and current_node.value == value:
            self.head = current_node.next
            current_node = None
            return

        previous_node = None
        while current_node and current_node.value != value:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        previous_node.next = current_node.next
        current_node = None

    def kth_from_end(self, k):
        """
        Finds the kth node from the end of the linked list.

        Parameters:
        -----------
        k: int
            The position of the node to find, counting from the end of the linked list.

        Returns:
        --------
        Any
            The value of the kth node from the end, or None if k is greater than the length of the linked list or less than or equal to 0.
        """

        if k < 0:
            raise Exception("K must be Positive!")

        # Get the length of the linked list
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next

        if k > length:
            raise Exception("out of range!")

        # Calculate the position of the kth node from the beginning
        position = length - k 

        # Traverse the linked list to find the kth node from the beginning
        current = self.head
        for i in range(position):
            current = current.next

        return current.value

    def find_middle(self):
        """
        Finds the middle node of the linked list.

        Returns:
        --------
        Any
            The value of the middle node, or None if the linked list is empty.
        """

        if not self.head:
            return None

        slow = self.head
        fast = self.head

        # Traverse the linked list using two pointers,
        # one moving at half the speed of the other.
        # When the fast pointer reaches the end of the
        # list, the slow pointer will be at the middle node.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.value

    @staticmethod
    def zipLists(list1: 'LinkedList', list2: 'LinkedList'):
        """
        Zips two linked lists together into one linked list, alternating between nodes from each list.
        Parameters:
        ----------
        list1 : LinkedList
            The first linked list to zip.
        list2 : LinkedList
            The second linked list to zip.
        Returns:
        -------
        LinkedList
            A new linked list containing the zipped nodes.
        """

        if list1.head is None:
            return list2
        if list2.head is None:
            return list1
        list1_current = list1.head
        list2_current = list2.head
        while list1_current and list2_current:
            list1_next = list1_current.next
            list2_next = list2_current.next
            list1_current.next = list2_current
            if list1_next is None:
                break
            list2_current.next = list1_next
            list1_current = list1_next
            list2_current = list2_next
        return list1
