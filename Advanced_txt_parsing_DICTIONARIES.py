#read a txt file, remove punctuation before adding to dictionary histogram
import string
fhand = open(r'C:\Python_for_everybody\words.txt')
counts = dict()
for line in fhand:
    line =line.strip()
    #delete punctuation, first two parameters replace another but can be empty strings
    line = line.translate(line.maketrans("","", string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word]=counts[word]+1
print(counts)