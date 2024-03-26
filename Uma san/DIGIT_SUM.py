lst = []

for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            if i+j == k:
                lst.append([(i,j),k])

print("The number of three digit numbers that satisfies the given condition : ",len(lst))
print()
print()
print("The numbers are : ",*lst,sep=" ")