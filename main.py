from functions import *

print("This is a calculator made in Python.")

counter = 0

history = []

continue_or_not = True

while continue_or_not == True:    
    if counter == 0:
        operation = input("What feature are you going to do? (Addition, Subtraction, Multiplication, Division, Modulus, View History): ")
    
    elif counter > 0:
        operation = input("You typed in an invalid operation. Try again: ")
        
    num1, num2 = check_num()
    
    operation = operation.lower()

    if operation == "addition" or operation == "add":
        addition(num1, num2)
        history.append(f"{num1} + {num2} = {num1 + num2}")
        counter = 0
     
    elif operation == "subtraction" or operation == "subtract":
        subtraction(num1, num2)
        history.append(f"{num1} - {num2} = {num1 - num2}")
        counter = 0
        
    elif operation == "division" or operation == "divide":
        division(num1, num2)
        history.append(f"{num1} / {num2} = {num1 / num2}")
        counter = 0

    elif operation == "multiplication" or operation == "multiply":
        multiplication(num1, num2)
        history.append(f"{num1} * {num2} = {num1 * num2}")
        counter = 0
    
    elif operation == "modulus" or operation == "remainder":
        modulus(num1, num2)
        history.append(f"{num1} % {num2} = {num1 % num2}")
        counter = 0
        
    elif operation == "history" or operation == "view history":
        print(history)
        counter = 0
    
    else:
        counter += 1
    
    y_n = "a"
    
    while y_n != "y" and y_n != "n":
        y_n = input("Would you like to continue? Y/N: ")
        y_n = y_n.lower()
    
    if y_n == "y":
        continue_or_not = True

    elif y_n == "n":
        continue_or_not = False


print("This is the end of the calculator.")