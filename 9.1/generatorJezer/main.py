def generatorRaselinnychJezerCR():
    yield "Chalupské jezírko"
    yield "Velké mechové jezírko"
    yield "Jezírko pod Táborem"
    yield "Malé mechové jezírko"
    yield "Rosička"

print("Raselinna jezera v CR")
for jezero in generatorRaselinnychJezerCR():
    print(jezero)