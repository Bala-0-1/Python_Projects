count =0
lst = [x for x in range(1,20)]
lst1 = []
for i in lst:
    
    
    for j in lst:
        for k in lst:
            if i+j+k == 22:
                count+=1
                lst1.append([i,j,k])

for i in lst1:
    print(i)
print(count)