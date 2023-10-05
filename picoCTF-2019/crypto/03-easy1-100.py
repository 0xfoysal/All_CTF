#!/usr/bin/env python

message = 'UFJKXQZQUNB'
key = 'SOLVECRYPTO'

s = ''

for m,k in zip(message, key):
    s += chr((ord(m) - ord(k) + 26) % 26 + ord('A'))


print('picoCTF{{{}}}'.format(s.upper()))