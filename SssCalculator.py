print("\n*** Welcome to our Calculator App.***")
print("\n*** INSTRUCTION ***")
print('''
1) + for Addition.
2) - for Subtraction.
3) * for Multiplication.
4) / for Division.
''')

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero."

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

while True:
    operator = input("\nEnter the operator ('+', '-', '*', '/'): ")
    if operator in operations:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        
        result = operations[operator](num1, num2)
        if isinstance(result, float):
            print(f"The result of {num1} {operator} {num2} = {result}")
        else:
            print(result)
            
        choice = input("Want to continue or not? (y/n): ")
        if choice.lower().endswith('n'):
            print("Thank you for using our calculator. Goodbye!")
            break
    else:
        print("Invalid Input. Try Again.")