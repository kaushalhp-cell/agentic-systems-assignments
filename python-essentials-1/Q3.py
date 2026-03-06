# Take input
name = input("Enter the name: ")
# to check if correct name is entered, not an email id or number or invalid character
if not name.replace(" ", "").isalpha():
    print("Invalid name input")
    exit()

age = input("Enter the age: ")

# convert age to integer
try:
    age = int(age)

    if age < 0:
        print("Age cannot be negative, pls enter once again")
    elif 0 <= age <= 13:
        print("Hello", name, ",you are a child and you are not eligible to vote")
    elif 13 <= age <= 17:
        print("Hello", name, ",you are a teenager you are not eligible to vote")
    elif 18 <= age <= 59:
        print("Hello", name, ",you are an adult and you are eligible to vote")
    elif age > 59:
        print("Hello", name, ",you are a senior citizen and you are eligible to vote")
# This runs if int() conversion fails
except ValueError:
    print("Invalid age input")
