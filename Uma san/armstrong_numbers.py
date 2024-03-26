def cube_of_each_digits(num):
    lst = [int(x) for x in str(num)]
    Sum = 0
    length = len(lst)
    for i in lst:
        Sum+=(i**length)
    return Sum

lst = []
n = 1
while True:
    if n == cube_of_each_digits(n):
        lst.append(n)
        print(n)
    n+=1