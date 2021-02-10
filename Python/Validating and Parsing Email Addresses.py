import re
import email.utils

n = '2'
nn = 'this <is_som@radom.stuff>'
nnn = 'this <is_it@valid.com>'

for _ in range(1):
    emails = email.utils.parseaddr(nnn)
    pattern = re.compile(r'^[a-zA-Z][\w\-.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$')
    if re.match(pattern, emails[1]):
        print(email.utils.formataddr(emails))
    else:
        pass
