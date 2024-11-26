def generatorSudychCisel(od, do):
    i = od
    if i % 2:
        i = i+1
    while(i <= do):
        yield i
        i=i+2

for x in generatorSudychCisel(3,51):
    print(x)