def is_decreasing(num):
    lst = [int(x) for x in str(num)]
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            return False
    else:
        return True
    
print(is_decreasing(952))