number = int(input("Enter a number to see its multiplication table: "))

for n in range(1,10):
    print(f"{number} * {n} =", number*n)