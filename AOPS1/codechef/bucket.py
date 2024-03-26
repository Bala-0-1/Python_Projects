n=int(input())
for i in range(n):
    num=int(input())
    lst=sorted(list(map(int,input().split())))
    Sum=sum(lst)
    for i in range(num):
        print(Sum,end=' ')
        Sum-=lst[i] 