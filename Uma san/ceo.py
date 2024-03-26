n = 100
Sum = 0
while sum(range(n))!=Sum:
    Sum = 0
    c = n
    while Sum<=sum(range(n)):
        if Sum == sum(range(n)):
            print("The CEO's room number is : ",n)
            print("The total number of rooms : ",c)
            break
        c+=1
        Sum+=c
    n+=1  