# This Python file uses the following encoding: utf-8
'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''

import datetime as dt

def sunday_the_first(start_year, end_year):
	tally = sum(1
		for y in range(start_year + 1, end_year + 1)
		for m in range(1, 13)
		if dt.date(y, m, 1).weekday() == 6)
	return tally

if __name__ == "__main__":
  print(sunday_the_first(1900, 2000))

# prints: 171




