a = 0
b = 1
c = 2
while True:
    sum = a*b*c
    if sum!=1716:
        a+=1
        b+=1
        c+=1
    else:
        break
print("age of first sister : ",a)
print("age of second sister : ",b)
print("age of third sister : ",c)