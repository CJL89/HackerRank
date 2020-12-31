import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()
        n, k = map(int, nk)
        print(k-1 if ((k-1) | k) <= n else k-2)
