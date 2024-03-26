for i in range(int(input())):
    int(input())
    lst = list(map(int,input().split()))
    odd_lst = [x for x in lst if x%2 != 0]
    even_lst = [x for x in lst if x%2 == 0]
    if len(odd_lst) == len(even_lst) or (len(odd_lst) == 1 and len(even_lst) == 0) or len(even_lst) == 0:
        print("YES")
    else:
        print("NO")