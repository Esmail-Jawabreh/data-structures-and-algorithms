## stack-and-queue
* Code Challenge 10 & 11
---
<br>

## Code Challenge 10
### Features
#### Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue (Python)
<br>

### Node:
#### Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
<br>

### Stack:
#### Create a Stack class that has a top property. It creates an empty Stack when instantiated.
#### This object should be aware of a default empty value assigned to top when the stack is created.
<br>

#### The class should contain the following methods:
- push
#### Arguments: value
#### adds a new node with that value to the top of the stack with an O(1) Time performance.

- pop
#### Arguments: none
#### Returns: the value from node from the top of the stack
#### Removes the node from the top of the stack
#### Should raise exception when called on empty stack

- peek
#### Arguments: none
#### Returns: Value of the node located at the top of the stack
#### Should raise exception when called on empty stack

- is empty
#### Arguments: none
#### Returns: Boolean indicating whether or not the stack is empty.
<br>

### Queue:
#### Create a Queue class that has a front property. It creates an empty Queue when instantiated.
#### This object should be aware of a default empty value assigned to front when the queue is created.
<br>

#### The class should contain the following methods:
- enqueue
#### Arguments: value
#### adds a new node with that value to the back of the queue with an O(1) Time performance.

- dequeue
#### Arguments: none
#### Returns: the value from node from the front of the queue
#### Removes the node from the front of the queue
#### Should raise exception when called on empty queue

- peek
#### Arguments: none
#### Returns: Value of the node located at the front of the queue
#### Should raise exception when called on empty stack

- is empty
#### Arguments: none
#### Returns: Boolean indicating whether or not the queue is empty
---
<br>

### Structure and Testing

#### Write tests to prove the following functionality:

- Can successfully push onto a stack
- Can successfully push multiple values onto a stack
- Can successfully pop off the stack
- Can successfully empty a stack after multiple pops
- Can successfully peek the next item on the stack
- Can successfully instantiate an empty stack
- Calling pop or peek on empty stack raises exception
- Can successfully enqueue into a queue
- Can successfully enqueue multiple values into a queue
- Can successfully dequeue out of a queue the expected value
- Can successfully peek into a queue, seeing the expected value
- Can successfully empty a queue after multiple dequeues
- Can successfully instantiate an empty queue
- Calling dequeue or peek on empty queue raises exception

---
<br>

## Code Challenge 11
### Feature 
#### Create a new class called pseudo queue.
#### Do not use an existing Queue.
#### Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below),
#### Internally, utilize 2 Stack instances to create and manage the queue
#### Methods:
- enqueue
##### Arguments: value
##### Inserts a value into the PseudoQueue, using a first-in, first-out approach.
- dequeue
##### Arguments: none
##### Extracts a value from the PseudoQueue, using a first-in, first-out approach.
<br>

#### NOTE: The Stack instances have only push, pop, and peek methods. You should use your own Stack implementation. Instantiate these Stack objects in your PseudoQueue constructor.
<br>

### WhiteBoard
![WhiteBoard](./stack_and_queue_Pseudo_WhiteBoard.png)
<br>

---
<br>

**- Esmail Jawabreh**