def mat_gen(n):
  lst = []
  for i in range(n):
    lst.append([x for x in "*" * n])
  return lst


def h_glass(n):
  lst = mat_gen(n)
  for i in range(len(lst) // 2 + 1):
    if i == 0:
      continue
    neg = -1
    for j in range(i):
      lst[i][j] = " "
      lst[i][neg] = " "
      neg -= 1
  lst[len(lst) // 2 + 1:len(lst)] = lst[0:len(lst) // 2]
  return lst[::-1]

for i in h_glass(9):
  print(*i, sep=" ")