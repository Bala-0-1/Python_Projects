
num = int(input())
for i in range(num):
    n = input()
    n = n.split(" ")
    lst = [int(x) for x in n]
    set1 = set(lst)
    lst1 = [lst.count(x) for x in set1]
    no_of_people = 0
    for j in lst1:
        if j%2 != 0 :
            no_of_people+=1
    print(no_of_people)
