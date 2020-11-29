import math
import os
import random
import re
import sys



# if __name__ == '__main__':
    # N = int(input())
N = 0

if N % 2 != 0:
    print('Not Weird')
elif N % 2 == 0 and N in range(2, 6):
    print('Not Weird')
elif N % 2 == 0 and N in range(6, 21):
    print('Weird')
else:
    print("Not Weird")
