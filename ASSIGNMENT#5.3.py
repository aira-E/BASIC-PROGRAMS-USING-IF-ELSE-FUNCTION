#Program 3: Life stages - Create a program that ask for an age of a person. Display the life stage of the person. Rules: 0 - 12 : Kid, 13 - 17 : Teen, 18 : Debut, 19 above : Adult

age = int (input("How old are you? "))
if age >= 0 and age <= 12:
    print ("kid")
if age >= 13 and age <= 17:
    print ("teen")
if age == 18:
    print ("debut")
if age >= 19:
    print ("adult")