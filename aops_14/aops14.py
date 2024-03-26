def NumMultiply(lst):
 # lst=[1,2,3,4,5,6,7,8,9,10]
 res = 1
 for i in lst: 
  res*=i
 print("The list is : ", lst)
 print("The multiplied value is : ", res)

def sumPosNeg(lst): 
 # lst=[1,2,-3,6,-8,9,-2,10]
 pos = 0
 neg = 0
 for i in lst: 
  if i<0:
   neg+=i
  else: 
   pos+=i
 print("The list is : ",lst)
 print("Sum of positive numbers : ", pos)
 print("Sum of negative numbers : ", neg)
 
def numcheck(lst): 
 # lst=[1,2,3,4,5,6]
 n=int(input("Enter a number : "))
 print("The list is : ", lst)
 if n in lst: 
  print("The index of {} is {}: ".format(n,lst.index(n)))
 else: 
  print("The number is not present in the list")

def permutation(lst): 
  lst1 = []
  for i in range(3):
    if i == 0:
      temp = [lst[0],lst[1],lst[2]]
      lst1.append(temp)
      lst1.append(temp[::-1])
    elif i == 1:
      temp = [lst[1],lst[0],lst[2]]
      lst1.append(temp)
      lst1.append(temp[::-1])
    elif i == 2:
      temp = [lst[1],lst[2],lst[0]]
      lst1.append(temp)
      lst1.append(temp[::-1])
  print(lst1)        




def duplicatesduplicates(lst):
  lst = list(set(lst))
  print(lst)




def words_extraction():
  str1 = input("Enter a string : ")
  n = input("Enter the starting letter : ")
  lst = str1.split(" ")
  lst1 = []
  for i in lst:
    if i[0] == n:
      lst1.append(i)
  print(*lst1,sep = "  ")



def month_order():
    month = ['January','February','March','April','May','June', 'July','August','September','October','November','December']
    month_dict = {x:y for y,x in list(enumerate(month))}
    lst=["March", "May", "April", "January", "February"]
    lst.sort(key=lambda month: month_dict[month])
    print(lst)


def neighbour(lst):
  for i in range(len(lst)-1):
    if lst[i] > lst[i+1]:
      continue
    else:
      lst[i] = lst[i+1]
  print(lst)


def sorting(lst):

  n = int(input("Enter the number : "))
  minlist = [x for x in lst if x < n]
  maxlist = [x for x in lst if x > n]
  print("Elements lesser than n :",minlist)
  print("Elements greater than n :",maxlist)

def function_caller():
  lst = list(eval(input("Enter the list values separated by commas : ")))
  print("List multiplier : ")
  NumMultiply(lst)
  print()
  print("Sum of positive and negative : ")
  sumPosNeg(lst)
  print()
  print("Index of number : ")
  numcheck(lst)
  print()
  print("Duplicate remover : ")
  duplicatesduplicates(lst)
  print()
  print("word extraction : ")
  words_extraction()
  print()
  print("month sorting : ")
  month_order()
  print()
  print("Neighbour : ")
  neighbour(lst)
  print()
  print("Sorting : ")
  sorting(lst)
  print()


function_caller()