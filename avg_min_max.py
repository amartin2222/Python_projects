import math
#create empty list
total = 0
count = 0

while True:
    s = input("Enter numbers for a list: ")
    if s == 'done':
        print("Total is: " + str(total))
        print("Count is: " + str(count))
        print("Average is: " + str(total/count))
        break
    try:
        num = float(s)
        total = float(total) + num
        count = float(count) + 1
        continue
    except:
        print("Not a number, try again.")
        continue







