''' drivers licence lists'''

names = ( "Ben", "bob", "jacob", "fred")

licence_status = ("Restricted", " no licence", "learners", "learners")







#start loping 

change = True

while change == True:

    print("licence_status of students")

    print("=" * 23)


    for i in range(len(names)):
        print(f"{i + 1} {names[i]:>10} {licence_status[i]:10}")

    driver = int(input("select student to update"))

    if driver == 0:
        change = False
    else:
        new_statue = input("enter new status: ")

        status[driver-1] = new_status

