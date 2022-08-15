import math
fhand = open(r'/mbox.txt')
thand = open(r'/mbox-short.txt')
count = 0
counts = 0
sum = 0
avg = 0

#find lines, split lines, print part of line
#(rstrip removes any white spaces at the end of the string)
for line in thand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    counts = counts + 1
    words = line.split()
    print(words[1])
print("There were " + str(counts) + " lines in the file with From as the first word.")

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        x = float((line[19:26]))
        count = count + 1
        sum = sum + x
        avg = sum / count
print("Average spam confidence: " + str(avg))

# -----------------------------------------------

