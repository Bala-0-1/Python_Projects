#  1). Create a list of 3 numbers. Say, [3,4,5]. Now, create a new list of all combination of numbers possible between these two numbers. Eg: for [3,4,5], it can be [345, 354, 435, 453, 534, 543].

def generate_combinations(numbers, current_combination, result):
    if len(current_combination) == len(numbers):
        result.append(int("".join(map(str, current_combination))))
        return
    
    for i in range(len(numbers)):
        if numbers[i] not in current_combination:
            generate_combinations(numbers, current_combination + [numbers[i]], result)


def generate_all_combinations(numbers):
    result = []  
    generate_combinations(numbers, [], result)
    return result




#2). Create a number list in python and multiply all numbers in the list and print the output.

def list_multiplier(lst,val,count):
    if count == len(lst):
        return val
    else:
        return list_multiplier(lst,val*lst[count],count+1)

#3). Consider you have coins in the denomination of [1,5,7,9,11]. With these coins with you, I could ask for any amount of money from 1 to 250. Provide me with minimum number of coins for any amount of money from 1 to 250 from the above denominations given to you.

def min_coins_recursive(amount, coins):
    if amount == 0:
        return 0
    
    max_coins_needed = amount + 1
    for coin in coins:
        if coin <= amount:
            num_coins = 1 + min_coins_recursive(amount - coin, coins)
            max_coins_needed = min(max_coins_needed, num_coins)
    
    return max_coins_needed

def find_min_coins():
    coins = [1, 5, 7, 9, 11]
    min_coins_list = []
    for amount in range(1, 251):
        min_coins_count = min_coins_recursive(amount, coins)
        min_coins_list.append(min_coins_count)
    return min_coins_list



#4). Can you reverse a number as it is, without converting it to a string.
def lengthRecursion(num,count):
    if(num<=0):
        return count
    else:
        count+=1
        num = num//10
        return lengthRecursion(num,count)
    
def rev(num,str):
    if(lengthRecursion(num,0) == 0):
        return str
    else:
        temp = num%10
        num = num//10
        str+="{}".format(temp)
        return rev(num,str)

#7). Write a program to find the factors of a given input number.

def factors(num,lst1=[],count=1):
    if count>round(num**0.5)+1:
        return lst1
    else:
        if num%count == 0:
            lst1.append(count)
        count+=1
        return factors(num,lst1,count)

#5). Write a program to find out whether a given number is a perfect number or not (Perfect number is one, which is equal to the sum of its divisors. Example: 6 is a perfect number. Because, 1, 2 and 3 are divisors of 6 and adding 1+2+3 = 6. )


def perfect_number(num):
    if(sum(factors(num,[],1)) == num):
        return True
    else:
        return False


#6). Given an input n, find out how many prime numbers are there between 1 and n. Print all of them.

import math

def prime_check(num,flag=False,count=2):
    if num == 0:
        return False
    if num == 1:
        return False
    if(num == 2):
        return True
    if num == 3:
        return True
    if(count == math.floor(num**0.5)+1):
        return flag
    if(num%count!=0):
        flag = True
        count+=1
        return prime_check(num,flag,count)
    elif num%count==0:
        return False

def primes(n,lst=[],count=0):
    if(count == n):
        return lst
    elif(prime_check(count)):
        lst.append(count)
        count+=1
        return primes(n,lst,count)
    else:
        count+=1
        return primes(n,lst,count)

print(primes(100))

# 8). Write a program to print the sum of powers of 2 upto 10.
# 1+2+4+8+16........+1024 = ?

def powers(num,n):
    if num == 2048:
        return n
    else:
        return powers(num*2,n+num)
    
