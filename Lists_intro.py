import math
max_value = 0
min_value = 0
lst = []
while True:
    x = input("Enter a number: ")
    if x == 'done':
        print(lst)
        max_value = max(lst)
        min_value = min(lst)
        print("Maximum: " + str(max_value))
        print("Minimum: " + str(min_value))
        break
    try:
        lst.append(float(x))
        # for i in lst():
        #     if max is None or i>max:
        #         max = i
        #     elif min is None or i<min:
        #         min = i
        #     else: continue
    except:
        print("Didn't get added to list")
        continue

#--------------------------------------
s = "Sea Bass and mashed potatoes with a martini."
spl = list(s)
print(spl)

#   list(s) breaks into letters
#   s.split() breaks lines into words

s = "Sea Bass and mashed potatoes with a martini."
half = s.split()
print(half)
print(half[3])

#   split with an optional argument (,)
p = 'potatoe,potatoe,potatoe'
x = ','
print(p.split(x))

#   join (opposite of split), combines with an optional argument(' ')
t = ['potatoe','potatoe','potatoe']
a = ' '
print(a.join(t))

#-----------------------------------------------------
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