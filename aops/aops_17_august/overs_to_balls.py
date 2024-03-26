try:
    n = float(input("Enter the number of overs : "))
    rem = ((n%1)*10)//1
    n = n//1
    print("The number of balls : ",n*6+rem)
except:
    print("The number can be only integer or decimal.")

