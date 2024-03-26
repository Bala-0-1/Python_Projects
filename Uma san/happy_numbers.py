def digits_splitter(num):
    lst = []
    while(num>0):
        temp = num%10
        num = num//10
        lst.append(temp)
    return lst

def square_sum(num):
    lst = digits_splitter(num)
    Sum = 0
    for i in lst:
        Sum+= i*i
    return Sum
    
def is_happy_number(num):
    while(True):
        val = square_sum(num)
        if(val <= 9):
            if val == 1:
                return True
            else:
                return False
        else:
            num = val
            continue

print(is_happy_number(10572550))