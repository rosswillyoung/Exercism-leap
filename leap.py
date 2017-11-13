def is_leap_year(year):
    year = int(year)
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        else:
            return True
    else:
        return False

print(is_leap_year(input('Enter a year')))
