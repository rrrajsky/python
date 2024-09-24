# Vytvořte model šesti českých řek, že model bude obsahovat u každé řeky její název,
# místo kde pramení a také místo kde se řeka vlévá do jiné řeky a informaci o tom,
# která z řek po spojení pokračuje a která zaniká.
# Napište program, který po zadání názvu řeky vypíše všechny řeky, které se do ní připojují a případně i řeku,
# do které se nakonec vlévá zadaná řeka.

vltava = {"name" : "vltava", "source" : "šumava", "end" : "labe"}
labe = {"name" : "labe", "source" : "krkonoše", "end" : "severní moře"}
morava = {"name" : "morava", "source" : "kralický sněžnik", "end" : "dunaj"}
dyje = {"name" : "dyje", "source" : "dolní rakousy", "end" : "morava"}
sazava = {"name" : "sazava", "source" : "šindelný vrch", "end" : "vltava"}
opava = {"name" : "opava", "source" : "vrbno pod pradědem", "end" : "odra"}

rivers = {"vltava" : vltava, "labe": labe, "morava" : morava, "dyje" : dyje, "sazava" : sazava, "opava" : opava}

searched = input("enter a river\n")
for each in rivers:
    if rivers[searched]["end"] in each:
        print(rivers[each]["name"])


