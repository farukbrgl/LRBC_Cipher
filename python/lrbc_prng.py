from lrbc import lrbc
from itertools import permutations
from random import randint
import lrbc_key
import lrbc_plaintext





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
    ciphertext = lrbc(plaintext=ct, key_list=key_list)
    print(ciphertext, "in")
    f.write(ciphertext + "\n")
    ct = [int(x) for x in ciphertext]
    print(ciphertext, "ctct")
print(plaintext1, "final_pt")
print(ct, "final_ct")
f.close()
