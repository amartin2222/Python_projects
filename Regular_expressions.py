# python specifically has a 'regular expression' library to search and extract information. It's power lies in how specific it can look for information
# (.+) is a wildcard, expanding to match all the characters between From & @

import re
fhand = open(r'C:\Python_for_everybody\mbox.txt')

for line in fhand:
    line = line.rstrip()
    if re.search('^From: ', line):  # search re expression that contain 'From'
        print(line)

# '^From:' // matches lines where it appears at the beginning
# '^F..m:' // searches for lines that start with 'F', followed by 2 characters, followed by 'm: '
# '^From:.+@' // matches start with "From:" followed by more characters (.+), followed by @ sign
# [0-9]+ is greedy, tried to make as large a string as possible before extracting those digits

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+',s)
print(lst)

#FINDALL() method searches in the second argument 's' and resturns a list of all the strings that look like the email addresses
# \S+ matches as many non-whitespace characters as possible
# findall() returns list []

for line in fhand: # this program won't run, pycharm won't run more than one for-loop for some reason, first one goes through
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0: # prints lines that have an @ sign between characters
        print(x)

# [a-zA-Z0-9]\S*@\S*[a-zA-Z0-9] the [] represent what we're willing to consider matching such as only Upper/Lower case letters or number
# '*" zero or more non-blank characters
# '*' or '+' applies to the single character immediately left(*@)/right(@*) of the + or *

for line in fhand: # this program won't run, pycharm won't run more than one for-loop for some reason, first one goes through
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z0-9]', line)
    if len(x) > 0: # prints lines that have an @ sign between characters
        print(x)

# search for line that start with X,
# followed by any non whitespace characters and ':'
# followed by a space and any number
# the number can include a decimal
# then print if it's greater than zero.
for line in fhand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)
        # when using findall(), parentheses indicate that you only are interested in extracting a portion of the substring that matches the regular expression
                                            #
# start with Details: rev= (.* followed by any number of characters)
# followed by numbers and '.'
# Then print the number if it is greater than zero

for line in fhand:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9.]+)', line)
    if len(x) > 0:
        print(x)

# ^From .* ([0-9][0-9]):
# start From followed by ' ' match any number od characters (.*)
# followed by ' ', follwoed by two digits [0-9][0-9]
# ADD PARENTHESES AROUND [][]
for line in fhand:
    line = line.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):', line) # FOLLOW TWO DIGIT number between 00 and 99 followed by ':'
    if len(x) > 0:
        print(x)  