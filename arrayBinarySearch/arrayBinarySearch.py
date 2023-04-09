def binary_search(arr, key):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == key:
            return mid
        
        if arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1



ex1 = binary_search([4, 8, 15, 16, 23, 42], 15)
ex2 = binary_search([-131, -82, 0, 27, 42, 68, 179], 42)   
ex3 = binary_search([11, 22, 33, 44, 55, 66, 77], 90)
ex4 = binary_search([1, 2, 3, 5, 6, 7], 4)


print(ex1)
print(ex2) 
print(ex3)
print(ex4) 