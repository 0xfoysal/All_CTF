#!/usr/bin/env python

cipher = 'cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}'

plain = ''

for char in cipher:
    if 'a' <= char <= 'z':
        plain += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
    elif 'A' <= char <= 'Z':
        plain += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
    else:
        plain = plain + char

print('{}'.format(plain))