import random

boxes = '''  
   __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
'''
carrot_box = ['''
   ___VV____
  |   VV    |
  |   VV    |
  |___||____|     __________
 /    ||   /|   /         /|
''', '''
                  ___VV____
                 |   VV    |
                 |   VV    |
  __________     |___||____|     
 /         /|   /    ||   /|   
''', '''
   ___VV____      _________
  |   VV    |    |         |
  |   VV    |    |         |
  |___||____|    |_________|
 /    ||   /|   /         /|
''', '''
   _________      ___VV____
  |         |    |   VV    |
  |         |    |   VV    |
  |_________|    |___||____|
 /         /|   /    ||   /| 
''']


# print(carrot_box + boxes[60:].lstrip())

def show_boxes(pl1_box, pl2_box, ascii=None, carrot=0):
    if ascii is not None:
        print(carrot_box[ascii] + boxes[60:].lstrip() + ' ' * carrot * 15 +
              f' (carrot!)\n{pl1_box}    {pl2_box}')
    else:
        print(f'{boxes}{pl1_box}    {pl2_box}')


def main():
    pl1 = ['Bob', 'RED']  # input('Human player 1, enter your name: '), 'RED'
    pl2 = ['Alice', 'GOLD']  # input('Human player 2, enter your name: '), 'GOLD'
    pl1_box = ' ' * ((11 - len(pl1[0])) // 2) + pl1[0] + ' ' * ((12 - len(pl1[0])) // 2)
    pl2_box = ' ' * ((11 - len(pl2[0])) // 2) + pl2[0] + ' ' * ((12 - len(pl2[0])) // 2)
    print(f'Here are two boxes:')
    show_boxes(pl1_box, pl2_box)
    print(f'{pl1[0]}, you have a {pl1[1]} box in front of you.\n'
          f'{pl2[0]}, you have a {pl2[1]} box in front of you.')
    # input(f'When {pl2[0]} has closed their eyes, press Enter.')
    carrot_h = 'RED'  # random.choice('RED', 'GOLD)
    carrot = 0
    if carrot_h == 'GOLD':
        carrot = 1
    print(f'{pl1[0]} carrot is the inside of {carrot_h} box:')
    show_boxes(pl1_box, pl2_box, carrot, carrot)
    # input(f'When you will remember in which box is carrot. Press Enter. And let {pl2[0]} open eyes.')
    print('\n' * 10)
    show_boxes(pl2_box, pl1_box)
    input(f'When {pl2[0]} decide to swap boxes or not. Press Enter.')
    swap_box = input(f'Do {pl2[0]} want to swap?(If don\'t  press Enter.)')
    if swap_box:
        pl1[1], pl2[1] = pl2[1], pl1[1]
        carrot = not carrot
    show_boxes(pl1_box, pl2_box, carrot + 2, carrot)
    print(f'Carrot inside of {carrot_h} box.')
    if carrot_h in pl1:
        print(f'Congratulations!!! {pl1[0]} wins!')
    else:
        print(f'Congratulations!!! {pl2[0]} wins!')
    print('Thank you for playing!!!')


main()
