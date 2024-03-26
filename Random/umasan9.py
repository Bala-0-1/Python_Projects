n = 0
while True:
  if n%3 == 0 and n%4 == 0 and set(str(n))=={'3','4'}:
    print(n)
    break
  else:
    n+=3