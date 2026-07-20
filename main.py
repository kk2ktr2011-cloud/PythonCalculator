from functions import *

print("This is a calculator made in Python.")

counter = 1

history = []

continue_or_not = True

while continue_or_not == True:    
    operation = input("What feature are you going to do? (Addition, Subtraction, Multiplication, Division, Modulus, View History, Delete History): ")
    
    operation = operation.lower()

    if operation == "addition" or operation == "add":
        num1, num2 = check_num()
        addition(num1, num2)
        history.append(f"{counter}. {num1} + {num2} = {num1 + num2}")
        counter += 1
     
    elif operation == "subtraction" or operation == "subtract":
        num1, num2 = check_num()
        subtraction(num1, num2)
        history.append(f"{counter}. {num1} - {num2} = {num1 - num2}")
        counter += 1

    elif operation == "division" or operation == "divide":
        num1, num2 = check_num()
        division(num1, num2)
        history.append(f"{counter}. {num1} / {num2} = {num1 / num2}")
        counter += 1

    elif operation == "multiplication" or operation == "multiply":
        num1, num2 = check_num()
        multiplication(num1, num2)
        history.append(f"{counter}. {num1} * {num2} = {num1 * num2}")
        counter += 1
    
    elif operation == "modulus" or operation == "remainder":
        num1, num2 = check_num()
        modulus(num1, num2)
        history.append(f"{counter}. {num1} % {num2} = {num1 % num2}")
        coutner += 1
        
    elif operation == "view history":
        for entry in history:
            print(entry)
        
    elif operation == "delete history":
        if not history:
            print("The history is empty. ")
            
        else:
            for entry in history:
                print(entry)
        
            while True:
                index = input("Which entry would you like to delete(EX: 1 or all).")
        
                if index == "all":
                    history.clear()
                    break
            
                else:
                    try:
                        index = int(index)
                        index -= 1
                        if 0 <= index < len(history):
                            deleted = history.pop(index)
                            print(f"{deleted} was deleted. ")
                            break
                        else:
                            print("The entry you gave is out of range. Try again. ")
                            continue
                    
                    except ValueError:
                        print("Please enter a valid number or 'all'. Try again. ")
                        continue
    else:
        print("Invalid operation. Please try again.")
        continue
    
    y_n = "a"
    
    while y_n != "y" and y_n != "n":
        y_n = input("Would you like to continue? Y/N: ")
        y_n = y_n.lower()
    
    if y_n == "y":
        continue_or_not = True

    elif y_n == "n":
        continue_or_not = False

print("This is the end of the calculator.")