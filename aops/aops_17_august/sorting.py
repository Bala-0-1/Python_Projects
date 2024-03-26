
lst = [3,7,1,4,2]
    
# Selection sort 

def selection_sort(lst):
    count1 = 0
    count2 = 0
    for i in range(len(lst)):
        count1+=1
        for j in range(len(lst)):
            count2+=1
            if lst[i] < lst[j]:
                lst[i],lst[j] = lst[j],lst[i]
    return lst

#Bubble sort

def bubble_sort(lst):
    count1 = 0
    count2 = 0
    for i in range(len(lst)-1):
        count1+=1
        for j in range(len(lst)-i-1):
            count2+=1
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst

#Quick sort

def quick_sort(lst,pivot=len(lst)-1):
    min_value = 0
    for i in range(len(lst)-1):
        if(lst[i]>lst[pivot]):
            temp_position = i
            if(lst[temp_position]<lst[min_value]):
                temp_position = min_value
            min_value = i
        if(lst[i]<lst[i+1]):
            lst[i],lst[i+1] = lst[i],lst[i+1]
    lst[pivot],lst[temp_position] = lst[temp_position],lst[pivot]
    return lst

import random
def quick_sort(lst):
    if len(lst)<=1:
        return lst
    pivot,left,right,middle=random.choice(lst),[],[],[]
    for i in lst:
        if i < pivot:
            left.append(i)
        elif i==pivot:
            middle.append(i)
        else:
            right.append(i)
    left=quick_sort(left)
    right=quick_sort(right)
    return left+middle+right

# insertion sort
# start from index 1 in first loop, start from 0 index in the second loop and sort.
# time: n squared

def insertion_sort(lst):
    for i in range(1,len(lst)):
        for j in range(i):
            if lst[i]<lst[j]:
                lst[j],lst[i]=lst[i],lst[j]
    return lst

#merge sort
# 
#

def merge(first,second):
    final=[]
    i,j=0,0
    while (i<len(first) and j<len(second)):
        if (first[i]<second[j]):
            final.append(first[i])
            i+=1
        else:
            final.append(second[j])
            j+=1
    final += first[i:]
    final += second[j:]
    return final

def merge_sort(lst):
    if len(lst)<=1:
        return lst
    mid = len(lst)//2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left,right)

print(merge_sort([1,2,3,4,5,6,7,8,9,10]))

#binary sort
import random
def binary_sort():
    def bogo(lst):
        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:
                return False
        return True
    while not bogo(lst):
        random.shuffle(lst)
    return lst

