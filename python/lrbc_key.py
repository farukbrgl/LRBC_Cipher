from random import randint
from itertools import permutations

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