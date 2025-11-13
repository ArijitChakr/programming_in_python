## count of same words in a list and maximum number of occurance of a word ##
malgudi = [
    "It", "was", "Monday", "morning", "Swaminathan", "was", "reluctant", "to", "open", "his", "eyes","he", "considered", "Monday", "specially", "unpleasant", "in", "the", "calendar", "After", "the", "delicious", "freedom", "of", "Saturday", "and", "Sunday","it", "was", "difficult", "to", "get", "into", "the", "Monday", "mood", "of", "work", "and", "discipline","He", "shuddered", "at", "the", "very", "thought", "of", "school","the", "dismal", "yellow", "building", "the", "fire-eyed", "Vedanayagam","his", "class", "teacher", "and", "headmaster", "with", "his", "thin", "long", "cane"
]

def occurance_of_words(list):
    occ = {}
    max = 0
    max_word = ''
    for word in list:
        if(word in occ):
            occ[word] += 1
        else:
            occ[word] = 1
        if(occ[word] > max):
            max = occ[word]
            max_word = word
    return ({max_word: max}, occ)

max_occ, words = occurance_of_words(malgudi)
print(max_occ, words)

## Sorting using functions: breaking big problems in small functions ##

def obvious_sort(l):
    sorted_list = []
    while(len(l) > 0):
        mini = l[0]
        for i in l:
            if (i < mini):
                mini = i
        sorted_list.append(mini)
        l.remove(mini)
    return sorted_list


# breaking into 2 small functions

def min_list(l):
    mini = l[0]
    for i in l:
        if (i < mini):
            mini = i
    return mini

def obvious_sort1(l):
    x = []
    while(len(l)> 0 ):
        mini = min_list(l)
        x.append(mini)
        l.remove(mini)
    return x

l = [90, 23, 97, 88, 5, 1]
print(obvious_sort1(l))        


'''## Matrics multiplication ##'''

r1 = [1,2,3]
r2 = [4,5,6]
r3 = [7,8,9]

s1 = [1,2,1]
s2 = [6,2,3]
s3 = [4,2,1]

A = []
B = []
A.append(r1)
A.append(r2)
A.append(r3)

B.append(s1)
B.append(s2)
B.append(s3)

C = [[0,0,0],[0,0,0],[0,0,0]]

dim = 3

# C[i][j] is the dot product of the ith row of A and jth column of B
# C[2][1] += A[2] * B[1]

for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            C[i][j] += A[i][k] * B[k][j]

print(C)

# Using numpy

import numpy

X = numpy.mat(A)
Y = numpy.mat(B)

print(X*Y)

t = {1:2,2:3}
print(type(t.popitem()))

