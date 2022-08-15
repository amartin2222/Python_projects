# TUPLES ARE LISTS THAT CAN'T BE CHANGED
# REPRESENTED BY (), NOT [] OR {}

# TO CREATE A TUPLE WITH A SINGLE ELEMENT, YOU NEED TO INCLUDE COMMA
t1 = ('a',)
# t1 = ('a') would only be a string, not a tuple

t = tuple('pineapple')
print(t)
# t[0] = 'A' // error: object doesn't support it em assignment

# you can't modify a tuple, but you can replace one tuple with another
t = ('A',)+t[1:]
print(t)

# compare tuples, compares from 1st elements, and then next until it finds a difference
print((0,1,2)<(0,3,4)) # true
print((0,1,2000000)<(0,3,4)) # true

# -----------------------------------------------------------------------

# build list of tuples, where each tuple is preceded by its length
txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))

# sort compares first element to next to break ties. reverse=true to go in decreasing order
t.sort(reverse=True)

# builds a list in descending order, reverse alphabetical order so 'what' appears before 'soft'
res = list()
for length, word in t:
    res.append(word)
print(res)

# ----------------------------------------------------
m = ['have','fun']
x,y =m
print(x)
print(y)

(x,y) = m
print(x)
print(y)

#YOU CAN SWAP VARIABLES
a,b=1,2
a,b=b,a
# a,b = 1,2,3 #error too many values to unpack

addr = 'monty@python.org'
a,b = addr.split('@') #it'll split at the '@'
print(a)
print(b)

# dictionaries method 'ITEMS' returns a LIST of TUPLES [(a.1),(b.2),(c.3)]
d = {'a':10, 'b':1, 'c':22}
t = list(d.items())
print(t)
# now that it's a LIST, it can be sorted
t.sort()
print(t)

# combine ITEMS method, tuple assigment, and 'for loop' to traverse the keys and values in a single loop -no particular order
for key, val in list(d.items()):
    print(val,key)

#sort by value, not key this time
l = list()
for key, val in list(d.items()):
    l.append((val,key))
print(l)

# --------------------------------------------------------------
# #read words in file and assign them to a dictionary, we don't care this time what the values to the keys are
import string
count = 0
fhand = open(r'C:\Python_for_everybody\words.txt')

d_words = dict()                   # Initializes the dictionary
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation)) #get rid of punctuation
    line = line.lower() # make all letters lowercase so cap words are no different
    words = line.split()
    for w in words:
        if w not in d_words: # histogram of 'words' frequency
            d_words[w] = 1
        else:
            d_words[w] += 1

w_lst = list()
for key, val in list(d_words.items()):  # put dictionary in list, sort by value (which is frequency count)
    w_lst.append((val, key))

w_lst.sort(reverse=True)

for key, val in w_lst[:10]: # prints out 10 most common words
    print(key, val)
# --------------------------------------------------------------------
# use TUPLES as KEYS in DICTIONARIES
number = 2709788036
first = 'ash'
last = 'cash'
directory = dict()

directory[last,first] = number #tuple is in brackets
#traverse this dictionary
for last, first in directory:
    print(first,last,directory [last,first])
