from random import randint

def plaintext():
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
    