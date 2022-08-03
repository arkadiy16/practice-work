

# cards: [[suit, rank, face], ...]
# Card painting with ASCII.
def card_print(cards):
    for i in range(4):
        if i == 0:
            print(' ___  '*len(cards))
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


# Creating card.

# Creating deck.

card_print([['f', '10', 'down'], ['a', '2', 'up'], ['d', '5', 'up'], ['h', 'K', 'up']])
card_print([['f', '10', 'down'], ['a', '2', 'up'], ['d', '5', 'up'], ['h', 'K', 'up']])
