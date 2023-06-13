## Merge Sort
- Code Challenge 27

---
<br>

## Assignment
#### Review the pseudocode below, then trace the algorithm by stepping through the process with the provided sample array. Document your explanation by creating a blog article that shows the step-by-step output after each iteration through some sort of visual.

#### Once you are done with your article, code a working, tested implementation of Merge Sort based on the pseudocode provided.
<br>

## Pseudocode
```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
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

**Step-by-Step Visualization of the Merge Sort Algorithm**

<br>

#### In this blog article, we will explore the Merge Sort algorithm, a popular sorting algorithm known for its efficiency and stability. 
#### We will review the provided pseudo code, trace its execution step-by-step, and visualize the output for a sample array. 
#### Additionally, we will implement the pseudo code in a programming language and provide a set of working tests.

<br>

#### The Merge Sort algorithm follows a divide-and-conquer approach by recursively splitting the input array into smaller subarrays until they become trivially sorted. 
#### It then merges these subarrays back together in a sorted manner, resulting in a fully sorted array. 
<br>

#### Let's review the provided pseudo code:
```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
        DECLARE mid <-- n/2
        DECLARE left <-- arr[0...mid]
        DECLARE right <-- arr[mid...n]
        // sort the left side
        Mergesort(left)
        // sort the right side
        Mergesort(right)
        // merge the sorted left and right sides together
        Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

<br>

#### Now, let's step through the algorithm by visualizing the output after each iteration for the provided sample array: 
```
[8, 4, 23, 42, 16, 15].
```
<br>

- Step 1:
    - The input array is [8, 4, 23, 42, 16, 15]. 
    - The Mergesort algorithm is called initially with this array.
    - The length of the array is 6, which is greater than 1, so we proceed with the algorithm.

<br>

- Step 2:
    - Since the array has more than one element, we calculate the middle index mid = 6/2 = 3.
    - We split the array into two subarrays:
        - left = [8, 4, 23]
        - right = [42, 16, 15]

<br>

- Step 3:
    - The Mergesort algorithm is called recursively on the left and right subarrays. 

    <br>

    - Recursive Call: Mergesort([8, 4, 23])
        - The length of the subarray is greater than 1, so we split it further.
        - Calculate mid = 3/2 = 1.
        - Split the subarray into two subarrays:
            - left = [8]
            - right = [4, 23]
        - Since the left subarray has only one element, it is already sorted.

    <br>

    - Recursive Call: Mergesort([4, 23])
        - The length of the subarray is greater than 1, so we split it further.
        - Calculate mid = 2/2 = 1.
        - Split the subarray into two subarrays:
            - left = [4]
            - right = [23]
        - Both left and right subarrays have only one element, so they are already sorted.

<br>

- Step 4:
    - Merge the sorted subarrays left = [4] and right = [23] back into the original arr = [4, 23] using the Merge algorithm.

<br>

- Step 5:
    - Return to the previous recursive call, where left = [8] and right = [4, 23] were split. 
    - Merge these sorted subarrays back into the original arr = [4, 8, 23].

<br>

- Step 6:
    - Return to the initial call of the Mergesort algorithm, where left = [4, 8, 23] and right = [42, 16, 15] were split. 
    - Merge these sorted subarrays back into the original arr.
    
    <br>

    - Recursive Call: Merge([4, 8, 23], [42, 16, 15], [8, 4, 23, 42, 16, 15])
        - Initialize i = 0, j = 0, and k = 0.
        - Compare left[i] = 4 with right[j] = 42. Since 4 <= 42, we assign arr[k] = 4, increment i, and increment k.
        - Compare left[i] = 8 with right[j] = 42. Since 8 <= 42, we assign arr[k] = 8, increment i, and increment k.
        - Compare left[i] = 23 with right[j] = 42. Since 23 <= 42, we assign arr[k] = 23, increment i, and increment k.
        - Now, i = 3, which is equal to the length of left. We copy the remaining elements from right to arr.
        - The resulting arr is [4, 8, 23, 42, 16, 15].


<br>

- Step 7:
    - The final sorted array is [4, 8, 23, 42, 16, 15]. 
    - This completes the execution of the Merge Sort algorithm for the given sample array.

<br>
<br>

### you can find the code implementation [here](./merge.py)

### you can find the complete set of working tests for the implementation [here](../../../Tests/test_mergeSort.py)

<br>

<br>

### Conclusion:
#### In this blog article, we reviewed the Merge Sort algorithm and traced its execution step-by-step using the provided pseudo code. 
#### We visualized the output after each iteration for the sample array [8, 4, 23, 42, 16, 15]. 
#### The Merge Sort algorithm effectively sorted the array in ascending order. 
#### By understanding the algorithm's recursive nature and merging process, we can appreciate its efficiency and stability.
<br>


---
<br>

**- Esmail Jawabreh**