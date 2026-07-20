def addition(num1, num2):
    print(f"The sum of your numbers is {num1 + num2}")
    
def subtraction(num1, num2):
    print(f"The difference of your numbers is {num1 - num2}")
    
def division(num1, num2):
    print(f"The quotient of your numbers is {num1/num2}")
    
def multiplication(num1, num2):
    print(f"The product of your numbers is {num1 * num2}")
    
def modulus(num1, num2):
    print(f"The remainder of your numbers is {num1 % num2}.")
    
def check_num():
    while True:
        try:
            num1 = int(input("Type in an integer: "))
            break
        except ValueError:
            print("Your first number was invalid. Try again: ")
            
    while True:
        try:
            num2 = int(input("Type in another integer: "))
            break
        except ValueError:
            print("Your first number was invalid. Try again: ") 
            
    return num1, num2