def generatorITOsoba():
    try:
        yield "Steve Jobs"
        yield "Ondrej Sprungl"
        yield "Micro Soft"
    except GeneratorExit:
        print("!Generovani preruseno!")