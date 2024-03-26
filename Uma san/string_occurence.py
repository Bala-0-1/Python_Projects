def string_occurence_match(str1):
    set1 = set(x for x in str1)
    length = len(str1)
    for i in set1:
        count = 0
        for j in str1:
            if i == j:
                count+=1
        if count == (length-count):
            return "YES"
    else:
        return "NO"
    
print(string_occurence_match("abaccc"))
