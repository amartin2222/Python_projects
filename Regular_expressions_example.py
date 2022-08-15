import re

fhand = open(r'C:\Python_for_everybody\mbox.txt')
lhand = open(r'C:\Python_for_everybody\mbox-short.txt')
#reg = input("Enter a regular expression: ")
count = 0
counts = 0
avg = 0
lst = []


# look for this line but ONLY extract the number([]), calc avg
for line in lhand:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9.]+)', line)
    y = float(x)
    if len(x) > 0:
        counts = counts+1
        lst.append(x)

print(lst)
# avg = sum(lst)/len(lst)
# print(avg)

# ------------------------------------------------------
# ask for reg expression / count lines that matched the reg expression
for line in fhand:
    line = line.rstrip()
    x = re.findall(str(reg), line)
    if len(x)>0:
        count = count + 1
print("mbox.txt had " + str(count) + " lines that matched " + str(reg))
# ----------------------------------------------------
