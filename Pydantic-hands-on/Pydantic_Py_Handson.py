# Part 1: You are building a User Registration System for an e-commerce platform.
# Design a Pydantic model system with the following requirements:

# Address Model

# city → string (minimum length 3)
# pincode → string (must be exactly 6 digits)
# User Model

# user_id → integer
# name → string
# email → email string
# age → integer (must be ≥ 18)
# address → nested Address model
# is_premium → optional boolean (default = False)
# Assignment validation should be enabled

from pydantic import BaseModel, EmailStr, Field, ValidationError
from typing import Optional


class Address(BaseModel):
    city: str = Field(min_length=3, description="City Name")
    pincode: str = Field(pattern=r'^\d{6}$', description="6 digit pin-code")


class User(BaseModel):
    user_id: int = Field(gt=0, description="Unique user id")
    name: str = Field(min_length=1, description="User's full name")
    email: EmailStr
    age: int = Field(ge=18)
    address: Address
    is_premium: Optional[bool] = False


class Config:
    validate_assignment = True


# Test the model
if __name__ == "__main__":
    # test case 1
    print("Test 1 : Valid user")
    try:
        user = User(user_id=1, name='Virat Kohli', email='vk18@gmail.com',
                    age=20, address={'city': 'Delhi', 'pincode': '123456'})
        print(
            f'User created:{user.name}, Age:{user.age},Premium: {user.is_premium}')
        print(f'Address: {user.address.city}, Pincode: {user.address.pincode}')
    except ValidationError as e:
        print(f'Validation failed: {e}')

print("\n"+"="*60+"\n")

# Test Case 2: Invalid age (< 18)
try:
    user = User(user_id=2, name='John Doe', email='johndoe@gmail.com',
                age=17, address={'city': 'Mumbai', 'pincode': '400023'})
    print(
        f'User created:{user.name}, Age:{user.age},Premium: {user.is_premium}')
    print(f'Address: {user.address.city}, Pincode: {user.address.pincode}')
except ValidationError as e:
    print(f'Validation failed: {e}')
    for error in e.errors():
        print(f'Field :{error['loc']}')
        print(f'Error :{error['msg']}')

print("\n"+"="*60+"\n")
# Test Case 3: Invalid pincode (not 6 digits)
try:
    user = User(user_id=3, name='Lionel Messi', email='lmessi@gmail.com',
                age=22, address={'city': 'Paris', 'pincode': '12345'})
    print(
        f'User created:{user.name}, Age:{user.age},Premium: {user.is_premium}')
    print(f'Address: {user.address.city}, Pincode: {user.address.pincode}')
except ValidationError as e:
    print(f'Validation failed: {e}')
    for error in e.errors():
        print(f'Field :{error['loc']}')
        print(f'Error :{error['msg']}')
print("\n"+"="*60+"\n")

# Test 4: Invalid pincode (has letters)
try:
    user = User(user_id=3, name='Virender Sehwag', email='Vsehwag@gmail.com',
                age=25, address={'city': 'Washington', 'pincode': '123AVC'})
    print(
        f'User created:{user.name}, Age:{user.age},Premium: {user.is_premium}')
    print(f'Address: {user.address.city}, Pincode: {user.address.pincode}')
except ValidationError as e:
    print(f'Validation failed: {e}')
    for error in e.errors():
        print(f'Field :{error['loc']}')
        print(f'Error :{error['msg']}')
print("\n"+"="*60+"\n")


# Test 5: Invalid city

try:
    user = User(user_id=3, name='Virender Sehwag', email='Vsehwag@gmail.com',
                age=25, address={'city': 'LA', 'pincode': '123456'})
    print(
        f'User created:{user.name}, Age:{user.age},Premium: {user.is_premium}')
    print(f'Address: {user.address.city}, Pincode: {user.address.pincode}')
except ValidationError as e:
    print(f'Validation failed: {e}')
    for error in e.errors():
        print(f'Field :{error['loc']}')
        print(f'Error :{error['msg']}')
print("\n"+"="*60+"\n")
