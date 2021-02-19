import re

while True:
    # asking password from the user
    password = input('Please enter the password: ')

    # defining the pattern and checking if at least 8 characters in the password.
    atleast_eight_pattern = r"[a-zA-Z0-9_%#@\.\+\$]{8,}"
    atleast_eight = re.search(atleast_eight_pattern, password)

    # defining the pattern and checking if there is a digit at the end of the password.
    end_with_digit_pattern = r"\d$"
    end_with_digit = re.search(end_with_digit_pattern, password)

    if atleast_eight and end_with_digit:
        # checking if the password is at least 8 characters and ends with a digit entering the password.
        print('Password entered successfully.')
        break
    elif atleast_eight and not end_with_digit:
        # asking the user to input password again in case of the password not ending with digits.
        print('The password must contain digit at the end.')
    elif not atleast_eight and end_with_digit:
        # asking the user to input password again in case of the password not being 8 characters.
        print('The password must contain at least 8 characters.')
    else:
        # asking the user to input password again in case of the password not being 8 characters and not ending with
        # digits.
        print('Please enter at least 8 characters and a digit at the end of the password.')
