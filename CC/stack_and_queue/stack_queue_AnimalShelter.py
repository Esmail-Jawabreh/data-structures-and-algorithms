class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name


class AnimalShelter:
    def __init__(self):
        """
        Initializes an AnimalShelter object.

        The AnimalShelter class holds dogs and cats in separate queues.
        It also keeps track of a timestamp to determine the arrival order of animals.
        """
        self.dog_queue = []
        self.cat_queue = []
        self.timestamp = 0

    def enqueue(self, animal):
        """
        Adds an animal to the shelter.

        Args:
            animal (Animal): The animal object to be added to the shelter.
                             It must have a 'species' property that is either 'cat' or 'dog',
                             and a 'name' property that is a string.

        Returns:
            None
        """
        animal.timestamp = self.timestamp
        self.timestamp += 1

        if animal.species == "dog":
            self.dog_queue.append(animal)
        elif animal.species == "cat":
            self.cat_queue.append(animal)

    def dequeue(self, pref):
        """
        Removes and returns an animal from the shelter based on preference.

        Args:
            pref (str): The preference for the type of animal to dequeue.
                        It can be either 'dog' or 'cat'.

        Returns:
            Animal or None: The dequeued animal object if a matching animal is found,
                            or None if no matching animal is available.
                            If the preference is neither 'dog' nor 'cat',
                            the function returns None.
        """
        if pref == "dog":
            return self._dequeue_dog()
        elif pref == "cat":
            return self._dequeue_cat()
        else:
            return None

    def _dequeue_dog(self):
        """
        Removes and returns a dog from the shelter.

        Returns:
            Animal or None: The dequeued dog object if available,
                            or None if no dog is currently in the shelter.
                            If there are no dogs but cats are present,
                            the function returns the oldest cat.
                            If there are no animals in the shelter, it returns None.
        """
        if self.dog_queue:
            return self.dog_queue.pop(0)
        elif self.cat_queue:
            return self.cat_queue.pop(0)
        else:
            return None

    def _dequeue_cat(self):
        """
        Removes and returns a cat from the shelter.

        Returns:
            Animal or None: The dequeued cat object if available,
                            or None if no cat is currently in the shelter.
                            If there are no cats but dogs are present,
                            the function returns the oldest dog.
                            If there are no animals in the shelter, it returns None.
        """
        if self.cat_queue:
            return self.cat_queue.pop(0)
        elif self.dog_queue:
            return self.dog_queue.pop(0)
        else:
            return None


# Example usage:
shelter = AnimalShelter()

# Enqueue
shelter.enqueue(Animal("dog", "Max"))
shelter.enqueue(Animal("cat", "Whiskers"))
shelter.enqueue(Animal("dog", "Buddy"))
shelter.enqueue(Animal("cat", "Mittens"))

# Dequeue
dog = shelter.dequeue("dog")
if dog:
    print(f"Adopted dog: {dog.name}")

cat = shelter.dequeue("cat")
if cat:
    print(f"Adopted cat: {cat.name}")

# Dequeue an animal without specifying preference
animal = shelter.dequeue("unknown")
if animal:
    print(f"Adopted animal: {animal.species} - {animal.name}")
else:
    print("No preference specified. Adopted oldest animal in the shelter.")
