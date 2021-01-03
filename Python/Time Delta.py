from datetime import datetime

# t1 = 'Sun 10 May 2015 13:54:36 -0700'
# t2 = 'Sun 10 May 2015 13:54:36 -0000'

t1 = 'Sat 02 May 2015 19:54:36 +0530'
t2 = 'Fri 01 May 2015 13:54:36 -0000'

def time_delta(t1, t2):
    date_format = '%a %d %b %Y %H:%M:%S %z'
    diff = abs(datetime.strptime(t1, date_format) - datetime.strptime(t2, date_format)).total_seconds()
    print(round(diff))

time_delta(t1, t2)
