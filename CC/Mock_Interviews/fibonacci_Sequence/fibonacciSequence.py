def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n+1):
            c = a + b
            a, b = b, c
        return b


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 14, 45]


for j in arr:
    if j < 15:
        print(fib_recursive(j))

for i in arr:
    print(fib_iterative(i))
