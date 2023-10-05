#!/usr/bin/env python

ciphertext = open('ciphertext', 'r').read()

cipher = ciphertext.split('{')[1].replace('}', '') # split mane bad dowa

for i in range(26):
    plain = ''

    for char in cipher:
        plain += chr(((ord(char) - ord('a')) + i) % 26 + ord('a'))
    print('{:<3}picoCTF{{{}}}'.format(i, plain))