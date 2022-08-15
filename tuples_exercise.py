# read file, print letters in decreasing order of frequency. Covert all letters to lowercase and only count the letters a-z. Don't count spacese, digits, punctuation.

import string
fhand = open(r'C:\Python_for_everybody\mbox.txt')

d = dict()                   # Initializes the dictionary
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation)) # get rid of punctuation
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.lower() # make all letters lowercase so cap words are no different
    words = line.split()
    for word in words:
        for char in word:
            if char not in d: # histogram of 'words' frequency
                d[char] = 1
            else:
                d[char] += 1

lst = list()
for key, val in list(d.items()):  # put dictionary in list, sort by value (which is frequency count)
    lst.append((val, key))

lst.sort()

print(lst)