#1). Convert a decimal number to binary in python without using bin() function

def decimal_to_binary(n):
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary

#2). Transpose a matrix in python

def transpose(lst):
    for i in range(len(lst[0])):
        for j in range(len(lst)):
            lst[i][j] = lst[j][i]
    return lst

#3). Find out the intersection of 2 arrays

def intersection(lst1,lst2):
    temp = []
    for i in range(len(lst1)):
        for j in range(len(lst1[i])):
            if lst1[i][j] == lst2[i][j]:
                temp.append(lst1[i][j])
    return temp

#4). Consider you have a String of TicTacToe board. Find out who is the winner (X or O or is it a draw)

