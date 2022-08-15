import string
# DO HISTOGRAM OF EMAIL TXT FILE
lhand = open(r'C:\Python_for_everybody\mbox-short.txt')
counts = dict()

for line in lhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1]
    if email not in counts:
        counts[email]=1
    else:
        counts[email]=counts[email]+1
print(counts)