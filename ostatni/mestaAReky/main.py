# Vytvořte pomocí libovlné kolekce, nebo jejich kombinací evidencí tří řek v ČR.
# U každé řeky evidujte její název, místo ve kterém pramení a další tři města nebo vesnice,
# kterými protéká. Napište program, který po zadání názvu města vypíše řeku, nebo řeky,
# které městem protékají a po zadání řeky vypíše všechna města, kterými protéká včetně místa kde pramení.

labe = {"name" : "labe" ,"source" : "krkonose", "flow" : ["ústí nad labem", "bad schandau", "lutherstadt wittenberg"]}
vltava = {"name" : "vltava" ,"source" : "sumava", "flow" : ["veltrusy", "rožmberk nad vltavou", "větrní"]}
svratka = {"name" : "svratka","source" : "křivý javor", "flow" : ["veverská bítýška", "jimramov", "rajhrad"]}
rivers = {"labe" : labe,"vltava" : vltava,"svratka" : svratka}

searched = input("enter river or city\n")
if searched in rivers:
    print("it's source is " + rivers[searched]["source"] + " and it flows through " + str(rivers[searched]["flow"]))
if searched in labe["flow"]:
    print(labe["name"])
if searched in vltava["flow"]:
    print(vltava["name"])
if searched in svratka["flow"]:
    print(svratka["name"])