#Strings 

#Create a string with the first, middle and last character of a given string

def f_m_l(str1):
    if len(str1)%2 != 0:
        temp = str1[0]+str1[len(str1)/2]+str1[len(str1)]
    else:
        temp = str[0]+str1[len(str1)//2]+str1[len(str1)//2+1]+str1[len(str1)]
    return temp

#Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.

def s1_s2():
  try:
    s1=input('enter first string: ')
    s2=input('enter second string: ')
    s3=''
    s2=s2[::-1]
    index=0
    if len(s1)==0 or len(s2) == 0:
        print("The length is zero, cant proceed")
    elif s1.strip()=='' or s2.strip() == '':
        print("Error: The input string consists of only spaces")
    else:
        while index < max(len(s1),len(s2)):
            if index < len(s1):
                s3+=s1[index]
            if index < len(s2):
                s3+=s2[index]
            index+=1
    print(s3)
  except ValueError:
    print('Error: The input is not a valid string.') 
  except NameError:
    print('Error: A variable used in the code is not defined.')
  except TypeError:
    print('Error: Check the types used in the code.')


#Calculate the sum and average of the digits present in a string eg: ghfh6.5hk7mbm8

def str_sum(str1):
    Sum = 0
    for i in str1:
        if(ord(i) in range(48,58)):
            Sum += int(i)
    return Sum

#Write a program to find all occurrences of a substring in a given string ignoring the case.

def all_substring_occurence(str1,str2):
    count = 0
    l1 = len(str1)
    l2 = len(str2)
    k = l2
    for i in range(l1-l2):
      if str1[i:k] == str2:
          count+=1
      k+=1
    return count  
#Consider you have a string. Fetch those substrings/words that have a number attached to them at the end
def strip(str1,str2):
    str3 = ""
    for i in str1:
        if i == str2:
            continue
        str3 += i
    return str3

def spilt_string_by_integers(str1):
    str1 = strip(str1,".")
    lst = []
    start = 0
    for i in range(len(str1)):
        if ord(str1[i]) in range(48,58):
            if i != len(str1)-1 and ord(str1[i+1]) not in range(48,58):
                lst.append(str1[start:i+1])
                start = i+1
    return lst

# print(spilt_string_by_integers())

'''Triangular numbers are so called because of the equilateral triangular shape that they occupy when laid out as dots.

1st (1)   2nd (3)    3rd (6)
*              **             ***
                *              **
                                *

For negative numbers, let the stars be 0

Sample Input and Output: 
0 --> 0
2 --> 3
3 --> 6
-10 --> 0'''

def triangular_number_printer(n):
    num = n*(n+1)/2
    k = n
    print("The trianglular number is : ",num)
    for i in range(n):
        print("*"*k,sep=" ")
        k-=1




#Loops

#Count the number of digits in a number

def digit_counter(num):
    count = 0
    if num>=0:
        for i in range(len(str(num))):
            count+=1
        return count
    else:
        return "Number cannot be negative."
    

#Print all prime numbers within a given range.

def primes(num):
    lst = []
    for i in range(2,num+1):
        flag = True
        for j in range(2,round(i**0.5)+1):
            if i%j == 0:
                flag = False
                break
        if flag == True:
            lst.append(i)
    return lst

#Consider you have a list of numbers. Iterate the list and print all the numbers which are multiples of 5 and less than 150

def multiple_of_5_and_less_than_150(lst):
    lst1 = []
    if len(lst) != 0:
        for i in lst:
            if i%5 == 0 and i < 150:
                lst1.append(i)
        return lst1 if (len(lst1)!=0) else "No numbers that satisfy the above condition."
    else:
        return "List length is zero."
    

#Consider you have a num like, 1234. Look at this number and say, in each digit, how many such digits occur together. 
# Eg: for the num 1234, the output should be 11121314 and for a num like, 11314, the output should be 21131114.

def count_of_repetition(num):
    dict = {x:y for x,y in zip(str(num),range(len(str(num))))}
    for i in str(num):
        count = 0
        for j in str(num):
            if i == j:
                count+=1
        dict[i] = count
    for x in dict:
        print(f'{x}{dict[x]}',end="")



#Lists


#Consider 2 lists. Iterate the first list from 0 to end and the second list from end to 0. Add each element from them into a third list

def l1_l2():
    num1=int(input("how many numbers in lst1: "))
    num2=int(input("how many numbers in lst2: "))
    lst1,lst2,lst3=[],[],[]
    for i in range(num1):
        lst1.append(int(input("enter the numbers in 1st list: ")))
    for i in range(num2):
        lst2.append(int(input("enter the numbers in 2nd list: ")))
    if len(lst1) and len(lst2) > 0:
        maxlength=max(len(lst1),len(lst2))
        lst1.extend([0]*(maxlength-len(lst1)))
        lst2.extend([0]*(maxlength-len(lst2)))
        for i in range(maxlength):
            lst3.append(lst1[i]+lst2[-(i+1)])
        print(lst3)
    else:
        print("Error: At least one of the lists is empty.")


#Consider you have a list with many sublists inside. Include a given sublist into the innermost sublist.

def innermost_sublist(lst1,num):
    def inner_list(lst):
        for i in range(len(lst)):
            if isinstance(lst[i], list):
                return inner_list(lst[i])
        else:
            return lst 
    def foist(lst1,lst2):
        inner_list(lst1).append(lst2)
        return lst1
    lst1=[1,2,3,[2,3,[3,4,[5,6,[7,8,[2]]]]]]
    lst2=5
    print(foist(lst1,lst2))

#Consider you have two lists. Concatenate them deeply as first element of first list with all elements of the second list and so on. 

def con():
    num1=int(input("how many numbers in lst1: "))
    num2=int(input("how many numbers in lst2: "))
    lst1,lst2,lst3=[],[],[]
    for i in range(num1):
        lst1.append(int(input("enter the numbers in 1st list: ")))
    for i in range(num2):
        lst2.append(int(input("enter the numbers in 2nd list: ")))
    if len(lst1) and len(lst2) > 0:
        for i in lst1:
            for j in lst2:
                lst3.append(i+j)
        print(lst3)