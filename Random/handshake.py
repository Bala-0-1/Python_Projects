n, lst, temp = int(input("Enter the number of handshakes : ")), [0], 0
for i in range(0, n+1): 
  temp = i + temp
  lst.append(temp)
if n in lst: print("The number of people is : ",lst.index(n))
else:
  maximum, minimum= min([i for i in lst if n < i]), max([i for i in lst if n > i])
  print("""It is not possible. \nBut the nearest values are {} people with {} handshakes and {} people with {} handshakes.""".format(lst.index(minimum) ,minimum, lst.index(maximum),maximum))