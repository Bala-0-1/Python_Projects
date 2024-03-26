def is_valid_isbn_10(isbn):
    cleaned_isbn = ''.join(filter(str.isdigit, isbn))
    if len(cleaned_isbn) != 10:
        return False
    checksum = 0
    for i in range(9):
        checksum += int(cleaned_isbn[i]) * (i + 1)
    checksum %= 11
    last_digit = cleaned_isbn[-1]
    if last_digit == 'X':
        last_digit_value = 10
    elif last_digit.isdigit():
        last_digit_value = int(last_digit)
    else:
        return False
    return (checksum + last_digit_value) % 11 == 0

def is_valid_isbn_13(isbn):
    cleaned_isbn = ''.join(filter(str.isdigit, isbn))
    if len(cleaned_isbn) != 13:
        return False
    checksum = sum(int(cleaned_isbn[i]) * (3 if i % 2 == 0 else 1) for i in range(12))
    checksum %= 10
    return (10 - checksum) % 10 == int(cleaned_isbn[-1])

def main(isbn):
    if len(isbn) == 10:
        if is_valid_isbn_10(isbn):
            return True
        else:
            return False
    elif len(isbn) == 13:
        if is_valid_isbn_13(isbn):
            return True
        else:
            return False
    else:
        return False

n = int(input("Enter the number of isbn numbers : "))
lst1 = []
lst2 = []
for i in range(0,n):
    temp = input("Enter a isbn number : ")
    if(main(temp)):
        lst1.append(temp)
    else:
        lst2.append(temp)

if(len(lst2) > 0):
    print("Invalid ISBN numbers : ",len(lst2))
    for i in lst2:
        print(i)
else:
    print("All passed!")