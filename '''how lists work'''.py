'''how lists work'''

#use square brackets andd commas after every name.
 
#  also use quatation marks for every word.


names = ["Benn", "neb", "ebn", "bne"]

#printing the names is good for debugging.

print(names)

#decides which name will be printed
#will print the 4th one becasue computer starts counting at 0

print(names[3])

#-1 is the last item in the list

print(names[-1])


#setting lenth as names

length=len(names)



#will print out the length of the first name

print(len(names[0]))

#adding names
names[2] = "white beard"

print(names)

#inserting for 1 
names.insert(1, "notben")

print(names)
#adding names on the end
names.append("worsley")

print(names)

#for loop

for name in names:
    print(name)

for i in range(len(names)):
    print( f"{i+1} {names[i]}")


