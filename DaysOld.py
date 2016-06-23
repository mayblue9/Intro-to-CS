# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def isLeap(yr):
  if yr % 4 != 0:
    return False
  elif yr % 100 != 0:
    return True
  elif yr % 400 != 0:
    return False

def get_julian_date(year, month, day):
  daysOfMonths = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  total = 0
  while month != 1:
    month = month - 1
    total = total + daysOfMonths[month]
    if month == 2 and isLeap(year):
      total = total + 1
  while day != 1:
    day = day - 1
    total = total + 1
  return total

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
  total_days = 0
  first_date = get_julian_date(year1, month1, day1)
  second_date = get_julian_date(year2, month2, day2)
  while year1 != year2:
    if isLeap(year1):
      total_days = total_days + 1
    total_days = total_days + 365
    year1 = year1 + 1
  return total_days + second_date - first_date

    

# Test routine

def test():
  test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
  for (args, answer) in test_cases:
    result = daysBetweenDates(*args)
    if result != answer:
      print("Test with data:", args, "failed")
    else:
      print("Test case passed!")

test()
