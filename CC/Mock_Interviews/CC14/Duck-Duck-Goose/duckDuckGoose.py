def DuckDuckGoose(names, k):
    queue = list(names)

    while len(queue) > 1:
        for _ in range(k - 1):
            # Rotate the queue by k - 1 times
            queue.append(queue.pop(0))

        # Remove the person at position k
        queue.pop(0)

    return queue[0]


# Example
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
k = 3
last_person = DuckDuckGoose(names, k)
print("The last person remaining is:", last_person)
