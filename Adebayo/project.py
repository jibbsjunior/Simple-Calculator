'''
A simple calculator program
 This program accepts 2 numbers input from users and then carries out a calculation
 on them
 This calculator dosent accept more than 2 input at a time because it's a simple calculator

'''
#This is to take input from user
number1 = float(input("Please enter the first number >>> "))
number2 = float(input("Please enter the second number >>> "))

#This is to tell the user the type of arithmetic operation he can perform
print("To perform arithmetic operation on your numbers,the next thing is for you to make your selecton")
print("When making your selection,you cant make more than 4 option which is addition,division,multilication or subtraction")

#This is to tell the user he should press enter if he is ok by the option
input("\nPress ENTER to CONTINUE")

add = 1
subtract = 2
divide = 3
multiply = 4

selection = int(input("Make your selection now >>> "))
 
if selection == 1:
     result = number1 + number2
elif selection == 2:
     result = number1 - number2
elif selection == 3:
     result = number1 / number2
elif selection == 4:
     result = number1 * number2
else:
     result = "Sorry, that's not a valid selection"

print(result)

input("\n\nPress <ENTER> to quit ...")
