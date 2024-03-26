lst = [x for x in range(1,101)]

def grid_printer(lst):
    n = 10
    for i in range(0,10):
        if i == 0:
            print(*lst[-10+n:n],sep="  | ")
        else:
            print(*lst[-10+n:n],sep=" | ")
        n+=10

def factor(n):
    lst = [1]
    for i in range(1,n):
        if(n%i == 0):
            lst.append(i)
    return lst
    
#returns true if n2 is a multiple of n1
def isMultiple(n1,n2):
    if(n2%n1 == 0):
        return True
    return False

#returns true if the n2 is a factor of n1
def isFactor(n1,n2):
    lst = factor(n1)
    if(n2 in lst):
        return True
    return False

def winning_strategy():
    player1 = []
    player2 = []
    path = []
    print("Welcome to the game...")
    print("RULES:\nThe first player chooses a positive even number that is less than 50, and crosses it out on the grid.\nThe second player chooses a number to cross out.\nThe number must be a factor or multiple of the first number.\nPlayers continue to take it in turns to cross out numbers, at each stage choosing a number that is a factor or multiple of the number just crossed out by the other player.\nThe first person who is unable to cross out a number loses.")
    print("Lessgoooooo......")
    i = 0
    temp2 = 1
    while(True):
        if i == 0:
            grid_printer(lst)
        temp = int(input("Enter your choice, player 1 : "))
        if i == 0 and temp>50:
            print("Read the rules and play the game!")
            i+=1
        if ((temp not in lst) or (isFactor(temp2,temp) or isMultiple(temp2,temp)) == False):
            print("Player 1 lost!")
            return
        else:
            if(temp in lst and (isFactor(temp2,temp) or isMultiple(temp2,temp))):
                lst[lst.index(temp)] = "-"
                player1.append(temp)
                path.append(temp)
                grid_printer(lst)
                while(True):
                    temp2 = int(input("Enter yourchoice, player 2 : "))
                    if temp2 not in lst or (isFactor(temp,temp2) or isMultiple(temp,temp2)) == False:
                        print("Player 2 lost!")
                        return
                    else:
                        if(temp2 in lst and (isFactor(temp,temp2) or isMultiple(temp,temp2))):
                            lst[lst.index(temp2)] = "-"
                            player2.append(temp2)
                            path.append(temp2)
                            grid_printer(lst)
                            break
                        else:
                            print("Read the rules!")
                            continue

winning_strategy()
