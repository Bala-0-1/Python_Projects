def printer(str1,n):
    k = 0
    for i in range(len(str1)//n+1):
        print(str1[k:k+n])
        k+=n



str1 =input("Enter a string : ")
n = int(input("Enter the number of characters per line : "))
printer(str1,n)