# Function to perform basic arithmetic operations

def perform_operation(num1,num2,operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return("Cannot divide by 0.")
        return num1 // num2
    
    def main():
        perform_operation()

    
    if __name__ == "__main__":
        main()