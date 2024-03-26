# def str_splitter(str1):
#     lst = []
#     k = 0
#     for i in range(len(str1)//3):
#         lst.append([str1[k:k+3]])
#         k+=3
#     return lst

# def unique_printer(str1):
#     lst = str_splitter(str1)
#     for i in lst:
#         temp = [str(x) for x in i[0]]
#         print(*i,"=>",*list(set(temp)),sep=" ")

# str1 = input("Enter a string : ")
# unique_printer(str1)

lst = [1,2,3]
print(" ".join(map(str, lst)))