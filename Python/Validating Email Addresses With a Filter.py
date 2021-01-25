import re

def fun(s):
    # return True if s is a valid email, else return False
    if re.match('(^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.([a-zA-Z]{0,3})$)', s):
        return True
    else:
        return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

# Examples
dheeraj-234@gmail.com
itsallcrap
harsh_1234@rediff.in
kunal_shin@iop.az
matt23@@india.in
fjladfk_iasdfad234@sdlkjf23335.in
ha@git@int.cz
prashant24_@gmail.com
its@gmail.com1
mike13445@yahoomail9.server
rase23@ha_ch.com
daniyal@gmail.coma
thatisit@thatisit
