import math
n = int(input("How much money do you need : " ))
lst = [1,5,7,9,11]
lowest = []
lst1 = []
for i in range(0,5):
    lowest.append(n/lst[i])
    lst1.append(math.floor(n/lst[i]))
if lst1[-1]*11 == n:
    print("{} 11 rupee coin.".format(lst1[-1]))
else:
    lst2 = []
    coins = lst1[-1]
    remainder = n - lst1[-1]*11
    Sum = n - remainder
    print(Sum)
    print(remainder) 
    while True:
        for i in lst:
            if remainder>i:
                lst2.append(i)
        coins+=lst2[len(lst2)-1]
        print(lst)
        print(lst2)
        lst.remove(lst2[len(lst2)-1])
        Sum = Sum-i
        if Sum <= 0 :

            break
    print(coins)

