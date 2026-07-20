from functions import *

print("This is a calculator made in Python.")

num1, num2 = check_num()

operation_true = False
counter = 0

while operation_true == False:
    
    if counter == 0:
        operation = input("What operation are you going to do? (Addition, Subtraction, Multiplication, Division, Modulus): ")
    
    elif counter > 0:
        operation = input("You typed in an invalid operation. Try again: ")
    
    operation = operation.lower()

    if operation == "addition" or operation == "add":
        addition(num1, num2)
        break
     
    elif operation == "subtraction" or operation == "subtract":
        subtraction(num1, num2)
        break
        
    elif operation == "division" or operation == "divide":
        division(num1, num2)
        break

    elif operation == "multiplication" or operation == "multiply":
        multiplication(num1, num2)
        break
    
    elif operation == "modulus" or operation == "remainder":
        modulus(num1, num2)
        break
    
    else:
        counter += 1

print("This is the end of the calculator.")