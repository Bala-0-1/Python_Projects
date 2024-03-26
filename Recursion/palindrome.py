def isPalindrome(str1,index,str2):
    if len(str1) == len(str2):
        if str1 == str2:
            return True
        else:
            return False
    str2+=str1[index]
    return isPalindrome(str1,index-1,str2)
    
print(isPalindrome(5,-1,""))
