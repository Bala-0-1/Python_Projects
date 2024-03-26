# Find the largest 4-digit number such that the first digit specifies the number of zeroes in the number, the second digit represents the number of 1's in the number, the third digit represents the number of 2's and the last digit represents the number of 3's in the number. 

# Can you extend your program to get the number of digits and generalize the problem for an n-digit number? (Let the maximum number of digits be 10 and not more than that).

def self_descriptive(num):
    lst1 = [int(x) for x in str(num)]
    counter = 0
    for i in lst1:
        if i == num.count(str(counter)):
            counter+=1
            continue
        else:
            return False
    
    return True

def length_of_digits(num):
    return len(str(num))

def largest_self_descriptive(num):
    lst = []
    num1 = "1"
    for i in range(num-1):
        num1 = num1+"0"
    num1 = int(num1)
    while True:
        if length_of_digits(num1) <= num:
            lst.append(num1)
            num1+=1
        else:
            break
    lst = lst[::-1]
    for i in lst:
        if(self_descriptive(str(i))):
            return i
    else:
        return f"There is no {num} digit self descriptive number"

print(largest_self_descriptive(10))