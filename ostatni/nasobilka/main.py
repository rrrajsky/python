
number = 1
numberer = 1
done = False

while not done:
    result = number * numberer
    print(str(number) + "*" + str(numberer) + " = " + str(result))

    if number == 10 and numberer == 10:
        done = True
        break

    numberer = numberer + 1

    if numberer == 11:
        numberer = 1
        number += 1

    