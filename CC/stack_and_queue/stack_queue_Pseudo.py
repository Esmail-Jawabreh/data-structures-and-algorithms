class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        """
        Pushes a value onto the top of the stack.

        Args:
            value: The value to be pushed onto the stack.
        """

        self.stack.append(value)

    def pop(self):
        """
        Removes and returns the value at the top of the stack.

        Returns:
            The value at the top of the stack.

        Raises:
            Exception: If the stack is empty.
        """

        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack.pop()

    def peek(self):
        """
        Returns the value at the top of the stack without removing it.

        Returns:
            The value at the top of the stack.

        Raises:
            Exception: If the stack is empty.
        """

        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[-1]

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """

        return len(self.stack) == 0


class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        """
        Adds an element to the end of the pseudo queue.

        Args:
            value: The value to be added to the pseudo queue.
        """

        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        self.stack1.push(value)
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())

    def dequeue(self):
        """
        Removes and returns the element at the front of the pseudo queue.

        Returns:
            The element at the front of the pseudo queue.

        Raises:
            Exception: If the pseudo queue is empty.
        """

        if self.stack1.is_empty():
            raise Exception("PseudoQueue is empty")
        return self.stack1.pop()


