import time
import os
import random
import winsound

bwlist = ["C--R--TER", "B--FIX", "ZO--E", "S--TA-", "P---ON", "VA--AB--S", "SUB-T--NG", "B--L-AN", "-L-M-NT", "-PP--D", \
   "FU--T--N", "S-Q-E-CE", "PRO-RA-", "CO--A-D", "I-P--T", "R-PO-IT-RY", "IN-E--R", "CO--IT--N", "TU-LE", "L--P" ]

wlist = ["CHARACTER", "BUGFIX", "ZOPE", "SYNTAX", "PYTHON", "VARIABLES", "SUBSTRING", "BOOLEAN", "ELEMENT", "APPEND", \
   "FUNCTION", "SEQUENCE", "PROGRAM", "COMMAND", "IMPORT", "REPOSITORY", "INTEGER", "CONDITION", "TUPLE", "LOOP" ]   

os.system("cls")

#------------------------------------------------------------------------
def hangman1():
    print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")

#------------------------------------------------------------------------
def hangman2():
    print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
#------------------------------------------------------------------------
def hangman3():
    print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
#------------------------------------------------------------------------
def hangman4():
    print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
#------------------------------------------------------------------------
def hangman5():
    print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "--╩--           †⚰\n")


#------------------------------------------------------------------------
def timer():

   t = 30
   
   print("Your will have 30 seconds to answer: ", "\r")
   time.sleep(1)
   while t >= 0:
        
        if t != 0:
            winsound.Beep(440, 300)

        secs = t % 60
        timer = "{:02d}".format(secs)
        print("Timer starts now.: ", timer, end="\r")
        time.sleep(1)
        
        t -= 1

   winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
   print("Your 30 seconds time to answer already lapsed. ")
#----------------------------------------------------------------------   

time.sleep(1)
name = input("Please enter your name: ")
continued = input("Press 'Q' to quit the game! or Enter 'S' to Start! ")

print("Lets play Hangman")

if continued == "S" or continued == "s":

   ctr = 0
    
   start = True
   
   ctr = 0 

   randomer = random.randint(0, 20)
      
   print("Hint:", bwlist[randomer], "\n")
   
   timer()

   while start:
      
      questioned = input("Guess the Word: ")   
      
      if questioned.upper() == wlist[randomer]:

         print( "Hurray!!! You answered", wlist[randomer],"!  CONGRATULATIONS!" )

         next = input("Continue the game? Y/N ")

         if next == "Y" or next == "y":

            start = True

            randomer = random.randint(0, 20)
      
            print("Hint:", bwlist[randomer], "\n")
   
            timer()

         elif next == "N" or next == "n":

            start = False

            print("Thank you! We are glad to have you here in our game!")

            break   

         else:

            break
   
      else:
           
         print("Sorry your answer is incorrect!")   

         ctr = ctr + 1
         
         if ctr == 1:

            hangman1()

         elif ctr == 2:

            hangman2()
         
         elif ctr == 3:
            
            hangman3()

         elif ctr == 4:
            
            hangman4()

         elif ctr == 5:

            print("Sorry the correct answer is", wlist[randomer] + ".")
            
            hangman5()  
            print("Thank you for playing Hangman", name+"!", "You have exausted your chance, Better luck next time...")         
            break
         
else:

   print("Thank you", name+"!", "Glad you used our game.")

   os.system("cls")
