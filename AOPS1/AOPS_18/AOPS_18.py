#  1). Consider you have a list of items. Write a program for removing all the occurrences of a given item present in the list.

def remove_all(lst,num):
    for i in lst:
        if i == num:
            lst.remove(i)
    return lst

#2). Consider you have a list of items. Write a program to extract all elements whose frequency is greater than K. Eg: if list=[1,2,1,3,1,4,2,3,4,3,4]. Extract all elements whose frequency is greater than 2.

def count_checker(lst,num):
    count = 0
    for i in lst:
        if i == num:
            count+=1
    return count

def frequency(lst):
    lst1 = []
    for i in set(lst):
        if count_checker(lst,i) > 2:
            lst1.append(i)
    return lst1

#3). Consider you have a list of items. Check whether the items present in the list are within a range, say, eg: if the items in the list are between 8 to 15 in a list like lst = [8,10,12,11,9,15]

def within_range(lst,start,end):
    for i in lst:
        if (i < start) or (i>end):
            return False
    else:
        return True
    
#4). Consider you have a list of items. Check whether three elements appear consecutively in the list. 
# Eg: [1,2,3,3,3,4,5] -> Returns True since, the element 3 comes three times consecutively in the list. 

def frequency_three(lst):
    for i in set(lst):
        if count_checker(lst,i) == 3:
            return True
    else:
        return False
    
#5. Your task in this kata is to implement a function that calculates the sum of the integers inside a string. For example, in the string "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", the sum of the integers is 3635.

def sum_of_integers_in_string(s):
    lst1 = []
    temp = ""
    s = s+"d"
    for i in range(len(s)-1):
        if s[i].isnumeric() and s[i+1].isnumeric() == False and s[i-1].isnumeric() == False:
            lst1.append(int(s[i]))
        elif (s[i].isnumeric() and s[i+1].isnumeric()) or (s[i].isnumeric() and s[i-1].isnumeric() and s[i+1].isnumeric() == False) or (s[i].isnumeric() and s[i-1].isnumeric()):
            temp+=s[i]
            if i == len(s)-2 and s[len(s)-1].isnumeric():
                temp+=s[len(s)-1]
            if len(s)-2 == i and temp!="":
                lst1.append(int(temp))
        else:
            if temp!="":
                lst1.append(int(temp))
                temp = ""
    return sum(lst1)


#6. Write a function which when given a non-negative integer n and an arbitrary base b, returns the number reversed in that base.

def numToBase(num,base):
    if num==0:
        return 0
    rev=0
    if base==1:
        return num
    while num>0:
        rem=num%base
        rev=rev*base+rem
        num//=base
    return rev


#7. Kevin is noticing his space run out! Write a function that removes the spaces from the values and returns an array showing the space decreasing.
#For example, running this function on the array ['i', 'have','no','space'] would produce ['i','ihave','ihaveno','ihavenospace']

def spacey(array):
    for i in range(len(array)):
        if i != 0:
            array[i] = array[i-1]+array[i]
    return array

#8. Create a function that checks if the first argument n is divisible by all other arguments (return true if no other arguments)

def is_divisible(*lst):
    check = lst[0]
    for i in range(1,len(lst)):
        if check%lst[i] != 0:
            return False
    else:
        return True
    
#9. Make a program that filters a list of strings and returns a list with only your friends name in it.

# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

# i.e.

# friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
# Note: keep the original order of the names in the output.

def friend(x):
    lst1 = []
    for i in x:
        if len(i) == 4:
            lst1.append(i)
    return lst1