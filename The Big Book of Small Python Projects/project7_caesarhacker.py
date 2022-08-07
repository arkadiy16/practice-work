# Program simulate work of caesar cipher hacker.
# Program decrypt message by shifting letters over
# all possible keys.


import string, pyperclip
import pyinputplus as pyip

alphabet = string.ascii_uppercase * 2


# Function for decrypt or encrypt.
def crypter(key, message):
    changed_message = ''
    for i, elem in enumerate(message):
        if elem not in alphabet:
            changed_message = changed_message + elem
            continue
        changed_message = changed_message + alphabet[alphabet.index(elem) + key]
    return changed_message


def main():
    message = pyip.inputStr('Enter the encrypted Caesar message to hack.\n').upper()
    for key in range(len(alphabet) // 2):
        changed_message = crypter(key, message)
        print(f'Key #{key}: {changed_message}')


main()
