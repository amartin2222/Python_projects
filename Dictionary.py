# dictionaries are key pairs, sets of values assigned to another
#come in curly brackets {}
fhand = open(r'C:\Python_for_everybody\words.txt')
lhand = open(r'C:\Python_for_everybody\mbox.txt')
thand = open(r'C:\Python_for_everybody\mbox-short.txt')
#-----------------------------------------------------------------------------
eng2sp = dict()
print(eng2sp)

eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {'one':'uno', 'two':'dos', 'three':'tres'}
print(eng2sp)
print(eng2sp['two'])
#print(eng2sp['four']) (KeyError: 'four')
print('one' in eng2sp) #true
print('uno' in eng2sp) #false

# you can use method 'values' which returns the value as a type that can be converted to a list and then used by the 'in' operator
vals = list(eng2sp.values())
print('uno' in vals)
# ------------------------------------------\
# Histogram for letters GET FUNCTION TO CLEAN UP
word = 'mississippi'
z = dict()
for c in word:
    z[c] = z.get(c,0)+1
print(z)

# Histogram for letters
# for c in word:
#     if c not in z:
#         z[c]=1
#     else:
#         z[c] = z[c]+1
# print(z)
#---------------------------------------


p = dict()
#histogram for words
for line in fhand:
    words = line.split()
    for word in words:
        if word not in p:
            p[word]=1
        else:
            p[word]=p[word]+1
print(p)
#------------------------------------------------------------------------------------
# #read words in file and assign them to a dictionary, we don't care this time what the values to the keys are
count = 0
dictionary_words = dict()                   # Initializes the dictionary
for line in lhand:
    words = line.split()
    words = line[1]
    for word in words:
        count += 1
        if word in dictionary_words:
            continue                        # Discards duplicates
        dictionary_words[word] = count      # Value is first time word appears
if 'Python' in dictionary_words:
    print('It is in the dictionary')
else:
    print('False')
#--------------------------------------------------------

