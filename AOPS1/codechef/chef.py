import math
def plates(x,y,r):
    extra_sticks = r//30 # 4
    nospch = math.ceil(x//y)*y # 18
    rem = abs((nospch-x)-extra_sticks) # 0
    e = math.ceil(rem/y) # 0 
    print(math.ceil(x//y)+e) # 

num = int(input())
for i in range(num):
    n = input()
    n = n.split(" ")
    lst = [int(x) for x in n]
    plates(lst[0],lst[1],lst[2])