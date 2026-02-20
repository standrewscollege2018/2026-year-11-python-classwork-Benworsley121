'''error catching'''


get_num == True
while get_num == True:

try:
    number= int(input("enter a number:"))
    
get_num = False

except ValueError:
    print("that is not a number")
        
     

print(f"your entered {number}")