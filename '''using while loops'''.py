'''using while loops'''

import random

NUMBER = random.randint(1,10)
ask_guess = True
#while loop
while ask_guess == True:
    guess = int(input("guess a number between 1 and 10"))




    if guess == NUMBER:
       ask_guess == False
     elif guess < NUMBER:
      print("too low")
     else:
      print("too high")

       
    
    
    

print("well done")