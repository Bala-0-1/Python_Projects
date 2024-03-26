def runner_up(lst):
    max = 0
    for i in lst:
        if i>0:
            max = i
    lst.remove(max)
    for i in lst:
        if i>0:
            max = i
    return max

print(runner_up([1,2,3,4,5,6]))