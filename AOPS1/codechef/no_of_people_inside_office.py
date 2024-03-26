for i in range(int(input())):
    n = int(input())
    val= tuple(map(int, input().split()))
    people_in = set()
    max = 0
    for i in val:
        if i not in people_in:
            people_in.add(i)
            if max<len(people_in):
                max = len(people_in)
        elif i in people_in:
            people_in.remove(i)
    print(max)
