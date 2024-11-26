# Předpokládejte, že máte následující seznam výherců v soutěži.
# Seznam má tři položky  každá položka je dvojice jména a počtu bodu.

vysledky = [
    ("Karel", 31),
    ("Petr", 10),
    ("Honza", 52),
    ("Eva", 61),
    ("Katka", 0),
]

# Pomocí metody listu, která se nazývá sorted(...) a jejího parametru key napište příkaz,
# který vypíše výsledky seřazené podle počtu bodů vzestupně.

seradit = lambda listek: sorted(listek,key=lambda x: x[1],reverse=False)
print(seradit(vysledky))