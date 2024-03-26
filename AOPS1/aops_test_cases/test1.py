def num(lst):
    lst1 = []
    if len(lst) == 0:
        return "The length of the list should greater than 1"
    for i in lst:
        if i < 150 and i>=0:
            if i%5 == 0 :
                lst1.append(i)
    return lst1

try:
    lst = list(eval(input("Enter the values separated by commas : ")))
    print(*num(lst),sep= " ")
except TypeError:
    print("Invalid data type.\nOnly whole numbers are accepted\nor you might have entered only one number")
except NameError :
    print("Invalid data type!\nOnly numbers are accepted")
except SyntaxError:
    print("Your mistakes might have been one of the below\n1.Consecutive commas\n2.Symbols other than comma\n3.spaces are not accepted\n4.Empty input\nOr you might be messing around")
