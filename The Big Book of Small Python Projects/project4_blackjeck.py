import random
import pyinputplus as pyip


# cards: [[suit, rank, face], ...]
# Card painting with ASCII.
def card_print(cards):
    if cards[0] == 'p':
        player = 'Player'
    else:
        player = 'AI'
    print(f'{player}\'s hand:')
    cards = cards[1:]
    for i in range(4):
        if i == 0:
            print(' ___  ' * len(cards))
        elif i == 1:
            for _, rank, face in cards:
                if face == 'down':
                    rank = '##'
                elif len(rank) == 1:
                    rank = rank + ' '
                print(f'|{rank} |', end=' ')
            print()
        elif i == 2:
            for suit, _, face in cards:
                if face == 'down':
                    print(f'|###|', end=' ')
                    continue
                print(f'| {suit} |', end=' ')
            print()
        elif i == 3:
            for _, rank, face in cards:
                if face == 'down':
                    rank = '##'
                elif len(rank) == 1:
                    rank = '_' + rank
                print(f'|_{rank}|', end=' ')
            print()
            print()


suits = '♥♠♦♣'
ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')


# Creating deck.
def deck_create(decks_amount=4):
    deck = []
    for _ in range(decks_amount):
        for suit in suits:
            for rank in ranks:
                deck.append([suit, rank, 'up'])
    random.shuffle(deck)
    return deck


# Counting points in hand.
def p_count(hand):
    pass


# Player's hand.
def hand():
    hand = []

    pass


# AI.
def ai():
    pass


# Input validation for bet.
def bet_validation(num, money=5000):
    if num == 'QUIT':
        return False
    try:
        bet = int(num)
    except:
        raise Exception('Bet should be digit.')
    if bet > money:
        raise Exception(f'Bet can\'t be more than you have.(<{money})')
    elif bet < 1:
        raise Exception('Bet should be at least 1.')
    print(f'Bet: {bet}', end='')
    return bet


def main():
    print(''' Rules:
      Try to get as close to 21 without going over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 through 10 are worth their face value.
      (H)it to take another card.
      (S)tand to stop taking cards.
      On your first play, you can (D)ouble down to increase your bet
      but must hit exactly one more time before standing.
      In case of a tie, the bet is returned to the player.
      The dealer stops hitting at 17.
      ''')
    money = 5000
    while True:
        print(f'Money: {money}')
        print(f'How much do you bet? (1-{money}, or QUIT)')
        bet = pyip.inputCustom(bet_validation)
        if not bet:
            print('Thank you for play.')
            break

        deck = deck_create()
        p_hand = ['p', deck.pop(), deck.pop()]
        card_print(p_hand)
        face_down_card = deck.pop()
        face_down_card[2] = 'down'
        a_hand = ['a', face_down_card, deck.pop()]
        card_print(a_hand)
