'''demonstrating how a conditional statement(if/else works it asks the user for a password and then checks if its correctt)'''
#asking for a password
SAVED_PASSWORD = ("hello")
password=input("enter password")



#check if its correct

if password == SAVED_PASSWORD:
    print("correct")
else:
    print("incorrect")    