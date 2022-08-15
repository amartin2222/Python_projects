# is operator, it helps equate two values
a = 'bannana'
b = 'bannana'
print(a is b)

# when you make two lists, they are two "SEPARATE" objects and are not equal
c = [1,2,3]
d = [1,2,3]
print(c is d)

#both variables refer to same object when assigned
e = [1,2,3,4,5]
f = e
print(e is f)

#since same, changing one element will change it for the other
# you can change a value inside
e[0]=69
print(e)

#modify and create a new list vs modify origional list (not a copy)
def middle():
    list2 = e[1:-1]
    return list2
def chop():
    del e[0]
    del e[-1]
    return None

print(middle())
print(e)
print(chop())
print(e)

