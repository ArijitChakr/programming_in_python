'''# remove characters that are other than english letter from the string

import string

s = "Arijit&%@)INdia)(U)#*!&)westBengal*(&@^(^@(*$^())))Kolkata"

eng = string.ascii_letters

letters = tuple(eng)

l = list(s)
filtered = []

for el in l:
    if el  in letters:
        filtered.append(el)

s = "".join(filtered)
print(s)

'''

def poly(L, x_0):
    psum = 0
    n = len(L)
    for i in range(n):
        psum = psum + L[i] * (x_0 ** i)
    return psum

def poly_zeros(L, a, b):
    zeros = [ ]
    for x in range(a, b + 1):
        if poly(L, x) == 0:
            zeros.append(x)
    return zeros

print(poly_zeros([-180, -144, 101, 52, -18, -4, 1], 0, 4))