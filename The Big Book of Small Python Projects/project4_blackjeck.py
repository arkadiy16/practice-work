import random
import pyinputplus as pyip


# cards: [['p'/'a'][suit, rank, face], ...]
# Hand painting with ASCII.
def card_print(cards):
    # Printing player's points.
    if cards[0] == 'p':
        player = 'Player'
    else:
        player = 'AI'
    cards = cards[1:]
    points = point_count(cards)
    print(f'{player}\'s hand: {points}')
    # Printing cards with ASCII.
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
    return points


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
def point_count(hand):
    points = 0
    ace_count = 0
    for _, rank, face in hand:
        if face == 'down':
            return '???'
        point = ranks.index(rank) + 1
        if point > 10:
            point = 10
        elif point == 1:
            point = 11
            ace_count += 1
        points += point
    if points > 21:
        while ace_count and points > 21:
            points -= 10
            ace_count -= 1
    return points


# AI.
def ai(a_hand, deck):
    while point_count(a_hand[1:]) < 17:
        print(1)
        a_hand.append(deck.pop())
    return a_hand, deck


# Input validation for bet.
def bet_validation(num, money=5000):
    if num == 'QUIT':
        return False
    try:
        bet = int(num)
    except:
        raise Exception('Bet should be integer digit.')
    if bet > money:
        raise Exception(f'Bet can\'t be more than you have.(<{money})')
    elif bet < 1:
        raise Exception('Bet should be at least 1.')
    print(f'Bet: {bet}', end='')
    return bet


# Player turn.
def p_turn(p_hand, deck):
    while True and point_count(p_hand[1:]) < 21:
        choice =  pyip.inputChoice(['h', 's', 'd'])
        if choice == 's':
            break
        elif choice == 'h':
            hit_card = deck.pop()
            print(f'You drew a {hit_card[1]} of {hit_card[0]}.')
            p_hand.append(hit_card)
        else:
            p_hand.append(deck.pop())
            break
    return p_hand, deck


# BJ game.
def bj():
    money = 5000
    deck = deck_create()
    while True:
        while True:
            print(f'You have: ${money}')
            print(f'How much do you bet? (1-{money}, or QUIT)')
            bet =  pyip.inputCustom(bet_validation)
            if not bet:
                break
            p_hand = ['p', deck.pop(), deck.pop()]
            p_points = card_print(p_hand)
            face_down_card = deck.pop()
            a_hand = ['a', face_down_card, deck.pop()]
            a_points = point_count(a_hand[1:])
            # Checking if any hand have bj.
            if p_points == 21 and a_points == 21:
                print(f'Draw!')
                break
            elif p_points == 21:
                print(f'Congratulations, you got Blackjeck!!!\nYou won: ${bet * 3 / 2}.')
                money += bet * 3 / 2
                break
            elif a_points == 21:
                print(f'Dealer got blackjeck!!!')
                card_print(a_hand)
                break
            face_down_card[2] = 'down'
            print()
            card_print(a_hand)
            face_down_card[2] = 'up'
            print('(H)it, (S)tand, (D)ouble down')
            p_hand, deck = p_turn(p_hand, deck)
            if point_count(p_hand[1:]) > 21:
                money -= bet
                card_print(p_hand)
                card_print(a_hand)
                print('You ower!')
                break
            a_hand, deck = ai(a_hand, deck)
            p_points = card_print(p_hand)
            a_points = card_print(a_hand)
            if p_points > a_points or a_points > 21:
                print('Congratulations! You won: ${bet}.')
                money += bet
            else:
                print('Dealer won.')
                money -= bet

        choise = pyip.inputYesNo('Do you want to play again? (y/n)')
        if choise[0] == 'y':
            if money > 1:
                choise = pyip.inputYesNo('Do you want to continue with same money you have? (y/n)')
            if choise[0] == 'n':
                money = 5000
                if len(deck) < 50:
                    deck = deck_create()
            if len(deck) < 50:
                deck = deck_create()

            continue
        else:
            break


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
    bj()
    print('Thank you for play.')


main()
