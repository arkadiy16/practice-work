from fileinput import filename


bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................
"""


# function take a string and replaced not empty characters by characters in string.
def bitmap_replacer(message, btmap):
    btmap_l = []
    # Loop over each line in the bitmap:
    for _, string in enumerate(btmap.split('\n')):
        for i, elem in enumerate(string):
            if elem != ' ':
                string = string.replace(elem, message[i % len(message)], 1)
        btmap_l.append(string)
    return btmap_l


def main():
    print('Enter the message to display with the bitmap.')
    # message = input('> ')
    message = 'Hello!'
    print(*bitmap_replacer(message, bitmap), sep='\n')
