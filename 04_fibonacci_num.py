# using for loop
def fib(j):
    a, b = 0, 1
    for i in range(j):
        a, b = b, a + b
    return a


for j in range(1, 11):
    print j, ":", fib(j)


# Example 2: Using recursion
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


for n in range(1, 30):
    print n, ":", fib(n)


# # Recursion using cache. It's much faster.
# fib_cache = {}
#
# def fibonacci(n):
#     if n in fib_cache:
#         return fib_cache[n]
#
#     if n == 1 or n == 2:
#         return 1
#     else:
#         val = fibonacci(n - 1) + fibonacci(n - 2)
#
#     fib_cache[n] = val
#     return val
#
#
# for n in range(1, 111):
#     print n, ":", fibonacci(n)

