# PUP GRADING SYSTEM
print ("Good day! Iskolar ng Bayan!")
grades = float (input ("What is your grade (in percentage) this semester? "))
if grades >= 97 and grades <= 100:
    print ("You got 1.0, Excellent!")
elif grades >= 94 and grades <= 96:
    print ("You got 1.25, Excellent!")
elif grades >= 91 and grades <= 93:
    print ("You got 1.5, Very Good!")
elif grades >= 88 and grades <= 90:
    print ("You got 1.75, Very Good!")
elif grades >= 85 and grades <= 87:
    print ("You got 2.0, Good!")
elif grades >= 82 and grades <= 84:
    print ("You got 2.25, Good!")
elif grades >= 79 and grades <= 81:
    print ("You got 2.5, Satisfactory!")
elif grades >= 76 and grades <= 78:
    print ("You got 2.75, Satisfactory!")
elif grades == 75:
    print ("You got 3.0, Passed!")
elif grades >= 65 and grades <= 74:
    print ("You got 5.0, Failure")
else:
    print ("Invalid, please enter a range from 65-100 only.")
