# Program 2: Find the lowest number. Create a program that ask 3 numbers. Find the lowest number using only if-else statement. Display the lowest number

input1 = int (input("Enter 1st Number: "))
input2 = int (input("Enter 2nd Number: "))
input3 = int (input("Enter 3rd Number: "))

def lowest_number (input1,input2, input3):
    if (input1 < input2) and (input1 < input3) :
        smallest_number = input1
    elif (input2 < input1) and (input2 < input3):
        smallest_number = input2
    elif (input3 < input1) and (input3 < input2):
        smallest_number = input3
    print (f"{smallest_number} is the lowest number")
        
smallest_number = lowest_number (input1, input2, input3)
    
