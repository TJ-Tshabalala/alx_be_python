FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
  global CELSIUS_TO_FAHRENHEIT_FACTOR
  fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  return fahrenheit

def main():
  while True:
    try:
      temperature = float(input("Enter the temperature to convert: "))
      unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
      if unit == 'C':
        converted_temperature = convert_to_fahrenheit(temperature)
        original_unit = 'F'
        (f"{temperature:.1f}°C is {converted_temperature:.1f}°{unit}")
      elif unit == 'F':
        converted_temperature = convert_to_celsius(temperature)
        original_unit = 'C'
        (f"{temperature:.1f}°F is {converted_temperature:.1f}°{unit}")
      else:
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
      print(f"{temperature:.1f}°{unit} is {converted_temperature:.1f} {original_unit}")
      break
    except ValueError:
      print(f"Invalid Temperature. Please enter a numeric value.")

    
if __name__ == "__main__":
  main()