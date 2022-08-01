import random, datetime
import logging, time

logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s -  %(message)s')


# Function for getting random month and day.
def rnd_bd():
    startOfYear = datetime.date(2001, 1, 1)
    randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
    birthday = startOfYear + randomNumberOfDays
    return birthday.strftime('%b %d').split()


# birthdays data.
def data_bd(group, first=False):
    # For more beautiful output in first simulation.
    bd_list = []
    if first:
        bd_group = {'Jan': [], 'Feb': [], 'Mar': [],
                    'Apr': [], 'May': [], 'Jun': [],
                    'Jul': [], 'Aug': [], 'Sep': [],
                    'Oct': [], 'Nov': [], 'Dec': []
                    }

        for _ in range(group):
            m, d = rnd_bd()
            bd_group[m].append(d)
        for m, days in bd_group.items():
            if days:
                for d in days:
                    bd_list.append(f'{m} {d}')
    else:
        for _ in range(group):
            m, d = rnd_bd()
            bd_list.append(f'{m} {d}')
    return bd_list


# same birthday checker.
def checker(bd_group, first=False):
    if len(bd_group) == len(set(bd_group)):
        return False,
    elif first:
        while bd_group:
            d = bd_group.pop()
            logging.info(d)
            if d in bd_group:
                return (True, d)
    else:
        return (True,)


# first simulation function.
def f_sim(bd_amount):
    data = data_bd(bd_amount, first=True)

    for i, date in enumerate(data):
        if i + 1 == len(data):
            print(date + '.')
        else:
            print(date, end=', ')
        if not (i + 1) % 10:
            print()
    bool_date = checker(data, first=True)
    if bool_date[0]:
        h = f'multiple people have a birthday on {bool_date[1]}'
    else:
        h = 'nobody have a birthday with another one in the same day.'

    print(f'In this simulation, {h}')


# LLW function.
def LLW(bd_amount):
    print('Let\'s run another 100,000 simulations.')
    print('1 simulations run.')
    total = 0
    for i in range(1, 100001):
        if '0000' in str(i):
            print(f'{i} simulations run.')

        data = data_bd(bd_amount)
        if checker(data)[0]:
            total += 1
    return total


# main function.
def main(bd_amount):
    # change to True if want to use with users.
    while False:
        try:
            bd_amount = 23  # int(input('How many birthdays should be generated?(Max 100, Min 2)'))
        except:
            print('Please use numeric digits.')
            continue
        if bd_amount < 100 and bd_amount > 2:
            break
        print('I need at lest 2 birthdays and max 100.')

    print(f'Here are {bd_amount} birthdays:')
    f_sim(bd_amount)
    print(f'Generating {bd_amount} random birthdays 100,000 times...')
    # input('Press Enter to begin...')
    total = LLW(bd_amount)
    percentages = total / 1000
    print(f'Out of 100,000 simulations of {bd_amount} people, there was a matching ')
    print(f'birthday in that group {total} times. This means that {bd_amount} people ')
    print(f'have a {percentages} % chance of having a matching birthday in their group.')
    print('That\'s probably more than you would think!')
    return bd_amount, percentages, total


start = time.time()
with open('birthday_paradox.txt', 'w') as file:
    for i in [5, 10, 20, 23, 30, 40, 50, 60, 70, 75, 100]:
        bd, perc, t = main(i)
        file.write(f'Out of 100,000 simulations of {bd} people, there was a matching\n')
        file.write(f'birthday in that group {t} times. This means that {bd} people\n')
        file.write(f'have a {perc} % chance of having a matching birthday in their group.\n')
        file.write('\n')
end = time.time()
print(end - start)
