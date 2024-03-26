lst = set()
for i in range(100, 1000):
  j = i
  while j > 1:
    k = j % 10
    j = j//10
    if k == 5:
      lst.add(i)
      continue
print("The numbers that comtains atleast one five: " ,sorted(lst))
print("The number of numbers that contains atleast one five:",len(lst))
