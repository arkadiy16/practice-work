# Program simulate work of caesar cipher.
# It encrypts letters by shifting them over
# by a certain number of places in the alphabet.
# Same to decrypt but shift letters in opposite direction.
# Program have 2 main functions for encrypt and decrypt given message.

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
    choice = pyip.inputStr('Do you want to (e)ncrypt or (d)ecrypt?\n',
                           allowRegexes=['e', 'encrypt', 'd', 'decrypt'],
                           blockRegexes=[r'.*'])
    key = pyip.inputNum('What is the key?\n', min=0, max=len(alphabet))
    choice_c = 'en'
    if choice[0] == 'd':
        choice_c = 'de'
        key = -key
    message = pyip.inputStr(f'Enter message to {choice_c}crypt.\n').upper()
    changed_message = crypter(key, message)
    pyperclip.copy(changed_message)
    print(changed_message, f'\nFull {choice_c}crypted text copied to clipboard.')

main()
