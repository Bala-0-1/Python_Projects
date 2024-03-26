def userinput():
    m = int(input("Enter the number of rows : "))
    n = int(input("Enter the number of columns : "))
    lst = []
    print("Enter the values row vice ")
    for i in range(1,m+1):
        lst.append(list(eval(input("Enter the row {} separated by commas : ".format(i)))))
    return lst

