size = int(input("Enter the size of the pattern: "))


# while True:
#     for row in range(size):
#         print("*" * size, end="")
#     row+=1

# Use a while loop to iterate through each row of the pattern

row= 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()
    row += 1