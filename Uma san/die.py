count = 0
lst = [1,2,3,4,5,6]
lst2 = [1,2,3,4,5,6]
for i in lst:
    for j in lst2:
        if i+j == 8 or i%2 == 0:
            count+=1
print(count)