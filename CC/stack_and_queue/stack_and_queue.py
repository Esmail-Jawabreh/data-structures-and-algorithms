class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        """
        Pushes a value onto the top of the stack.

        Args:
        - value: The value to be added to the stack.
        """
        new_node = Node(value)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        """
        Removes and returns the value at the top of the stack.

        Returns:
        - The value at the top of the stack.

        Raises:
        - Exception: If the stack is empty.
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        """
        Returns the value at the top of the stack without removing it.

        Returns:
        - The value at the top of the stack.

        Raises:
        - Exception: If the stack is empty.
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.value

    def is_empty(self):
        """
        Returns True if the stack is empty, False otherwise.

        Returns:
        - True if the stack is empty, False otherwise.
        """
        return not bool(self.top)


class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, value):
        """
        Enqueues a value at the back of the queue.

        Args:
        - value: The value to be added to the queue.
        """
        new_node = Node(value)
        if not self.front:
            self.front = new_node
            self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node

    def dequeue(self):
        """
        Dequeues and returns the value at the front of the queue.

        Returns:
        - The value at the front of the queue.

        Raises:
        - Exception: If the queue is empty.
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.front.value
        self.front = self.front.next
        return value

    def peek(self):
        """
        Returns the value at the front of the queue without removing it.

        Returns:
        - The value at the front of the queue.

        Raises:
        - Exception: If the queue is empty.
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.front.value

    def is_empty(self):
        """
        Returns True if the queue is empty, False otherwise.

        Returns:
        - True if the queue is empty, False otherwise.
        """
        return not bool(self.front)
