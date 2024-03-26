def l_t_s(str1):
    temp = 0
    for i in str1:
        temp+=ord(i)
    return temp

str1 = input("Enter a string : ")
print(l_t_s(str1))