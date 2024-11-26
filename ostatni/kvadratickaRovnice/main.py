# Použijte konstrukci pro zachycení výjimek, která má všechny čtyři části
# try
# except
# else
# finally
# pro výpočet kvadratické rovnice po zadání hodnot a, b, c.,
# kde je nutné vždy (finally) vypsat výsledek. V závislosti na tom,
# jestli v diskriminantu dojde k odmocňování záporného čísla
# - buď vypčítejte kořeny v reálných (else) nebo v imaginárních (except) číslech.
import math

while True:

    while True:
        try:
            a = int(input("enter number a: "))
        except ValueError:
            print("enter a valid number")
        else:
            break
    while True:
        try:
            b = int(input("enter number b: "))
        except ValueError:
            print("enter a valid number")
        else:
            break
    while True:
        try:
            c = int(input("enter number c: "))
        except ValueError:
            print("enter a valid number")
        else:
            break


    try:
        d = b**2 - 4*a*c
        if d < 0:
            raise ArithmeticError
    except ArithmeticError:
        print("imagine")
    else:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
    finally:
        print("roots of the equation are " + str(x1) + " " + str(x2))
        break
