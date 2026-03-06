# Take input
a = input("Enter the first number ")
b = input("Enter the second number ")

# Try to convert to integers
try:
    c = int(a)
    d = int(b)

# Check for division by zero
    if d == 0:
        print("Cannot divide by zero")
    else:
     # Perform operations
        print("The sum is : ", c + d)
        print("The divided number is : ", c/d)
# This runs if int() conversion fails
except ValueError:
    print("Invalid input")
