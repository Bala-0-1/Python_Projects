# Take any 2-digit number and multiply the digits together. If this process is continued, all 2-digit numbers will become single-digit numbers.

# For example,
# Consider 76 : 7x6 = 42 : 4x2 = 8. We started with 76 and it ended in an 8.
# Consider 43 : 4x3 = 12 : 1x2 = 2. Started with 43 and it ended in a two.

# My question is, how many 2-digit numbers will finish on zero? like 10, 20, ...

# You might be wondering that a two-digit number like 55 also ends in zero. For your reference, 55: 5x5 = 25: 2x5 = 10: 1x0 = 0.

# So, find how many 2-digit numbers will finish on zero?

def digits_splitter(num):
    lst = []
    while(num>=1):
        temp = num%10
        num = num//10
        lst.append(temp)
    return lst

def multiply(lst):
    num = 1
    for i in lst:
        num*=i
    return num

def ends_with_zero():
    lst = []
    for i in range(10,100):
        num = i
        while(num>9):
            num = multiply(digits_splitter(num))
            if(num==0):
                lst.append(i)
                break
            num = multiply(digits_splitter(num))
    return lst

print(ends_with_zero())