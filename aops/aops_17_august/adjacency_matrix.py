str1 = input("Enter a string separated by commas : ")
lst = str1.split(",")
adj = input("Enter the adjacency values separated by commas : ")
lst1 = adj.split(",")
for i in range(len(lst)):
    if lst[i] == lst1[0] and lst[i+1] == lst1[1]:
        print("True")
        break
else:
    print("False")