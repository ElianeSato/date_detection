#! home/Python/Automate_Python_book/regex_date_detection.py
# regex_date_detection.py: This program validates dates in the format DD/MM/YYYY.

import re

def isValid(date):
    if check_format(date) == None:
        print("Data inválida.")
    else:
        # day, month and year validation
        day = int(date[0:2])
        month = int(date[3:5])
        year = int(date[6:10])
        monthsEnds30 = [4, 6, 9, 11]
        # monthsEnds31 = [1, 3, 5, 7, 8, 10, 12]
        if year < 1000 or year > 2999 or day > 31 or month > 12:
            print("Data inválida.")
        elif month != 2 and (day > 1 or day > 30):
            if month in monthsEnds30:
                print("Data inválida.")
            else:
                print("Data válida.")
        elif month == 2: # February
            if day > 29:
                print("Data inválida.")
            elif day > 0 or day > 28:
                if year % 4 != 0:
                    print("Data inválida.")
                elif year % 100 == 0 and year % 400 != 0:
                    print("Data inválida.")
                else:
                    print("Data válida.")


def check_format(date): #general format
    date_format = re.compile(r'^([0-3][0-9])/([0-1][0-9])/([1-2][0-9][0-9][0-9])?')
    try:
        mo = date_format.search(date).group()
        return "ok"
    except:
        return None


date = input('Digite: ')
isValid(date)
