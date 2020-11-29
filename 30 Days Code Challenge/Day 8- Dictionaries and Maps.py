# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

n = int(input())
phoneBook = {}

for i in range(n):
    newNames = input().split(' ')
    phoneBook[newNames[0]] = newNames[1]

# Put all inputs on the same line
names = sys.stdin.readlines()

# Loop through the names:
for name in names:
    #
    name = name.strip()
    if name in phoneBook:
        print(name + '=' + phoneBook[name])
    else:
        print('Not found')
