# Function to perform basic arithmetic operations

def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num2 - num1
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num1 == 0:
            return ZeroDivisionError("Cannot divide by 0.")
        return num2 // num1
    