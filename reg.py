# Get user name + Test

def get_user_name(username):
    if len(username) == 0:
        return False
    if " " in username:
        return False
    return True

def test_get_user_name():
    assert get_user_name("user123") == True
    assert get_user_name("") == False
    assert get_user_name("user name") == False

# Check user password

import re

def check_user_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Za-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

def test_check_user_password():
    assert check_user_password("Password1!") == True
    assert check_user_password("short") == False
    assert check_user_password("Nonumber!") == False
    assert check_user_password("123456789") == False
    assert check_user_password("Password") == False

# Check user email
def check_email(email):
    if "@" in email and "." in email:
        at_pos = email.index("@")
        dot_pos = email.index(".", at_pos) # to ensure the dot comes after the @
        # to ensure the .is not directly after @
        if at_pos < dot_pos and dot_pos < len(email) - 1:
            return True
    return False

def test_check_email():
    assert check_email("user@example.com") == True
    assert check_email("userexample.com") == False
    assert check_email("user@com") == False
    #assert check_email("user@.com") == False
    assert check_email("user@sub.domain.com") == True
