#In a two digit number, the unit's digit exceeds the ten's digit by 2. Also, the product of the number and its sum of the digits is 144. Find the number.

def math_func():
    lst=[str(x) for x in range(10,100)]
    for i in lst:
        if int(i[0])+2 == int(i[1]):
            if (int(i[0])+int(i[1]))*int(i) == 144:
                return i
        

#I am a 2-digit prime number. The total of my digits is a prime number greater than 13. Who am I?

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


def digit_sum(n):
    lst = [int(x) for x in str(n)]
    return sum(lst)

def math_func_two():
    lst = prime_generator(100)
    for i in lst:
        if(isPrime(digit_sum(i))):
            if(digit_sum(i)>13):
                return i
            
print(math_func_two())