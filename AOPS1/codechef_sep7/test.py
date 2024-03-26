def generate_pairs_with_repetition(lst):
    pairs = []
    n = len(lst)
    for i in range(n):
        for j in range(n):
            pair = (lst[i], lst[j])
            pairs.append(pair)

    return pairs

for i in range(int(input())):
    n = int(input())
    lst = tuple(map(int,input().split()))
    lst1 = generate_pairs_with_repetition(lst)
    count = 0
    for i in lst1:
        if(i[0]<=i[1]):
            temp = ((lst.index(i[0])+1)+(lst.index(i[1])+1))
            if((i[0]+i[1])%temp == 0):
                count+=1
    print(count)
            
    
    
    
    
    