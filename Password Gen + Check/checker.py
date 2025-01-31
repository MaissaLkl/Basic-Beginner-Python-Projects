import string 

def pass_checker(password):
    digits = string.digits
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    specs = string.punctuation

    has_digit = any(char in digits for char in password)
    has_lowercase = any(char in lowercase for char in password)
    has_uppercase = any(char in uppercase for char in password)
    has_specs = any(char in specs for char in password)

    if len(password) >= 8 and has_digit and has_lowercase and has_uppercase and has_specs:
        print("Your password is strong.")
    else: 
        print("Your password is weak.")

password = input("Enter your password: ")
pass_checker(password)
