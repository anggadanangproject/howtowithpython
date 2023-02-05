def isLeapYear(year):
    if year > 1582:
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    return year % 4 == 0

def daysInMonth(year, month):
    if(year == 1582 and month == 10):
        return 21
    elif month == 2: 
        return 28 + isLeapYear(year) 
        return(31 - (((month - 1) % 7) % 2))

print(daysInMonth(2023, 2)

#output
#28
