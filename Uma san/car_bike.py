def parking_problem(num):
    lst = []
    count = 1
    while len(lst)!=num:
        lst.append("c")
        for i in range(count):
            if(len(lst) == 144):
                break
            lst.append("b")
        count+=1
    return lst[len(lst)//2:].count("b")


print(parking_problem(144))