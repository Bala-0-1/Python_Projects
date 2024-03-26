n = int(input("Enter the dimension 'n' of the chessboard:"))
res = 0
for i in range(1, n + 1):
  res = res + (i * i)
print("The number of squares is:", res)
  