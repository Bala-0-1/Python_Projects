#st..st...utter
str1 = input("Enter the string : ")
if len(str1)>2:
    rem = str1[0:2]
    str1 = str1[2:len(str1)]    
    print(f"{rem}..{rem}..{str1}")
else:
    print(str1)