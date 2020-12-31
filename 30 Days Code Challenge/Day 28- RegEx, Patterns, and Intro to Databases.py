import math
import os
import random
import re
import sys

n = 'riya riya@gmail.com'

N = 1
names = []
for N_itr in range(N):
    firstNameEmailID = n.split()

    firstName = firstNameEmailID[0]

    emailID = firstNameEmailID[1]
    
    if re.findall('[a-z]+@gmail.com', emailID):
        names.append(firstName)

    print(*sorted(names), sep='\n')
