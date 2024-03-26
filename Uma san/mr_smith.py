def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, round(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_factor(n):
    lst = []
    for i in range(2, round(n**0.5) + 1):
        if is_prime(i):
            while n % i == 0:
                lst.append(i)
                n //= i
    if n > 1:
        lst.append(n)
    return lst

def lst_sum(n):
    lst = prime_factor(n)
    Sum = 0
    for i in lst:
        if i < 10:
            Sum+=i
        else:
            temp = str(i)
            temp_lst = [int(x) for x in temp]
            Sum+=sum(temp_lst)
    return Sum



def Sum(n):
    str1 = str(n)
    lst = [int(x) for x in str1]
    return sum(lst)


def mr_smith():
    n = 4937776
    while True:
        if Sum(n) == lst_sum(n) and is_prime(n) == False:
            print("The number greater than 4937775 is : ",n)
            break
        else:
            n+=1

mr_smith()