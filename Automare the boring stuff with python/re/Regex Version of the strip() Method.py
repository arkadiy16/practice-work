import re

# This is practice work from Automate the boring stuff with python.
# Regular expression.
# Regex Version of the strip() Method.
# Main task is to write function that uses regular expression and does the same thing as the strip() string method.


def re_strip(string, char=' '):
    # func take string and char that should be removed(if not given space by default)
    # and remove it from left and right
    patStrip = re.compile(rf'^{re.escape(char)}*|{re.escape(char)}*$')
    return patStrip.sub('', string)


print(re_strip('a sfasfasfagadgaaaaaaaaa', char='a'))