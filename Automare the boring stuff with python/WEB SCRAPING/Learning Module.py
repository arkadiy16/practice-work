# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip


if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)


import bs4
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('#author')
type(elems) # elems is a list of Tag objects.
# <class 'list'>
len(elems)
# 1
type(elems[0])
# <class 'bs4.element.Tag'>
str(elems[0]) # The Tag object as a string.
# '<span id="author">Al Sweigart</span>'
elems[0].getText()
# 'Al Sweigart'
elems[0].attrs
# {'id': 'author'}
