def num_odd_even(n):
    if n%2 == 0:
        return n//2
    else:
        return n//2+1

def right(n,str1):
    return "-"*n+str1

def Center(n,str1):
    n1 = num_odd_even(n)
    return "-"*n1+str1+"-"*n1

def left(n,str1):
    return str1+"-"*n




str1 = input("Enter a string : ")
print("""Enter your choice,
      1.left
      2.center
      3.right""")
n = int(input("Enter your preferred alignment : "))

match n:
    case 1:
        print(left(len(str1),str1))
        
    case 2:
        print(Center(len(str1),str1))
    
    case 3:
        print(right(len(str1),str1))
    case _:
        print("Wrong choice.")