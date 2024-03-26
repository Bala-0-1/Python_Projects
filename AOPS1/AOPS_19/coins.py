n = int(input("Enter the amount : "))
lst = sorted([1,3,5,7,11],reverse=True)
lst1 = []
for i in lst:
    count = 0
    temp = 0
    while(True):
        if(temp<=(n-i)):
            temp+=i
            count+=1
        else:
            break
    lst1.append(count)
    n-=count*i

print(lst1)

lst.index()


