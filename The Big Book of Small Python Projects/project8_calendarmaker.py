import datetime
import calendar


def calend(year, month):
    # Create datetime object for turn month number in name.
    date = datetime.datetime(year, month, 1)
    l = '+----------+----------+----------+----------+----' \
        '------+----------+----------+\n'
    cal = f'                                  {date:%B} {year}\n' \
          '...Sunday.....Monday....Tuesday...Wednesday...' \
          'Thursday....Friday....Saturday..\n' + l
    # Create Calendar object in which first day in week will be in sunday.
    c = calendar.Calendar(firstweekday=6)
    # List with dates, first date is monday before the start of the month if 1st <month> is not monday.
    dates = list(c.itermonthdates(year, month))
    # Leave only days in string format, if <day> < 10 add <space> before it.
    dates = list(map(lambda x: str(x.day).rjust(2), dates))
    # Loop for every week.
    for row in range(len(dates) // 7):
        sat = 7 * (row + 1)
        # First row.
        cal += '|{}        |{}        |{}        |{}        |{}        |{}        |{}        |\n' \
            .format(*dates[sat - 7:sat])
        # Second-fourth row.
        # First elem is <|> after <10 spaces|> which is repeated 7 times
        # in the end of line add <\n> and repeated all line 3 times
        # then add <l>.
        cal += ('|' + ('{}|'.format(' ' * 10) * 7) + '\n') * 3 + l
    return cal


def main():
    year = 2029  # int(input('Enter the year for the calendar:\n> '))
    month = 12  # int(input('Enter the month for the calendar, 1-12:\n> '))
    cal = calend(year, month)
    print(cal)

    with open(f'calendar_{year}_{month}.txt', 'w') as file:
        file.write(cal)
        print(f'Saved to calendar_{year}_{month}.txt')


main()
