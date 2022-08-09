import random
import pyinputplus as pyip

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

def main():
    cut = 0.05
    print('''In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
''')
    player = 'Bob' # input('Input your name')
    money = 5000
    # Loop for game.
    while True:
        print(f'You have: ${money}')
        print(f'How much do you bet? (1-{money}, or QUIT)')
        bet = pyip.inputCustom(bet_validation)
        print('''The dealer swirls the cup and you hear the rattle of dice.
The dealer slams the cup on the floor, still covering the
dice and asks for your bet.''')
        guess = pyip.inputChoice(('cho', 'han'))
        s = [random.randint(1, 6) for _ in range(2)]
        print(f'{s[0]}    {s[1]}')
        if guess == sum(s) % 2:
            fee = bet * cut
            money += bet - fee
            print(f'Congratulations! You take{bet}!')
            print(f'The house collects a {fee} fee.')
        else:
            money -= bet
            print('Sorry you lose.')
main()