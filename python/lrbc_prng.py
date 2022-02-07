from lrbc import lrbc
from itertools import permutations
from random import randint


# random for generating plaintext and keys for starting
# permutations for generating all key permutations
# random 16-bit plaintext created
plaintext = []
for i in range(0, 16):
    n = randint(0, 1)
    plaintext.append(n)

# print(plaintext)

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

f = open("random_numbers_lrbc.txt", "w")

plaintext1 = plaintext
ct_0 = lrbc(plaintext1, key_list)
f.write(ct_0 + "\n")
print(ct_0, "zero")
# ct = int(ct)
# print(type(ct))
ct = [int(x) for x in ct_0]
print(ct, "one")

for i in range(2):
    print(ct, "inin")
    ct = lrbc(plaintext=ct, key_list=key_list)
    print(ct, "in")
    f.write(ct + "\n")
    ct = [int(x) for x in ct]
    print(ct, "ctct")
print(plaintext1, "final_pt")
print(ct, "final_ct")
f.close()
