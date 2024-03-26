lst = [str(x) for x in range(100,1000)]
count = 0
lst1 = []
for i in lst:
    if int(i[0])+int(i[1]) == int(i[2]):
        count+=1
        lst1.append(i)
    
    
print(lst1)
print(count)