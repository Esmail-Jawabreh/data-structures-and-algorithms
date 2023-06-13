## Insertion Sort
- Code Challenge 26

---
<br>

## Assignment
#### Review the pseudocode below, then trace the algorithm by stepping through the process with the provided sample array. Document your explanation by creating a blog article that shows the step-by-step output after each iteration through some sort of visual.

#### Once you are done with your article, code a working, tested implementation of Insertion Sort based on the pseudocode provided.
<br>

## Pseudocode
```
Insert(int[] sorted, int value)
  initialize i to 0
  WHILE value > sorted[i]
    set i to i + 1
  WHILE i < sorted.length
    set temp to sorted[i]
    set sorted[i] to value
    set value to temp
    set i to i + 1
  append value to sorted

InsertionSort(int[] input)
  LET sorted = New Empty Array
  sorted[0] = input[0]
  FOR i from 1 up to input.length
    Insert(sorted, input[i])
  return sorted
```

<br>

## Sample Arrays

#### In your blog article, visually show the output of processing this input array:
```
[8,4,23,42,16,15]
```
<br>

#### For your own understanding, consider also stepping through these inputs:

- Reverse-sorted: 
    ```
    [20,18,12,8,5,-2]
    ```
- Few uniques: 
    ```
    [5,12,7,5,5,7]
    ```
- Nearly-sorted: 
    ```
    [2,3,5,7,13,11]
    ```

<br>


### Implementation
- Provide a visual step through for each of the sample arrays based on the provided pseudo code
- Convert the pseudo-code into working code in your language
- Present a complete set of working tests

<br>

---
---
<br>

## Blog Article:

**Exploring Insertion Sort: A Step-by-Step Guide**

<br>

#### Insertion Sort is a simple sorting algorithm that works by repeatedly building a sorted portion of the array and inserting each unsorted element into its correct position within the sorted portion. 

#### In this article, we will review the provided pseudocode for Insertion Sort, trace the algorithm step-by-step using visual representations, and then implement the algorithm in code. 

#### We will also examine the algorithm's behavior with various sample arrays.

<br>

### Pseudocode Review
```
Insert(int[] sorted, int value)
  initialize i to 0
  WHILE value > sorted[i]
    set i to i + 1
  WHILE i < sorted.length
    set temp to sorted[i]
    set sorted[i] to value
    set value to temp
    set i to i + 1
  append value to sorted

InsertionSort(int[] input)
  LET sorted = New Empty Array
  sorted[0] = input[0]
  FOR i from 1 up to input.length
    Insert(sorted, input[i])
  return sorted
```
<br>

### Step-by-Step Visualization

- sample array: 
    ```
    [8, 4, 23, 42, 16, 15]
    ```
<br>

- Step 1:
    - Initial state: [8]
    - Start with the first element in the sorted array.

<br>

- Step 2:
    - [4, 8]
    - Compare the second element (4) with the sorted array (8) and insert it at the correct position.

<br>

- Step 3:
    - [4, 8, 23]
    - Compare the third element (23) with the sorted array (4, 8) and insert it at the correct position.

<br>

- Step 4:
    - [4, 8, 23, 42]
    - Compare the fourth element (42) with the sorted array (4, 8, 23) and insert it at the correct position.

<br>

- Step 5:
    - [4, 8, 16, 23, 42]
    - Compare the fifth element (16) with the sorted array (4, 8, 23, 42) and insert it at the correct position.

<br>

- Step 6:
    - [4, 8, 15, 16, 23, 42]
    - Compare the sixth element (15) with the sorted array (4, 8, 16, 23, 42) and insert it at the correct position.

<br>

### The final sorted array is [4, 8, 15, 16, 23, 42].
<br>

### you can find the code implementation [here](./insertion.py)

### you can find the complete set of working tests for the implementation [here](../../../Tests/test_insertionSort.py)

<br>

<br>

### Conclusion:
#### In this article, we explored the Insertion Sort algorithm, reviewed its pseudocode, and traced its execution step-by-step using visual representations. 
#### We also implemented the algorithm in code and verified its correctness through a set of tests. 
<br>

#### Insertion Sort is an efficient algorithm for small input sizes or partially sorted arrays. 
<br>

---
<br>

**- Esmail Jawabreh**