try:
    n = int(input("Enter the number : "))
    m = int(input("Enter the range : "))
    lst =[]
    for i in range(1,m+1):
        lst.append(n*i)
    print(*lst,sep=",")
except:
    print("Invalid input.\ntry again!")
