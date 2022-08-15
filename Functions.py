#'get' function needs default value in case it fails
counts = {'chuck':1, 'annie':42, 'jan':100}
print(counts.get('jan',0))
print(counts.get('jack',0))

#use 'get' function to elimate the need for if statement, it already handles case where key not in dict
word = 'mississippi'
d = dict()
for c in word:
    d[c]=d.get(c,0)+1
print(d)

