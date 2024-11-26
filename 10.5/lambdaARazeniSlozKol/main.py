# Přepodkládejte následující kolekci:
zbozi = [
    {
        "name" : "IPHONE 14",
        "price" : 22169.0,
        "category" : (12, "Mobilní telefony")
    },
    {
        "name" : "Fujifilm XT30",
        "price" : 22269.0,
        "category" : (2, "Fotoaparáty")
    },
    {
        "name" : "Niceboy HIVE Pins Black",
        "price" : 999.0,
        "category" : (4, "Sluchátka")
    }
]
# Pomocí funkce sorted(zbozi, .... ) seřaďte zboží:

# podle ceny vzestupně
# podle názvu sestupně
# podle pořadí kategorie vzestupně

seradit_cena_vzestupne = lambda listek: sorted(listek, key=lambda x: x["price"], reverse=False)
seradit_nazev_sestupne = lambda listek: sorted(listek, key=lambda x: x["name"], reverse=True)
seradit_podle_poradi_kategorie_vzestupne = lambda listek: sorted(listek, key=lambda x: x["category"][0], reverse=False)

print(seradit_cena_vzestupne(zbozi))
print(seradit_nazev_sestupne(zbozi))
print(seradit_podle_poradi_kategorie_vzestupne(zbozi))