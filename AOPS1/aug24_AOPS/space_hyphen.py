def space_to_hyphen(str1):
    lst = [x for x in str1]
    for i in lst:
        if i == " ":
            lst[lst.index(i)] = "-"
    return "".join(lst)

str1 = input("Enter a string : ")
print("String with hyphens : ",space_to_hyphen(str1))