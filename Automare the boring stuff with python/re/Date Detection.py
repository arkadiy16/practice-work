import re


# This is practice work from Automate the boring stuff with python
# Regular expression
# Date Detection
# Main task is to write a regular expression that can detect dates in the  DD/MM/YYYY format
# Days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999

def is_year_leap(year, flag=False):
    # function for checking if year is leap
    # func take 4 digits as year and return True if year is leap and False if not
    if not year % 4 and year % 100 or not year % 400:
        flag = True
    return flag


def main(l_date):
    # func take list of dates and print dates and validation of them
    for i in l_date:
        d, m, y = i.split('/')
        flag = 'invalid'
        if r_date.search(i):
            if d in max_days:
                if m in max_days[d]:
                    flag = 'valid'
            elif d == '29' and m == '02':
                if is_year_leap(int(y)):
                    flag = 'valid'
            else:
                flag = 'valid'
        print(f'{d}/{m}/{y} is {flag} date')


r_date = re.compile(r'''
                    ([0-2][0-9]|3[0-1])/       # re for day 01-31
                    (0[0-9]|1[0-3])/               # re for day 01-12
                    [1-2][0-9]{3}                  # re for year 1000-2999
                    ''',
                    re.X)

max_days = {'31': ['01', '03', '05', '07', '08', '10', '12'],  # dictionary for max days in each months in non leap yaer
            '30': ['04', '06', '09', '11'], '28': ['02']}      # key is max day,  value - list of number of month

dat = ['11/01/2000', '31/02/2020', '31/04/2020', '11/11/2000']  # list for example

main(dat)
