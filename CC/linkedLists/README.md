## Linked Lists
- Code Challenge 05

---
<br>

#### Challenge Type: Implementation
#### Challenge Instruction: 
<br>

### Features:
<br>

#### Node: 
- Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
<br>

#### Linked List: 

<ul>
<li>Create a Linked List class</li>
<li>Within your Linked List class, include a head property.</li>
<li>Upon instantiation, an empty Linked List should be created.</li>
<br>
<li>The class should contain the following methods</li>
<ul>
<li>insert</li>
<ul>
<li>Arguments: value</li>
<li>Returns: nothing</li>
<li>Adds a new node with that value to the head of the list with an O(1) Time performance.</li>
</ul>
<br>
<li>includes</li>
<ul>
<li>Arguments: value</li>
<li>Returns: Boolean</li>
<li>Indicates whether that value exists as a Node’s value somewhere within the list.</li>
</ul>
<br>
<li>to string</li>
<ul>
<li>Arguments: none</li>
<li>Returns: a string representing all the values in the Linked List, formatted as: <strong>"{ a } -> { b } -> { c } -> NULL"</strong>
</li>
</ul>
</ul>
</ul>

---
<br>

### Structure and Testing:
<br>

#### Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

#### Be sure to follow your language/frameworks standard naming conventions (e.g. C# uses PascalCasing for all method and class names).

#### Any exceptions or errors that come from your code should be contextual, descriptive, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom error that describes what went wrong in calling the methods you wrote for this lab.
<br>

#### Write tests to prove the following functionality:

<ul>
<li>Can successfully instantiate an empty linked list</li>
<li>Can properly insert into the linked list</li>
<li>The head property will properly point to the first node in the linked list</li>
<li>Can properly insert multiple nodes into the linked list</li>
<li>Will return true when finding a value within the linked list that exists</li>
<li>Will return false when searching for a value in the linked list that does not exist</li>
<li>Can properly return a collection of all the values that exist in the linked list</li>
</ul>
<br>

#### Ensure your tests are passing before you submit your solution.

---
<br>

### Stretch Goal:
<br>

#### Create a new branch called <strong>doubly-linked-list</strong>, and, using the resources available to you online, implement a doubly linked list (completely separate from your singly linked list).

---
<br>

**- Esmail Jawabreh**