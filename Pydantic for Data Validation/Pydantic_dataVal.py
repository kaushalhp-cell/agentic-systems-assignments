# Part 1: User Registration Validation
# Create a Pydantic model UserRegister with:
# username (str, min 5 characters)
# email (valid email)
# age (int, must be ≥ 18)
# Validate incoming data and reject invalid inputs

from pydantic import BaseModel, EmailStr, Field, ValidationError


class UserRegister(BaseModel):
    username: str = Field(min_length=5)
    age: int = Field(ge=18)
    email: EmailStr


# test case 1
details = {'username': 'Parag', 'age': 18, 'email': 'parag@gmail.com'}
try:
    user = UserRegister(**details)  # validation happens here
    print(f'Registeration successful!')
    print(f'Username : {user.username}')
    print(f'Age : {user.age}')
    print(f'Email : {user.email}')
except ValidationError as e:
    print("Validation failed")
    print(e)

# test case 2 : Invalid name

details1 = {'username': 'Josh', 'age': 18, 'email': 'parag@gmail.com'}
try:
    user = UserRegister(**details1)  # validation happens here
    print(f'Registeration successful!')
    print(f'Username : {user.username}')
    print(f'Age : {user.age}')
    print(f'Email : {user.email}')
except ValidationError as e:
    print("Validation failed")
    print(e)

# test case 3 : Age < 18

details2 = {'username': 'Parag', 'age': 17, 'email': 'parag@gmail.com'}
try:
    user = UserRegister(**details2)  # validation happens here
    print(f'Registeration successful!')
    print(f'Username : {user.username}')
    print(f'Age : {user.age}')
    print(f'Email : {user.email}')
except ValidationError as e:
    print("Validation failed")
    print(e)

# test case 3 : Invalid email id

details3 = {'username': 'Parag', 'age': 24, 'email': 'parag_mail.com'}
try:
    user = UserRegister(**details3)  # validation happens here
    print(f'Registeration successful!')
    print(f'Username : {user.username}')
    print(f'Age : {user.age}')
    print(f'Email : {user.email}')
except ValidationError as e:
    print("Validation failed")
    print(e)
