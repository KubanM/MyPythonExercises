import math
import time


num = 6

for i in range(2, num):
    if num % i == 0:
        print num, "is NOT a Prime number"
        break
else:
    print num, "is a Prime number"

# def is_prime_v1(n):
#     """ Return 'True' if the 'n' is a Prime number. False otherwise."""
#
#     if n == 1:
#         return False
#
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


# t0 = time.time()
# for n in range(1, 21):
#     print n, is_prime_v1(n)

# t1 = time.time()
# print "Time is required: ", t1 - t0
#
# print "In range from 1 to 15 000:"
# t0 = time.time()
# for n in range(1, 15000):
#     is_prime_v1(n)
# t1 = time.time()
# print "v1 time is required: ", t1 - t0
#
# '''To improve our code we need to reduce number of divisors up to suqare root of n. v2: Test all divisors from 2
#     throuth sqrt(n)'''


# def is_prime_v2(n):
#     '''Return True if number is prime number. False otherwise.'''
#     if n == 1:
#         return False
#
#     max_divisor = math.floor(math.sqrt(n))
#     for i in range(2, 1 + int(max_divisor)):
#         if n % i == 0:
#             return False
#     return True
#
#
# print "In range from 1 to 150 000:"
# t0 = time.time()
# for n in range(1, 150000):
#     is_prime_v2(n)
# t1 = time.time()
# print "v2 time is required: ", t1 - t0


# # v3. In v2 we go over all even integers up to the loop, we don't need to.
# #  Step 1: Test if n is even, Step 2: Test only odd divisors
#
# def is_prime_v3(n):
#     if n == 1: return False
#
#     # Check if n is even and not 2, then it's not prime
#     if n == 2: return True
#     if n > 2 and n % 2 == 0: return False
#
#     max_divisor = math.floor(math.sqrt(n))
#     for i in range(3, 1 + int(max_divisor), 2):
#         if n % i == 0:
#             return False
#     return True
#
#
# print "In range from 1 to 150 000:"
# t0 = time.time()
# for n in range(1, 150000):
#     is_prime_v3(n)
# t1 = time.time()
# print "v3 time is required: ", t1 - t0

