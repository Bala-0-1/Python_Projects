lst = [["Abinaya", 67, 68, 69], ["Arjun" ,70 ,98 ,63], ["Prasanth", 52, 56, 60]]

str1 = input("Enter the name of the person : ")

for i in lst:
    if i[0].lower() == str1.lower():
        temp = [x for x in i if isinstance(x,int)]
        print(sum(temp)//len(temp))
        break
else:
    print("User not found!")