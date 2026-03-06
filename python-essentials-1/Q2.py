# Take input
a = input("Enter the first name: ")
b = input("Enter the second name: ")
c = input("Enter the age: ")

# convert age to integer
try:
    c = int(c)

# Check for division by zero
    if c < 0:
        print("Age cannot be negative")
    elif c == 0:
        print("Age cannot be equal to zero")
    else:
        print("Full name is : ", a + " " + b)
        print("You will be", c+1, "next year")
# This runs if int() conversion fails
except ValueError:
    print("Invalid age input")
