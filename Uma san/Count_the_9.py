n = 11
lst = list({1,2,3,4,5,6,7,8,10})
while len(lst)<500:
    num = n
    temp = 100
    while num>8:
        temp = num%10
        num = num//10
        if temp == 9:
            break
    else:
        lst.append(n)
    n+=1
print("The 500th digit is : ",lst[-1])