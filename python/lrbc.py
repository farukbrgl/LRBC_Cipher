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
# Fig. 3 at the paper
# pt1 = plaintext[0:2] + plaintext[8:10]
# pt2 = plaintext[2:4] + plaintext[10:12]
# pt3 = plaintext[4:6] + plaintext[12:14]
# pt4 = plaintext[6:8] + plaintext[14:16]
pt1 = (str(random.randint(0, 8)))
pt2 = (str(random.randint(0, 8)))
pt3 = (str(random.randint(0, 8)))
pt4 = (str(random.randint(0, 8)))

# pt1_temp = [int(l) for l in pt1]
# pt1 = bin(int("".join(map(str, pt1_temp))))
# print((pt1))
# keys generated
# k1, k2, k3, k4 4 bit keys
# key_list 24 permutaiton of k1, k2, k3, k4
# every round uses key_list[i]
k1 = str(random.randint(0, 8))
k2 = str(random.randint(0, 8))
k3 = str(random.randint(0, 8))
k4 = str(random.randint(0, 8))
b = list(permutations(k1 + k2 + k3 + k4))
key_list = []
key_list_abcd = []
for k in range(24):
    key_list_abcd = []
    for i in range(4):
        key1 = (((int((b)[k][i]))))
        # print(key1)
        # print(type(key1))
        key_list_abcd.append(key1)
    key_list.append(key_list_abcd)
# print(key_list)
# print((((  (int(key_list[1][1]))  )   ^(int(key_list[2][2])))))
# print(((int(key_list[1][1]))))

# round function of lrbc

# print(bin(int(pt1)))
def lrbc_round(key_a, key_b, key_c, key_d, pt1, pt2, pt3, pt4):
    ic1 = 0xf - (int(pt1) ^ key_a)
    ic2 = int(pt2) ^ key_b
    ic3 = int(pt3) ^ key_c
    ic4 = 0xf - (int(pt4) ^ key_d)

    # sbox of F-function
    is1 = format(0xf - (ic1 ^ ic3), "04b")
    is2 = format((ic1 ^ 1), "04b")
    is3 = format(0xf - (ic2 ^ ic4), "04b")
    is4 = format(ic2 ^ 1, "04b")

    # pbox of F-function
    p1 = is1[0:1] + is2[3:4] + is1[1:2] + is2[2:3]
    p2 = is1[2:3] + is2[1:2] + is1[3:4] + is2[0:1]
    p3 = is3[0:1] + is4[3:4] + is3[1:2] + is4[2:3]
    p4 = is3[2:3] + is4[1:2] + is3[3:4] + is4[0:1]

    # lbox of F-function
    t1 = format((int(p1[0:1]) ^ int(p2[3:4])), "01b")
    print(t1)
    x1 = format(1 - (int(p1[0:1]) ^ 0), "01b")

    t2 = format(1 - (int(p1[1:2]) ^ int(p2[2:3])), "01b")
    x2 = format(int(p1[1:2]) ^ 1, "01b")

    t3 = format(int(p1[2:3]) ^ int(p2[1:2]), "01b")
    x3 = format(1 - (int(p1[2:3]) ^ 0), "01b")

    t4 = format(1 - (int(p1[3:4]) ^ int(p2[0:1])), "01b")
    x4 = format(int(p1[3:4]) ^ 1, "01b")

    t5 = format(int(p3[0:1]) ^ int(p4[3:4]), "01b")
    x5 = format(1 - (int(p2[0:1]) ^ 0), "01b")

    t6 = format(1 - (int(p3[1:2]) ^ int(p4[2:3])), "01b")
    x6 = format(int(p2[1:2]) ^ 1, "01b")

    t7 = format(int(p3[2:3]) ^ int(p4[1:2]), "01b")
    x7 = format(1 - (int(p2[2:3]) ^ 0), "01b")

    t8 = format(1 - (int(p3[3:4]) ^ int(p4[0:1])), "01b")
    x8 = format(int(p2[3:4]) ^ 1, "01b")

    l1 = t1 + x4 + t2 + x3 + t3 + x2 + t4 + x1
    l2 = t5 + x8 + t6 + x7 + t7 + x6 + t8 + x5
    # print (type(x3))
    # print(l1)
    # print(l2)
    pt1 = l1[4:8]
    pt2 = l2[4:8]
    pt3 = l1[0:4]
    pt4 = l2[0:4]
    print(pt1)
    return l1, l2, pt1, pt2, pt3, pt4


# lrbc_round(key_list[0][0], key_list[0][1], key_list[0][2], key_list[0][3], pt1, pt2, pt3, pt4)
pt_1 = ""
pt_2 = ""
pt_3 = ""
pt_4 = ""
for i in range(24):
    l1, l2, pt_1, pt_2, pt_3, pt_4 = lrbc_round(key_list[i][0], key_list[i][1], key_list[i][2], key_list[i][3], pt1, pt2, pt3, pt4)

ct = pt_1 + pt_2 + pt_3 + pt_4
print(ct)