import random
import time


#https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
import os
def clear():
    os.system('cls' if os.name=='nt' else 'clear')


global p_score      #Declaring global variable for easy access by all functions
global c_score      #Declaring global variable for easy access by all functions
def play_toss():#The function for Declaring the toss result and winner of toss
  player=int(input("ENTER YOUR CHOICE ODD=1,EVEN=2: "))
  toss_input=int(input("Pick Your Number:[0,1,2,3,4,5,6]"))
  comp_input=random.randint(0,6)#random function has been used to identify computer's input
  dec=["score","defend"]
  scorer=""
  if (toss_input+comp_input)%2==0:#declaring toss result
    toss=2
  else:
    toss=1
  time.sleep(.5)
  if toss==player:
    print("You have won the toss")
    time.sleep(.5)
    x=int(input("1.Scoring 2.Defending\n"))
    print("You have chosen to,",dec[x-1],"first")
    time.sleep(.5)
  else:
    x=random.randint(1,2)
    print("opponent has chosen to",dec[2-x],"first")
  if x==1:
        scorer="p"
  else:
        scorer="c"
  return scorer
#Function to play the match 
def match():
  r=play_toss() #toss function is called for evaluating the toss
  p_score=0
  c_score=0
  if r=="p":
    while True:
      print("Your score=",p_score)
      time.sleep(.5)
      a=int(input("Enter your Choice For Scoring\n[0,1,2,3,4,5,6]\n"))%7
      b=random.randint(0,6)
      print("Your choice",a)
      time.sleep(0.8)
      print("Computer's choice",b)
      time.sleep(0.5)
      if a==b:
        print("Your wicket has been taken by computer\nYour score",p_score)
        time.sleep(0.5)
        print("Score for computer to win--",p_score+1)
        time.sleep(.5)
        break
      elif a==0:
        p_score+=b
      else:
        p_score+=a
      time.sleep(1)
      clear()
    while True:
      print("Computer's score",c_score)
      time.sleep(.5)
      a=int(input("Enter your Choice For Defending\n[0,1,2,3,4,5,6]\n"))%7
      b=random.randint(0,6)
      time.sleep(.5)
      print("Your choice",a)
      time.sleep(0.8)
      print("Computer's choice",b)
      time.sleep(0.5)
      if a==b and c_score<p_score:
        print("Hurray you have taken computer's wicket")
        time.sleep(.5)
        print("Your score",p_score)
        time.sleep(.5)
        print("computer's score,",c_score)
        time.sleep(.5)
        if c_score!=p_score:
          print("You have won The game")
        else:
          print("Draw match\nGood game")
        break
      elif b==0:
        c_score+=a
      else:
        c_score+=b
      if c_score>p_score:
        print("OOps Computer has won the game\n:(\nbetter luck next time")
        break
      time.sleep(1)
      clear()
  else:
    while True:
      print("Computer's score",c_score)
      a=int(input("Enter your Choice For Defending\n[0,1,2,3,4,5,6]\n"))%7
      b=random.randint(0,6)
      print("Your choice",a)
      time.sleep(0.8)
      print("Computer's choice",b)
      time.sleep(0.5)
      if a==b:
        print("Hurray you have taken computer's wicket")
        time.sleep(.5)
        print("computer's score,",c_score)
        time.sleep(.5)
        print("Score for you to win",c_score+1)
        time.sleep(.5)
        break
      elif b==0:
        c_score+=a
      else:
        c_score+=b
      time.sleep(1)
      clear()
    while True:
      print("Your score=",p_score)
      time.sleep(.5)
      a=int(input("Enter your Choice For Scoring\n[0,1,2,3,4,5,6]\n"))%7
      b=random.randint(0,6)
      time.sleep(.5)
      print("Your choice",a)
      time.sleep(0.8)
      print("Computer's choice",b)
      time.sleep(0.5)
      if a==b and p_score<=c_score:
        print("Your wicket has been taken by computer\nYour score",p_score)
        time.sleep(.5)
        print("Computer's score",c_score)
        time.sleep(.5)
        if c_score!=p_score:
          print("You have lost The game")
        else:
          print("Draw match\nGood game")
        break
      elif a==0:
        p_score+=b
      elif a!=0:
        p_score+=a
      if p_score>c_score:
        print("You have won the match\nCongrats!!!")
        break
      time.sleep(1)
      clear()
#mainmenu function for initialising the main menu
def Mainmenu(): 
    print("Odd Or Even") 
    print("W-E-L-L-C-O-M-E")
    print("===============")
    time.sleep(0.5)
    print("  MAIN MENU  ")
    print("+-+-+-+-+-+-+")
    time.sleep(1)
    print("|1.Lets PLay    |")
    print("|"+"-"*16)
    time.sleep(0.5)
    print("|2.Rule Book    |")
    print("|"+"-"*16)
    time.sleep(0.5)
    print("|Enter Q to Quit|")
    print("|"+"-"*16)
    time.sleep(0.5)
    menu_choice=input("Enter your choice: \n")
    time.sleep(0.5)
    clear()
    if menu_choice=="1":
        print("if your choice is out of range\nit will be truncated as the remainder received when divided by the range")
        match()
        req_con=input("Do you wish to continue[Y/N]\n{press any thing to exit}\n")
        if req_con in "Yy":
          return True
        else:
          return False

    elif menu_choice=="2":
        z=open("data.txt")
        print("Press enter to go to next Instruction")
        for l in z:
            print(l)
            input()
            continue
        return True
    elif menu_choice in "Qq":
        print("Thank you for playing")
        return False
    else:
        print("INVALID INPUT!!!!\ntry again after 2 seconds")
        time.sleep(2)
        return True
        

#excecution block 
while True:
  if not Mainmenu():
    break
  clear()
#end



    

    


