import math

str = 'X-DSPAM-Confidence:0.8475'
pos = str.find(':')
end = str.find(' ', pos)
snip = str[pos+1:end]
print(snip)