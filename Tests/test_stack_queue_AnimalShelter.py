import pytest
from CC.stack_and_queue.stack_queue_AnimalShelter import *


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


# def test_dequeue_without_pref(animal_shelter, dog, cat):
#     animal_shelter.enqueue(dog)
#     animal_shelter.enqueue(cat)

#     dequeued_animal = animal_shelter.dequeue("")
#     assert dequeued_animal is not None, "No animal dequeued"
#     assert dequeued_animal.species in ["dog", "cat"], "Dequeued animal is not a dog or cat"



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
