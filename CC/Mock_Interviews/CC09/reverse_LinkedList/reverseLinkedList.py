class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def reverse_list(head):
    if not head:
        return None
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
