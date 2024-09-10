
day = 0

while 0 >= day or day > 31:
    try:
        day = int(input("day of birth: \n"))
    except ValueError:
        print("please enter a number")

month = 0

while 0 >= month or month > 12:
    try:
        month = int(input("month of birth: \n"))
    except ValueError:
        print("please enter a number")

year = input("year of birth: \n")

print("your birthdate is " + str(day) + "." + str(month) + "." + str(year))