
def computegrade():
    grade = float(input("Enter grade between 0-1: "))
    if grade > 1.0 or grade < 0.6:
        print("Bad Number")
    elif grade >= 0.9:
        print("Your grade is A")
    elif grade >= 0.8:
        print("Your grade is B")
    elif grade >= 0.7:
        print("Your grade is C")
    elif grade >= 0.6:
        print("Your grade is D")
    else:
        print("Your grade is F")

computegrade()


# hours = float(input("Enter Hours\n"))
# rate = float(input("Enter Rate\n"))
# pay = 40*rate
#
# if hours <= 40:
#     print(pay)
# if hours > 40:
#     over_pay = (hours - 40) * (rate * 1.5)
#     print("overpay is " + str(over_pay))
#     print("Total is: " + str(over_pay+pay))
# else: print("Enter another number please.")

# width = 17
# height = 12.0
#
# print(width//2)
# print(width/2.0)
# print(height/3)
# # print(1+2*5)

