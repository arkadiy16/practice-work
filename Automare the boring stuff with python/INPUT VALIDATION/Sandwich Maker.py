import pyinputplus as pyip


# This is practice work from Automate the boring stuf with python
# Input validation
# Sandwich Maker
# Main task is to write a program that asks users for their sandwich preferences.
# The program should use PyInputPlus functions such as: inputMenu(), inputYesNo(), inputInt()



def main():
    total = 0
    print('What type of bread you want?')
    bread, p_bread =  pyip.inputMenu(['wheat $0.4', 'black $0.45', 'sourdough $0.5'], numbered=True).split('$')
    total += float(p_bread)
    print('What type of protein you want?')
    protein, p_protein =  pyip.inputMenu(['chicken $1.75', 'turkey $2', 'ham $1.5', 'tofu $1'], numbered=True).split('$')
    total += float(p_protein)
    print('Want some cheese?')
    if pyip.inputYesNo() == 'yes':
        print('What type of?')
        chees, p_chees =  pyip.inputMenu(['chedder $1', 'Swiss $ 1.2', 'mozzarella $1.3'], numbered=True).split('$')
        total += float(p_chees)
    else:
        chees = 'no'
    print('Something extra?')
    if pyip.inputYesNo() == 'yes':
        print('We have:')
        extra, p_extra =  pyip.inputMenu(['mayo $0.1', 'mustard $0.15', 'lettuce $0.3', 'tomato $0.2'], numbered=True).split('$')
        total += float(p_extra)
    else:
        extra = 'no'
    print(f'You have {bread.strip()} bread, with {protein.strip()}, {chees.strip()} cheese, extra {extra.strip()}')
    number = pyip.inputInt('How much sandwiches you want?\n', min=1)
    total *= number
    print(f'You have to pay {round(total, 2)}$')

main()
