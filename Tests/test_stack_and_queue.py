import pytest
from CC.stack_and_queue.stack_and_queue import Stack, Queue
from CC.stack_and_queue.stack_queue_AnimalShelter import *
from CC.stack_and_queue.stack_queue_Pseudo import PseudoQueue
from CC.stack_and_queue.stack_queue_Brackets import validate_brackets


# Stack tests
def test_stack_push_one_value():
    stack = Stack()
    stack.push(1)
    assert stack.top.value == 1


def test_stack_push_multiple_values():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.top.value == 3


def test_stack_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    value = stack.pop()
    assert value == 2
    assert stack.top.value == 1


def test_stack_empty_after_multiple_pops():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.pop()
    stack.pop()
    assert stack.is_empty()


def test_stack_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    value = stack.peek()
    assert value == 2
    assert stack.top.value == 2


def test_stack_is_empty():
    stack = Stack()
    assert stack.is_empty()


def test_stack_pop_on_empty_stack_raises_exception():
    stack = Stack()
    with pytest.raises(Exception):
        stack.pop()


def test_stack_peek_on_empty_stack_raises_exception():
    stack = Stack()
    with pytest.raises(Exception):
        stack.peek()


# Queue tests
def test_queue_enqueue_one_value():
    queue = Queue()
    queue.enqueue(1)
    assert queue.front.value == 1
    assert queue.back.value == 1


def test_queue_enqueue_multiple_values():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.front.value == 1
    assert queue.back.value == 3


def test_queue_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    value = queue.dequeue()
    assert value == 1
    assert queue.front.value == 2


def test_queue_peek():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    value = queue.peek()
    assert value == 1
    assert queue.front.value == 1


def test_queue_empty_after_multiple_dequeues():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.dequeue()
    queue.dequeue()
    assert queue.is_empty()


def test_queue_is_empty():
    queue = Queue()
    assert queue.is_empty()


def test_queue_dequeue_on_empty_queue_raises_exception():
    queue = Queue()
    with pytest.raises(Exception):
        queue.dequeue()


def test_queue_peek_on_empty_queue_raises_exception():
    queue = Queue()
    with pytest.raises(Exception):
        queue.peek()


############################################################################################
# stack_queue_AnimalShelter


@pytest.fixture
def animal_shelter():
    return AnimalShelter()


@pytest.fixture
def dog():
    return Animal("dog", "Buddy")


@pytest.fixture
def cat():
    return Animal("cat", "Whiskers")


def test_enqueue_and_dequeue_pref(animal_shelter, dog, cat):
    animal_shelter.enqueue(dog)
    animal_shelter.enqueue(cat)

    assert animal_shelter.dequeue("dog") == dog
    assert animal_shelter.dequeue("cat") == cat


def test_dequeue_invalid_pref(animal_shelter, dog, cat):
    animal_shelter.enqueue(dog)
    animal_shelter.enqueue(cat)

    assert animal_shelter.dequeue("rabbit") is None


def test_dequeue_when_empty(animal_shelter):
    assert animal_shelter.dequeue("dog") is None
    assert animal_shelter.dequeue("cat") is None


def test_dequeue_oldest_animal(animal_shelter, dog, cat):
    animal_shelter.enqueue(dog)
    animal_shelter.enqueue(cat)

    assert animal_shelter.dequeue("dog") == dog
    assert animal_shelter.dequeue("cat") == cat


def test_enqueue_timestamp(animal_shelter, dog, cat):
    animal_shelter.enqueue(dog)
    animal_shelter.enqueue(cat)

    assert dog.timestamp == 0
    assert cat.timestamp == 1


def test_enqueue_multiple_dogs(animal_shelter, dog):
    animal_shelter.enqueue(dog)
    animal_shelter.enqueue(dog)
    animal_shelter.enqueue(dog)

    assert animal_shelter.dequeue("dog") == dog
    assert animal_shelter.dequeue("dog") == dog
    assert animal_shelter.dequeue("dog") == dog


def test_enqueue_multiple_cats(animal_shelter, cat):
    animal_shelter.enqueue(cat)
    animal_shelter.enqueue(cat)
    animal_shelter.enqueue(cat)

    assert animal_shelter.dequeue("cat") == cat
    assert animal_shelter.dequeue("cat") == cat
    assert animal_shelter.dequeue("cat") == cat


############################################################################################
# stack_queue_Pseudo


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


############################################################################################
# stack_queue_Brackets


def test_validateBrackets_one():
    actual = validate_brackets("{}")
    expected = True
    assert actual == expected


def test_validateBrackets_two():
    actual = validate_brackets("{}(){}")
    expected = True
    assert actual == expected


def test_validateBrackets_three():
    actual = validate_brackets("()[[Extra Characters]]")
    expected = True
    assert actual == expected


def test_validateBrackets_four():
    actual = validate_brackets("(){}[[]]")
    expected = True
    assert actual == expected


def test_validateBrackets_five():
    actual = validate_brackets("{}{Code}[Fellows](())")
    expected = True
    assert actual == expected


def test_validateBrackets_six():
    actual = validate_brackets("[({}]")
    expected = False
    assert actual == expected


def test_validateBrackets_seven():
    actual = validate_brackets("(](")
    expected = False
    assert actual == expected


def test_validateBrackets_eight():
    actual = validate_brackets("{(})")
    expected = False
    assert actual == expected
