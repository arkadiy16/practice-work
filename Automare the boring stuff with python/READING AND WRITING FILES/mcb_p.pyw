# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb_p.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb_p.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb_p.pyw list - Loads all keywords to clipboard.
#        py.exe mcb_p.pyw delete <keyword> - Delete keyword from the shelve.

import shelve, pyperclip, sys


with shelve.open('mcb_p') as mcbShelf:
    if len(sys.argv) == 3:
        #Save clipboard content.
        if sys.argv[1].lower() == 'save'and sys.argv[2].lower() != 'all':
            mcbShelf[sys.argv[2]] = pyperclip.paste()
        #Delete clipboard content.
        elif sys.argv[1].lower() == 'delete':
            #Delete all keys.
            if sys.argv[2].lower() == 'all':
                mcbShelf.clear()
            elif sys.argv[2].lower() in list(mcbShelf.keys()):
                del mcbShelf[sys.argv[2]]
    elif len(sys.argv) == 2:
        # List keywords and load content.
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcbShelf.keys())))
        elif sys.argv[1] in mcbShelf:
            pyperclip.copy(mcbShelf[sys.argv[1]])

