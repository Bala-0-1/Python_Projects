lst=[]
def user():
  global lst
  username=input('enter your name: ')
  pin=int(input('enter 4 digit pin: '))
  deposit=0
  lst.extend([[username],[pin],[deposit]])
  print(lst)
  print('account created')
def Deposit():
  print(lst)
  username=input('enter your name: ')
  pin=int(input('enter your 4 digit pin: '))
  for i in range (len(lst)-1):
      if lst[0][i] == username and lst[1][i] == pin:
          deposit=int(input('enter the amount of money you would like to deposit: '))
          lst[2][i]+=deposit
          print("Deposit successful")
          print(lst)
          break
      else:
          print('wrong pin')
def Withdraw():
  username=input('enter your name: ')
  pin=int(input('enter your 4 digit pin: '))
  for i in range (len(lst)):
      if ([lst[i][0],lst[i],[1]])==[username,pin]:
          val=int(input('enter the amount you want to withdraw: '))
          if lst[i][2]>val:
              lst[i][2]-=val
              print('successfully withdrawn')
              break
          else:
              print('not enough balance')
def ChangePin():
  username=input('enter your name: ')
  pin=int(input('enter your 4 digit pin: '))
  for i in range (len(lst)):
      if ([lst[i][0],lst[i],[1]])==[username,pin]:
          upin=int(input('enter 4 digit pin: '))
          lst[i][1]=upin
          break
def Balance():
  username=input('enter your name: ')
  pin=int(input('enter your 4 digit pin: '))
  for i in range (len(lst)):
      if ([lst[i][0],lst[i],[1]])==[username,pin]:
          print(f"{lst[i][2]} is the account balance")
def atm():
  
  while True:
    print('1.create account\n2.login')
    ch=int(input('enter the choice: '))
    if ch==1:
      user()
    elif ch==2:
      print('choose an action:\n1.Deposit money\n2.Withdraw money\n3.Change pin\n4.Check Balance\n5.Exit')
      choice=int(input('enter the number: '))
      if choice==1:
          Deposit()
          continue
      elif choice==2:
          Withdraw()
          continue
      elif choice==3:
          ChangePin()
          continue
      elif choice==4:
          Balance()
          continue
      elif choice==5:
          print('thank you ')
          break
atm()
