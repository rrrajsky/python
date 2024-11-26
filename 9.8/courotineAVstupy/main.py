def vydej_obedu():

    menu = [
         "vitamínový nápoj",
         "polévka česneková s bramborem",
         "segedínský guláš, houskové knedlíky",
         "jablko",
         "polevka gulasova",
         "kureci rizek s bramborovym salatem",
         "mrkev"
    ]

    yield [menu[0]]
    volba = yield "co chces"
    if volba == "A":
        yield [menu[1],menu[2],menu[3]]
    if volba == "B":
        yield [menu[4],menu[5],menu[6]]
    else:
        yield "kys"

corutina1 = vydej_obedu()

napoje = next(corutina1)
print(napoje)
next(corutina1)
jidla = corutina1.send("B")
print(jidla)