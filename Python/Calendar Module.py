import calendar

month, day, year = map(int, input().split(' '))
day = calendar.weekday(year, month, day)
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(weekdays[day].upper())
