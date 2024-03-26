#1). Intersection of two lists.

def intersection(lst1,lst2):
    temp = []
    for i in range(len(lst1)):
        for j in range(len(lst1[i])):
            if lst1[i][j] == lst2[i][j]:
                temp.append(lst1[i][j])
    return temp

#2). Consider you have 3 numbers and create a list containing different combinations of all three elements by using a loop.

def comb_3(lst):
    pass