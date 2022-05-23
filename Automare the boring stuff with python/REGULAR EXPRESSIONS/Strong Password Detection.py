import re


# This is practice work from Automate the boring stuff with python.
# Regular expression.
# Strong Password Detection.
# Main task is to write function that use regular expression to check that a password is strong.
# A strong password need to be at least eight characters long,
# contains both uppercase and lowercase characters, and has at least one digit.


def strong_password_detection(password):
    # func take a password as string and return strong string if it is strong and weak else
    flag = 'weak'
    patRegex = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[\w\d]{8,}')
    if patRegex.search(password):
        flag = 'strong'
    return flag


def main(l_password):
    # take password and print status
    for password in l_password:
        print(f'{password} is {strong_password_detection(password)} password')


l_password = [
    'ag5315ASFhaksmg', 's', 'S', '2', 'ASFGHADHD15315124g', 'ASDFGHJK',
    '123456789', 'asd123ASD', 'as123ASD', '123123ASD', 'd123ASD', 'aA1'
]

main(l_password)
