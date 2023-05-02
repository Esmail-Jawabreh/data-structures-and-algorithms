import pytest
from CC.Mock_Interviews.CC09.reverse_LinkedList.reverseLinkedList import *


def test_reverse_linked_list():
    # Test case 1
    head = Node(3)
    head.next = Node(2)
    head.next.next = Node(1)
    reversed_head = reverse_list(head)
    assert reversed_head.data == 1
    assert reversed_head.next.data == 2
    assert reversed_head.next.next.data == 3

    # Test case 2
    head = Node('a')
    head.next = Node('b')
    head.next.next = Node('c')
    reversed_head = reverse_list(head)
    assert reversed_head.data == 'c'
    assert reversed_head.next.data == 'b'
    assert reversed_head.next.next.data == 'a'
