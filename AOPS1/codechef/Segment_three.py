for i in range(int(input())):
    n_tables = int(input())
    number_of_dishes = list(map(int,input().split()))
    lst = []
    count = 0
    for j in range(len(number_of_dishes)//3):
        lst.append(number_of_dishes[count:count+3])
        count+=3
    non_divisible_list = [x for x in lst if sum(x)%3 != 0]
    if len(non_divisible_list) == 0:
        print(0)
    else:
        Total_Sum = 0
        for k in non_divisible_list:
            if (sum(k)+1)%3 == 0:
                Total_Sum+=1
            elif (sum(k)+2)%3 == 0:
                Total_Sum+=2
        print(Total_Sum)

    