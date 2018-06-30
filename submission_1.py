"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if month <= 11:
        date1 = datetime.date(year, month, 1)
        date2 = datetime.date(year, (month + 1), 1)
        delta = date2 - date1
        return delta.days
    else:
        return 31    
    
def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if (year >= datetime.MINYEAR and year <= datetime.MAXYEAR) is True:
        if (month >= 1 and month <= 12) is True:
            if (day >= 1 and day <= days_in_month(year, month)) is True:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    if (is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2)) is False:
        return 0
    else:
        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)
        
        if date2 <= date1:
            return 0
        else:
            delta = date2 - date1
            return delta.days

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    #date_of_birth = datetime.date(year, month, day)
    
    if is_valid_date(year, month, day) is False:
        return 0
    if datetime.date(year, month, day) >= datetime.date.today():
        return 0
    
    return days_between(year, month, day, 2018, 6, 30)

