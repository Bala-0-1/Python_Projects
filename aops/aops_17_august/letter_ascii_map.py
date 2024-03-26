str1 = input('Enter the letters : ')
lst = str1.split(',')
dict_lst = {}
for i in lst:
    dict_lst[i] = ord(i)
print(dict_lst)
