# Basic Calculator Program

def calculator():
    # Get user input
    num1 = float(input("Enter first number: "))
    operator = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    
    # Perform calculation
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operator! Please use +, -, *, or /.")
        return
    
    # Display result
    print(f"{num1} {operator} {num2} = {result}")

# Run the calculator
calculator()
