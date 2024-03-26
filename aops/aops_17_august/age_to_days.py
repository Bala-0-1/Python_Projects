from datetime import date

def splitter(n):
    lst =[]
    lst.append(n[0:2])
    lst.append(n[3:5])
    lst.append(n[6:10])
    return lst[::-1]


def days_calc(m,n):
    if m > n:  
        return (m-n).days
    else:
        return (n-m).days

print("Only the below format is supported\ndd/mm/yyyy")
from_date = input("Enter your birthday : ")
to_date = input("Enter the to date : ")
if '/' in from_date and len(from_date) == 10:
    if from_date[2] == '/' and from_date[5] == '/':
        frm = splitter(from_date)
        frm = [int(x) for x in frm]
    else:
        print("You've messed up the slashes of the from date.")
    if to_date[2] == '/' and to_date[5] == '/':
        to = splitter(to_date)
        to = [int(x) for x in to]
    else:
        print("You've messed up the slashes of the to date.")
    if from_date[2] == '/' and from_date[5] == '/' and to_date[2] == '/' and to_date[5] == '/':
        no_of_days = days_calc(date(frm[0],frm[1],frm[2]),date(to[0],to[1],to[2]))
        print(no_of_days)
else:
    print("Invalid format")


