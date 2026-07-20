from mathfunctions import *

print("This is a calculator made in Python.")

num1 = int(input("Type in a number: "))
num2 = int(input("Type in another number:"))

operation_true = False

while operation_true == False:
    operation = input("What operation are you going to do? (Addition, Subtraction, Multiplication, Division): ")
    operation.lower()

    if operation == "addition" or operation == "add":
        addition(num1, num2)
        operation_true == True
        break
     
    elif operation == "subtraction" or operation == "subtract":
        subtraction(num1, num2)
        operation_true == True
        break
        
    elif operation == "division" or operation == "divide":
        division(num1, num2)
        operation_true == True
        break

    elif operation == "multiplication" or operation == "multiply":
        multiplication(num1, num2)
        operation_true == True
        break

print("This is the end of the calculator.")