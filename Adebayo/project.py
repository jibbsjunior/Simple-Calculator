'''
A simple calculator program
 This program accepts 2 numbers input from users and then carries out a calculation
 on them
 This calculator dosent accept more than 2 input at a time because is a simple calculator

'''

number1 = float(input("Please enter the first number >>> "))
number2 = float(input("Please enter the second number >>> "))

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
