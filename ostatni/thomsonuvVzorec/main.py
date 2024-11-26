# Přidejte do nasledujiciho algoritmu zachyceni dvou typů vyjimek.
# Jednu pro zachycení toho, že uživatel nezadal číslo a druhou,
# ke které dojde při odmocnění  záporného čísla.
# V případě zadání nečíselné hodnoty uživatele vyzve k zadani dané hodnoty znovu,
# v případě odmocnování záporného čísla musí dojít k zopakování zadání všech hodnot znovu.

from math import sqrt

while True:

    while True:
        try:
            L = int(input("Zadej indukcnost [H]:"))
        except ValueError:
            print("enter a valid number")
        else:
            break

    while True:
        try:
            C = int(input("Zadej kapacitu [F]:"))
        except ValueError:
            print("enter a valid number")
        else:
            break

    try:
        rooted = L * C
        if rooted <= 0:
            raise ArithmeticError
        F = 1 / (2 * 3.14 * sqrt(rooted))
    except ArithmeticError:
        print("try again with valid numbers")
    else:
        break

print("Frekvence je: " + str(F) + "Hz")