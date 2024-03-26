# LOOPS

# 1. Print a list in reverse order.

def reverse(num):
    reversed_list = num[::-1]
    return reversed_list

# 2. Write a program to find the GCD of a number

def GCD(x, y):
 
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
             
    return gcd


# 3. Write a program to convert Decimal to binary, Octal and Hexadecimal

# Function to convert decimal to binary
def decimal_to_binary(n):
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary

# Function to convert decimal to octal
def decimal_to_octal(n):
    octal = ""
    while n > 0:
        remainder = n % 8
        octal = str(remainder) + octal
        n = n // 8
    return octal

# Function to convert decimal to hexadecimal
def decimal_to_hexadecimal(n):
    hexadecimal = ""
    while n > 0:
        remainder = n % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal
        n = n // 16
    return hexadecimal


# 4. Write a program to search an element in a ascending ordered array using binary search.

def binary_search(lst,target):
    sum_value = 0
    sorted(lst)
    while len(lst) >= 1:
        mid = len(lst)//2
        if lst[mid] == target:
            return len(lst)//2+sum_value
        elif lst[mid] < target:
            sum_value = len(lst[0:mid])
            lst = lst[mid:len(lst)]
        elif lst[mid] > target:
            lst = lst[0:mid]
    else:
        return "Element not in list."
    

# 5. Write a program to find the sum of digits of a number.

def sum_of_digits(num):
    Sum = 0
    while num>=1:
        temp = num%10
        num = num//10
        Sum+=temp
    return Sum



# RECURSION 

# 1. Print a list in reverse order.

def recursion_reverse(lst,f,l):
    if f>l:
        return lst
    tem = lst[f]
    lst[f] = lst[l]
    lst[l] = tem

    return recursion_reverse(lst,f+1,l-1)

# 2. Write a program to find the GCD of a number


def recursion_GCD(x,y,count,gcd):
    if x < count:
        return gcd
    elif (x%count == 0) and (y%count == 0):
        gcd = count
        return recursion_GCD(x,y,count+1,gcd)
    else:
        return recursion_GCD(x,y,count+1,gcd)
    

# 3. Write a program to convert Decimal to binary, Octal and Hexadecimal

def recursion_binary(num,binary):
    if num<=0:
        return binary[::-1]
    else:
        binary+=str(num%2)
        num = num//2
        return recursion_binary(num,binary)

def recursion_octal(num,octal):
    if num<=0:
        return octal[::-1]
    else:
        octal+=str(num%8)
        num = num//8
        return recursion_octal(num,octal)

def recursion_hexadecimal(num, hexa):
    if num == 0:
        return hexa[::-1]
    else:
        remainder = num % 16
        if remainder < 10:
            hexa += str(remainder)
        else:
            hexa += chr(ord('A') + remainder - 10)
        num = num // 16
        return recursion_hexadecimal(num, hexa)



# 4. Write a program to search an element in a ascending ordered array using binary search.

def recursion_binary_search(lst,target,sum_value):
    mid = lst[len(lst)//2]
    if lst[mid] == target:
        return mid+sum_value
    if len(lst)<1:
        if lst[0] != target:
            return "Element not found!!"
        else:
            return lst[0]
        
    elif lst[mid] < target:
        sum_value = len(lst[0:mid])
        lst = lst[mid:len(lst)]
        return recursion_binary_search(lst,target,sum_value)

    elif lst[mid] > target:
        lst = lst[0:mid]
        return recursion_binary_search(lst,target,sum_value)

    else:
        return recursion_binary_search(lst,target,sum_value)

# 5. Write a program to find the sum of digits of a number.

def recursion_sum(num,sum_value):
    if num<1:
        return sum_value
    else:
        return recursion_sum(num//10,sum_value+num%10)
