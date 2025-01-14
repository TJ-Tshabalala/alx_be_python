# Function to perform basic arithmetic operations

def perform_operation(num1,num2,operation):
    if operation == "add":
        return num1+num2
    elif operation == "subtract":
        return num1-num2
    elif operation == "multiply":
        return num1*num2
    elif operation == "divide":
        if num2 == 0:
            return("Cannot divide by 0.")
        return num1//num2
    
def main():
        num1 = float(int(input("Enter the first number: ")))
        num2 = float(int(input("Enter the second number: ")))
        operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
        result = perform_operation(num1, num2, operation)
        print(f"Result: {result}")

    
if __name__ == "__main__":
        main()