import pytest
from CC.stack_and_queue.stack_queue_Pseudo import PseudoQueue


def test_pseudo_queue_happy_path():
    queue = PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    assert queue.dequeue() == 3
    assert queue.dequeue() == 4
    assert queue.dequeue() == 5
    assert queue.dequeue() == 6


def test_pseudo_queue_empty():
    queue = PseudoQueue()
    with pytest.raises(Exception):
        queue.dequeue()
