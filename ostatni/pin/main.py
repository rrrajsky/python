pin = 1234
tries = 0
isIn = False

while tries < 3:
    tried = int(input('Enter PIN: '))
    tries += 1
    if pin == tried:
        print("Welcome in.")
        isIn = True
        break

if tries == 3 and not isIn:
    print("too bad.")