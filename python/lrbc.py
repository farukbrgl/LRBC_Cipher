#!/usr/bin/env python
# coding: utf-8

"""
LRBC Hafif Blok Şifreleyicisinin Python ile Gerçeklenmesi
Orijinal makaleye
https://link.springer.com/article/10.1007%2Fs12652-020-01694-9
adresinden ulaşabilirsiniz.
"""

# random for generating plaintext and keys for starting
# permutations for generating all keys
import random
from itertools import permutations
import numpy

# random 16-bit plaintext created
plaintext = []
for i in range(0, 16):
    n = random.randint(0, 1)
    plaintext.append(n)

# print(plaintext)

# plaintext divided into 4 pieces pt1, pt2, pt3, p4
# Fig. 3 at the document
pt1 = plaintext[0:2] + plaintext[8:10]
pt2 = plaintext[2:4] + plaintext[10:12]
pt3 = plaintext[4:6] + plaintext[12:14]
pt4 = plaintext[6:8] + plaintext[14:16]


# keys generated
# k1, k2, k3, k4 4 bit keys
# key_list 24 permutaiton of k1, k2, k3, k4
# every round uses key_list[i]
k1 = str(random.randint(0,8))
k2 = str(random.randint(0,8))
k3 = str(random.randint(0,8))
k4 = str(random.randint(0,8))
b= list(permutations(k1+k2+k3+k4))
key_list = []
key_list_abcd = []
for k in range (24):
    key_list_abcd = []
    for i in range (4):
        key1 = format(int((b)[k][i]),"04b")
        key_list_abcd.append(key1)
    key_list.append(key_list_abcd)
print(key_list)

# def lrbc_round():
    