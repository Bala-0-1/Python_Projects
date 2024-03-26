# Dominique wrote down the 1000-digit number 200820082008...2008.

# She then erased some digits and was surprised to find that the remaining digits added up to 2008.

# What is largest number of digits that she could have erased?

# 0 - 500
# 2 - 250
# 8 - 250

def erasing_digits(num,target):
    set1 = sorted(list(set(num)),reverse=True)
    total_num_needed = 0
    value = 0
    occurence_lst = []
    for i in set1:
        occurence_lst.append(num.count(i))
    j = 0
    for i in occurence_lst:
        if value == target:
            break
        count = 1
        while(count<=i):
            if(value == target):
                break
            value += int(set1[j])
            total_num_needed += 1
            count+=1
    if(target == value):
        return (True,value,total_num_needed,1000-total_num_needed)
    else:
        return (False,False)
        
            
    
str1 = "2213"*250
tup = erasing_digits(str1,2008)
if(tup[0]):
    print(f'''
            
Total numbers needed : {tup[2]}

Maximum numbers that can be erased : {tup[3]}
        

        ''')
else:
    print("Not possible")