for i in range(int(input())):
    n = int(input())
    lst1 = list(map(int,input().split()))
    lst = set(lst1)
    count = 0
    for i in lst:
        for j in lst:
            if(i<=j):
                temp = i+j
                if(temp%((lst1.index(i)+1)+(lst1.index(j)+1))==0):
                    count+=1
    print(count)