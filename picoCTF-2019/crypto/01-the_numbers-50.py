#!/usr/bin/env python

numbers = '16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }'

space = ''

for number in numbers.split():
    try:
        n = int(number)
        space = space + chr(ord('a') + n - 1)
    except:
        space = space + number

print('{}'.format(space.upper())) 