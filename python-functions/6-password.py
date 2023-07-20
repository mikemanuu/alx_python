#!/usr/bin/python3
def validate_password(password):
    if len(password) < 8:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    for char in password:
        if char.isspace():
            return False
        elif char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
    
    if has_upper and has_lower and has_digit:
        return True
    else:
        return False
