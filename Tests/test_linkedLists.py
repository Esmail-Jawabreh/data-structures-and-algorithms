import pytest
from CC.linkedLists.linkedLists import LinkedList, Node
from CC.linkedLists.doubly_linkedList import DoublyLinkedList


def test_empty_linked_list():
    linked_list = LinkedList()
    assert linked_list.head == None


def test_insert_linked_list():
    linked_list = LinkedList()
    linked_list.insert(5)
    assert linked_list.head.value == 5


def test_insert_multiple_linked_list():
    linked_list = LinkedList()
    linked_list.insert(5)
    linked_list.insert(10)
    linked_list.insert(15)
    assert linked_list.head.value == 15
    assert linked_list.head.next.value == 10
    assert linked_list.head.next.next.value == 5


def test_find_existing_value():
    linked_list = LinkedList()
    linked_list.insert(5)
    linked_list.insert(10)
    linked_list.insert(15)
    assert linked_list.includes(10) == True


def test_find_non_existing_value():
    linked_list = LinkedList()
    linked_list.insert(5)
    linked_list.insert(10)
    linked_list.insert(15)
    assert linked_list.includes(20) == False


def test_to_string():
    linked_list = LinkedList()
    linked_list.insert(5)
    linked_list.insert(10)
    linked_list.insert(15)
    assert linked_list.to_string() == "{ 15 } -> { 10 } -> { 5 } -> NULL"



# DoublyLinkedList tests

def test_empty_doubly_linked_list():
    doubly_linked_list = DoublyLinkedList()
    assert doubly_linked_list.head is None
    assert doubly_linked_list.tail is None


def test_insert_into_doubly_linked_list():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert(1)
    assert doubly_linked_list.head.value == 1
    assert doubly_linked_list.tail.value == 1


def test_insert_multiple_nodes_into_doubly_linked_list():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert(1)
    doubly_linked_list.insert(2)
    doubly_linked_list.insert(3)
    assert doubly_linked_list.head.value == 1
    assert doubly_linked_list.tail.value == 3


def test_includes_value_in_doubly_linked_list():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert(1)
    doubly_linked_list.insert(2)
    doubly_linked_list.insert(3)
    assert doubly_linked_list.includes(2) is True


def test_does_not_include_value_in_doubly_linked_list():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert(1)
    doubly_linked_list.insert(2)
    doubly_linked_list.insert(3)
    assert doubly_linked_list.includes(4) is False


def test_doubly_linked_list_to_string():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert(1)
    doubly_linked_list.insert(2)
    doubly_linked_list.insert(3)
    assert doubly_linked_list.to_string(
    ) == "{ 1 } <-> { 2 } <-> { 3 } <-> NULL"
