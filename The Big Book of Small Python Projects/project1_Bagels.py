import random

print('''
Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
''')


def checking(guess, num):
    if len(guess) != 3:
        print('Number is 3-digit long.')
        return False
    clue = []
    for i, dig in enumerate(guess):
        if dig in num:
            if num[i] == dig:
                clue.append('Fermi')
            else:
                clue.append('Pico')
    if not clue:
        clue.append('Bagels')
    return clue


def main():
    print('''
    Bagels, a deductive logic game.
    By Al Sweigart al@inventwithpython.com
    I am thinking of a 3-digit number. Try to guess what it is.
    Here are some clues:
    When I say:    That means:
      Pico         One digit is correct but in the wrong position.
      Fermi        One digit is correct and in the right position.
      Bagels       No digit is correct.
    ''')
    while True:
        num = str(random.randint(100, 999))
        print('I have thought up a number.')
        print('You have 10 guesses to get it.')
        for i in range(1, 11):
            print(f'Guess #{i}')
            guess = input()
            if guess == num:
                print('You got it!')
                break
            clue = checking(guess, num)
            if clue:
                print(*clue, sep=' ')
        if input('Do you want to play again?(y/n)') != 'y':
            break



main()

