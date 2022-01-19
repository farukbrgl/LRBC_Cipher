#!/usr/bin/env python
# coding: utf-8

"""
LRBC Hafif Blok Şifreleyicisinin Python ile Gerçeklenmesi
Orijinal makaleye
https://link.springer.com/article/10.1007%2Fs12652-020-01694-9
adresinden ulaşabilirsiniz.
"""

from itertools import permutations
from random import randint


def lrbc(plaintext, key_list):

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
        pt1 = l1[4:8]
        pt2 = l2[4:8]
        pt3 = l1[0:4]
        pt4 = l2[0:4]

        return pt1, pt2, pt3, pt4

    pt_1 = ""
    pt_2 = ""
    pt_3 = ""
    pt_4 = ""
    for i in range(24):
        pt_1, pt_2, pt_3, pt_4 = lrbc_round(
            key_list[i][0], key_list[i][1], key_list[i][2], key_list[i][3], pt1, pt2, pt3, pt4)

    ct = pt_1 + pt_2 + pt_3 + pt_4
    print(ct)
    return ct


# random for generating plaintext and keys for starting
# permutations for generating all key permutations
# random 16-bit plaintext created
plaintext = []
for i in range(0, 16):
    n = randint(0, 1)
    plaintext.append(n)

print(plaintext)

# plaintext divided into 4 pieces pt1, pt2, pt3, p4
# Fig. 3 at the paper
pt1 = plaintext[0:2] + plaintext[8:10]
pt2 = plaintext[2:4] + plaintext[10:12]
pt3 = plaintext[4:6] + plaintext[12:14]
pt4 = plaintext[6:8] + plaintext[14:16]
pt1 = int("".join(str(i) for i in pt1), 2)
pt2 = int("".join(str(i) for i in pt2), 2)
pt3 = int("".join(str(i) for i in pt3), 2)
pt4 = int("".join(str(i) for i in pt4), 2)

# produce random plaintexts
# pt1 = (str(randint(0, 15)))
# pt2 = (str(randint(0, 15)))
# pt3 = (str(randint(0, 15)))
# pt4 = (str(randint(0, 15)))


# keys generated randomly
# k1, k2, k3, k4 4 bit keys
# key_list 24 permutaiton of k1, k2, k3, k4
# every round uses key_list[i]
k1 = [str(randint(0, 15))]
k2 = [str(randint(0, 15))]
k3 = [str(randint(0, 15))]
k4 = [str(randint(0, 15))]
perm = list(permutations(k1 + k2 + k3 + k4))
# print(perm)
# print(k1, k2, k3, k4)

key_list = []
key_list_abcd = []
for k in range(24):
    key_list_abcd = []
    for i in range(4):
        a = str(k1)
        b = str(k2)
        c = str(k3)
        d = str(k4)
        # print(type(perm[0]))
        key1 = (((int((perm)[k][i]))))
        key_list_abcd.append(key1)
        # print(key_list_abcd)
    key_list.append(key_list_abcd)
# print(k1)
# print(key_list)
# print(pt1, pt2, pt3, pt4)


lrbc(plaintext, key_list)
