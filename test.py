# python specifically has a 'regular expression' library to search and extract information. It's power lies in how specific it can look for information
# (.+) is a wildcard, expanding to match all the characters between From & @

import re
fhand = open(r'C:\Python_for_everybody\mbox-short.txt')


for line in fhand:
    line = line.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):', line) # FOLLOW TWO DIGIT number between 00 and 99 followed by ':'
    if len(x) > 0:
        print(x)

