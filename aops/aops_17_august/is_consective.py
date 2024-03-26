try:
    lst1 = list(eval(input("Enter the values separated by commas : ")))
    lst2 = list(eval(input("Enter the values separated by commas : ")))
    lst1 = list(set(lst1))
    lst2 = list(set(lst2))
    for i in lst2:
        lst1.append(i)
    lst1.sort()
    


except TypeError:
    print("Invalid data type.\nOnly whole numbers are accepted\nor you might have entered only one number")
except NameError :
    print("Invalid data type!\nOnly numbers are accepted")
except SyntaxError:
    print("Your mistakes might have been one of the below\n1.Consecutive commas\n2.Symbols other than comma\n3.spaces are not accepted\n4.Empty input\nOr you might be messing around")