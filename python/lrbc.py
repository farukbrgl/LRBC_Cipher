#!/usr/bin/env python
# coding: utf-8

"""
LRBC Hafif Blok Şifreleyicisinin Python ile Gerçeklenmesi
Orijinal makaleye
https://link.springer.com/article/10.1007%2Fs12652-020-01694-9
adresinden ulaşabilirsiniz.
"""


import random
plaintext = []
for i in range(0, 16):
    n = random.randint(0, 1)
    plaintext.append(n)

print(plaintext)
pt1 = plaintext[0:2] + plaintext[8:10]
pt2 = plaintext[2:4] + plaintext[10:12]
pt3 = plaintext[4:6] + plaintext[12:14]
pt4 = plaintext[6:8] + plaintext[14:16]
