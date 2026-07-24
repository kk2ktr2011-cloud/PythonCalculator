from functions import *

print("This is a calculator made in Python.")

history = []

continue_or_not = True

while continue_or_not == True:    
    operation = input("What feature are you going to do? (Addition, Subtraction, Multiplication, Division, Modulus, View History, Delete History): ")
    
    operation = operation.lower()

    if operation == "addition" or operation == "add":
        num1, num2 = check_num()
        addition(num1, num2)
        history.append(f"{num1} + {num2} = {num1 + num2}")
     
    elif operation == "subtraction" or operation == "subtract":
        num1, num2 = check_num()
        subtraction(num1, num2)
        history.append(f"{num1} - {num2} = {num1 - num2}")

    elif operation == "division" or operation == "divide":
        num1, num2 = check_num()
        division(num1, num2)
        history.append(f"{num1} / {num2} = {num1 / num2}")

    elif operation == "multiplication" or operation == "multiply":
        num1, num2 = check_num()
        multiplication(num1, num2)
        history.append(f"{num1} * {num2} = {num1 * num2}")
    
    elif operation == "modulus" or operation == "remainder":
        num1, num2 = check_num()
        modulus(num1, num2)
        history.append(f"{num1} % {num2} = {num1 % num2}")
        
    elif operation == "view history":
        for number, entry in enumerate(history, start=1):
            print(f"{number}. {entry}")
        
    elif operation == "delete history":
        if not history:
            print("The history is empty. ")
            
        else:
            for number, entry in enumerate(history, start=1):
                print(f"{number}. {entry}")
            while True:
                index = input("Which entry would you like to delete(EX: split them through commas or write all): ")
                success = False
                
                if index == "all":
                    history.clear()
                    break
            
                else:
                    try:
                        clean_text = index.split(",")
                        index_array = [int(x) for x in clean_text]
                        index_array.sort(reverse=True)
                        for entry in index_array:
                            entry -= 1
                            if 0 <= entry < len(history):
                                deleted = history.pop(entry)
                                print(f"{deleted} was deleted. ")
                            else:
                                print(f"{entry+1} is out of range.")
                                continue
                            success = True
                    except ValueError:
                        print("Please enter a valid number or 'all'. Try again. ")
                if success == True:
                    break
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