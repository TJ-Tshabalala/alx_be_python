def safe_divide(numerator, denominator):
    try:
      result =  numerator/denominator
    except ValueError as e:
       print("Error: Please enter numeric values only.")
    except ZeroDivisionError as e:
       print("Error: Cannot divide by zero.")
    except Exception as e:
       print(e)
    else:
       return f"The result of the division is {result :.2f}"

