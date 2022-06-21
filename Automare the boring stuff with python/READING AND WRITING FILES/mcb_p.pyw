# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb_p.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb_p.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb_p.pyw list - Loads all keywords to clipboard.
#        py.exe mcb_p.pyw del <keyword> - Delete keyword from the shelve.
#        py.exe mcb_p.pyw delete - Delete all keywords from the shelve.

import shelve, pyperclip, sys


with shelve.open('mcb_p') as mcbShelf:
    #Save clipboard content.
    if len(sys.argv) == 3 
        if sys.argv[1].lower() == 'save':
            mcbShelf[sys.argv[2]] = pyperclip.paste()
        elif sys.argv[1].lower() == 'del':
            mcbShelf.pop(argv[1], 'None')
    elif len(sys.argv) == 2:
        # List keywords and load content.
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcbShelf.keys())))
        elif sys.argv[1] in mcbShelf:
            pyperclip.copy(mcbShelf[sys.argv[1]])
        elif sys.argv[1].lower() == 'delete':
            mcbShelf.clear()

