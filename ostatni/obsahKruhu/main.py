# Napište program, který vypočítá obsah kruhu podle zadaného poloměru.
# Program musí vyhodit vyjímku ArithmeticError,
# pokud uživatel zadá záporný nebo nulový poloměr.
import math

while True:
    try:
        radius = int(input("enter radius: "))
        if radius <= 0:
            raise ArithmeticError
    except ArithmeticError:
        print("please enter a valid radius")
    except ValueError:
        print("please enter a valid radius")

    else:
        result  = math.pi * radius**2
        print("result is " + str(result))
        break

