def isPrime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,round(n**0.5)):
        if(n%i == 0):
            return False
    else:
        return True
    
def prime_generator(n):
    lst = []
    for i in range(n):
        if(isPrime(i)):
            lst.append(i)
    return lst

# lst = prime_generator(100)
# lst1 = []

# for i in lst:
#     for j in lst:
#         if i+j>13 and isPrime(i+j):
#             lst1.append([i,j,(i+j)])

# print(lst1)

print(isPrime(1234567891011121314))