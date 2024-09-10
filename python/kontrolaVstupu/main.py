
# Opravte nasledující algoritmus tak, aby pokud uživatel nezadá číslo,
# program neskončil chybovou hláškou. Namísto toho uživatele znovu vyzve,
# ať zadá číslo a tento požadavek bude opakovat tak dlouho, dokud uživatel skutečně nezadá číslo.
# K řešení musíte použít konstrukci try/except

while True:
    try:
        x = int(input("enter number: "))

    except ValueError:
        print("please enter a valid number")

    else:
        break

y = int(x) + 1
print(y)
