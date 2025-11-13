""" Caeser Cipher """
## this prgram considers an input file and encrypts it by using caeser cipher by that it shifts every letter by 3 units. For example, a becomes d, b becomes e and so on...w -> z, x-> a, y -> b, z ->c

import string

def create_caeser_dict():
    l = list(string.ascii_lowercase)
    d = {}
    for i in range(len(l)):
        d[l[i]]=l[(i+3)%26]
    return d

f = open("mytext.txt", "r")
g = open("encryptedMytext.txt", "w")

d = create_caeser_dict()
c = f.read(1)
while (c != ""):
    g.write(d[c])
    c= f.read(1)
f.close()
g.close()

g = open("encryptedMytext.txt", "r")
print(g.read())
g.close()

## decypting the caeser cipher ##

def decrypt_caser_dict():
    l = list(string.ascii_lowercase)
    d = {}
    for i in range(len(l)):
        d[l[i]] = l[i - 3] if i >= 0 else l[(i-3) + 26]
    return d

f = open("encryptedMytext.txt", "r")
g = open("decryptedMytext.txt", "w")

d = decrypt_caser_dict()
c = f.read(1)
while(c!= ""):
    g.write(d[c])
    c = f.read(1)
f.close
g.close

g = open("decryptedMytext.txt", "r")
print(g.read())
g.close()
