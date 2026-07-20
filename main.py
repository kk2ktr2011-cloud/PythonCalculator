from mathfunctions import *

print("This is a calculator made in Python.")

num1 = int(input("Type in a number: "))
num2 = int(input("Type in another number:"))

operation_true = False
counter = 0

while operation_true == False:
    operation = input("What operation are you going to do? (Addition, Subtraction, Multiplication, Division, Modulus): ")
    operation.lower()

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

print("This is the end of the calculator.")