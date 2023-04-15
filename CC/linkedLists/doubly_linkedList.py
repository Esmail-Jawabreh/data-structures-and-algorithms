class DoublyLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        new_node = DoublyLinkedListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def includes(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def to_string(self):
        current_node = self.head
        result = ""
        while current_node:
            result += "{ " + str(current_node.value) + " } <-> "
            current_node = current_node.next
        result += "NULL"
        return result
