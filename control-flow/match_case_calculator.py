num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operator = input("Choose the operation (+, -, *, /): ")

match operator:
    case "+":
        print("The result is ", num1+num2)
    case "-":
        print("The result is ", num2-num1)
    case "/" if num1 == 0:
        print("Cannot divide by zero")
    case "/":
        print("The result is ", num2//num1)
    case "*":
        print("The result is ", num1*num2)
    case _:
        print("Invalid operation")