import string
import random

def generate_password():
    total = string.ascii_letters + string.digits + string.punctuation

    length = 16

    password = "".join(random.sample(total,length))
    print(password)

user_response = "yes"
while user_response == "yes" or user_response == "y":
    generate_password()

    user_response = input("Do you want another password? ('yes' or 'no') ").lower()
    print()
    
