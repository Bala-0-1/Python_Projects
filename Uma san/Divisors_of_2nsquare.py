def factors(n,n1):
    lst = []
    for i in range(1,n1+1):
        if(n%i == 0):
            lst.append(i)
    return lst

def two_n_squared(n):
    return 2*(n*n)

def F_N(n):
    Sum = 0
    for i in range(1,n+1):
        Sum += len(factors(two_n_squared(i),i))
    return Sum

print(F_N(1000000000000))

# def count_factors(num):
#     count = 1
#     i = 2
#     while i * i <= num:
#         exponent = 0
#         while num % i == 0:
#             num //= i
#             exponent += 1
#         count *= (exponent + 1)
#         i += 1
#     if num > 1:
#         count *= 2
#     return count

# def F_N(n):
#     total_factors = 0
#     for i in range(1, n + 1):
#         total_factors += count_factors(i * i)
#     return total_factors

# print(F_N(100000))
