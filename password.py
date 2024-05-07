import re
# password validation function
def check_password_strength(password):
    #min length
    if len(password) < 8:
        return "Password must be at least eight characters long"
    # capital letters 
    elif not re.search("[A-Z]",password):
        return "Password must have at least one uppercase letter"
    # numbers
    elif not re.search("[0-9]",password):
        return "Password must include a number"
    elif not re.search("[@#_*]",password):
        return "Password must have at least one special character"
    else:
        common_patterns = [
            r'(?i)1234567890',
            r'(?i)p@ssw0rd',
            r'(?i)Admin1234',
        ]
        return "Password Correct"
password = input("Enter Your Password: ")
print(check_password_strength(password))