# Napište program, který uživatele vyzve k zadání datumu narození podle definovaných pravidel.
# Následně program provede tyto kontroly tak, že když jedna z nich selže vyhodí se (raise)
# klasická výjimka (Exception) a další kontroly se již nespouštějí.
# Při zachycení výjimky vždy vypisujte chybovou hlášku:

# Rok musí být nastaven tak, aby člověku bylo nejméně 0 a nejvíce zhruba 119 let.
# Pokud ne vytvořte chybovou hlášku týkající se roku.

# Měsíc musí být číslo od 1 do 12. Pokud ne vytvořte chybovou hlášku týkající se měsíce.

# Den musí být pro měsíce 1,3,5,7,8,10,12 max. 31, pro únor max.
# 29 (přestupné roky neřešte) a pro ostatní 30. Pokud ne vytvořte chybovou hlášku týkající se dne.

# Datum narození nesmí odpovídat datu, které spadá do letních prázdnin. Pokud ano napište nepovolené datum.

while True:
    while True:
        try:
            year = int(input('Enter year: '))
            if not 2024 > year > 1905:
                raise Exception
        except Exception:
            print('you have to be 0 - 119 year old')
        else:
            break

    while True:
        try:
            month = int(input('Enter month: '))
            if not 1 <= month <= 12:
                raise Exception
        except Exception:
            print('enter a valid month')
        else:
            break

    while True:
        try:
            day = int(input('Enter day: '))



            if not 1 <= day <= 31:
                raise Exception
        except Exception:
            print('enter a valid day')
        else:
            break
