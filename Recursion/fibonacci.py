def fibonacci_series(n):
    if n <= 1:
        return n
    else:
        return fibonacci_series(n-1) + fibonacci_series(n-2)
    
print(fibonacci_series(100))

# import time
# import sys

# sys.set_int_max_str_digits(100000000)

# n = int(input("Enter the nth term : "))
# a = 0
# b = 1
# c = 0
# c_time = time.time()
# if n == 0:
#   print("0")
# else:
#   for i in range(1, n + 1):
#     c = a + b
#     print(c)
#     a, b = b, c
# n_time = time.time()

# print(n_time-c_time)