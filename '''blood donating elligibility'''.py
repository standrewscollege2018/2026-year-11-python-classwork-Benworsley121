'''blood donating elligibility'''
#asking for age

DONOR_AGE = 16
WEIGHT=50

age= int(input("what is your age"))
if age < DONOR_AGE:
    print("you are too young")
else:
    print("you meet the age requirements")

weight=int(input("what is your weight"))

if weight<WEIGHT:
    print("you do not weigh enough")
else:
    print("you weigh enough")