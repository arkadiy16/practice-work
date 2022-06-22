# This is practice work from Automate the boring stuff with python.
# Reading and Writing Files.
# Regex Search.
# Main task is to write a program that read all .txt files in a folder
# and searches any line that matches user's reg exp.
# In example reg exp for fincing all sites in http:/.... format.

import re
from pathlib import Path


def main(folder_path, reg_exp):
    reg = re.compile(reg_exp)
    path = Path(folder_path)
    # Find all .txt files in a folder.
    for txt_path in path.glob('*.txt'):
        # Open .txt file and search for matches.
        with open(txt_path, 'r') as text:
            matches = {}
            # Check all lines.
            for line in text.readlines():
                r = reg.search(line)
                if r:
                    matches[line] = r.group()
            if matches:
                print(f'You have matches in {txt_path.stem}:')
                for l in matches:
                    # Print matches in match - line format.
                    print(f'{matches[l]} - {l}', end='')
                print()
        

                          
main('C:\\Users\\1\\Desktop\\New', r'http:[a-zA-Z0-9/._]*')
                                           
                                           
