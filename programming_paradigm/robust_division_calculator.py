def  safe_divide(numerator,denominator):
                try:
                    result =  float(numerator)/float(denominator)
                except ZeroDivisionError as e:
                   return("Error: Cannot divide by zero.")
                except ValueError as e:
                   return("Error: Please enter numeric values only.")
                except Exception as e:
                   print(e)
                else:
                   return(f"The result of the division is {result}")

