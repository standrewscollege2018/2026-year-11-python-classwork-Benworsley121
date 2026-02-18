''' asking usser for two numbers, and then telling them about the numbers'''

#asking user for 2 numbers
number1 = int(input("type in a number"))

number2 = int(input("type in another number"))
#printing their numbers
print( f"your numbers are {number1} and {number2}")

#finding the larger number

if number1 > number2:
   print("Your first number is bigger")

if number2 > number1:
   print("your second number is bigger")

if number1 == number2:
   print("your numbers are equal")

#adding the numbers together

TOTAL = number1 + number2

print( f"Your two numbers added together are{TOTAL}")



