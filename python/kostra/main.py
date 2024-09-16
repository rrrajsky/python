# Napište kostru programu (ted jen základ programu) pro výpočet Ohmova zákona tak,
# že uživatel zadá libovolné dvě veličiny a program vždy dopočítá tu třetí.
#
# Implementujte však pouze výpočet jedné z nich, je-li zadaná správně
# a ostatní varianty jen připravte, tak aby bylo jasné,
# do kterého místa ve zdrojovém kódu se má daný výpočet dopsat tak,
# že na toto místo ve zdrojovém kódu umístíte vyhození (raise) vyjímky NotImplementedError

u = -1
while u == -1 or None:
    inputU = input("voltage (leave empty if none): \n")
    if inputU == "":
        u = None
        break
    else:
        try: u = float(inputU)
        except ValueError:
            print("please enter a valid number or nothing")
            u = -1

r = -1
while r == -1 or None:
    inputR = input("resistance (leave empty if none): \n")
    if inputR == "":
        r = None
        break
    else:
        try: r = float(inputR)
        except ValueError:
            print("please enter a valid number or nothing")
            r = -1

i = -1
while i == -1 or None:
    inputI = input("current (leave empty if none): \n")
    if inputI == "":
        i = None
        break
    else:
        try: u = float(inputI)
        except ValueError:
            print("please enter a valid number or nothing")
            i = -1
try:

    result = None

    if u is None:
        result = float(r*i)
    elif r is None:
        raise NotImplementedError
    elif i is None:
        raise NotImplementedError
    else:
        print("you made a mistake somewhere")

except NotImplementedError:
    print("not implemented")

