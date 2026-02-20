'''asking for numbers task 2'''


#asking for first number


get_num = True
while get_num == True:
    try:
         number1 = int(input("type in a number"))
         get_num = False
    except ValueError:
        print("that is not a number")
       



 






#while loop
get_num = True
while get_num == True:
    try:
        number2 = int(input("type in a number bigger than your previous one"))
        if number1 >= number2:
            print("your second number should be bigger")

        else:
            get_num = False     
    except ValueError:
        print("that is not a number")


    



    
#typing their numbers

print( f"your numbers are {number1} and {number2}")
  












    

