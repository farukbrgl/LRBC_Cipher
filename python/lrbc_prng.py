# execution time : 18.869 s

from lrbc import lrbc
from itertools import permutations
from random import randint
import lrbc_key
import lrbc_plaintext


k1 = [str(randint(0, 15))]
k2 = [str(randint(0, 15))]
k3 = [str(randint(0, 15))]
k4 = [str(randint(0, 15))]
perm = list(permutations(k1 + k2 + k3 + k4))
# print(perm)

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


f = open("random_numbers_lrbc.txt", "w")
plaintext = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
plaintext1 = plaintext
ct_0 = lrbc(plaintext1, key_list)
f.write(ct_0 + "\n")
print(ct_0, "zero")
# ct = int(ct)
# print(type(ct))
ct = [int(x) for x in ct_0]
print(ct, "one")

for i in range(99999):
    print(ct, "inin")
    ciphertext = lrbc(plaintext=ct, key_list=key_list)
    print(ciphertext, "in")
    f.write(ciphertext + "\n")
    ct = [int(x) for x in ciphertext]
    print(ciphertext, "ctct", i)
print(plaintext1, "final_pt")
print(ct, "final_ct")
f.close()
