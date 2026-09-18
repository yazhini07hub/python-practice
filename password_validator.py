password = input("Enter your password: ")

has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)

if len(password) >= 8 and has_upper and has_lower and has_digit:
    print("Password meets the basic requirements.")
else:
    print("Password should contain:")
    print("- At least 8 characters")
    print("- One uppercase letter")
    print("- One lowercase letter")
    print("- One number")