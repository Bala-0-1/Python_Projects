def digit_sum(n):
    sum = 0
    while(n>0):
        sum+=n%10
        n = n//10
    return sum

def is_square(n):
    if(str(n**0.5)[-2]+str(n**0.5)[-1] == ".0"):
        return True
    else:
        return False

lst = []
for i in range(2001,2100):
    if(is_square(digit_sum(i))):
        lst.append(i)

print(lst)

