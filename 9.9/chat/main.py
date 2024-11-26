
def chatbot():
    yield "Ahoj jak se mas?"


    while True:
        odpoved = yield
        if(odpoved =="Konec"):
            yield "Loucim se"
            break
        elif(odpoved =="Rekni mi vtip"):
            yield "Tady mas dobry vtip: Sli dva a prostredni upad. Haha. Chces slyset dalsi?"
        else:
            yield "Nechapu"

chat = chatbot()  #nastartuje corutinu

print(next(chat))  #spusti prvni cast a pozdravi

while True:
    try:
        next(chat)
        odpoved = input("zadej prikaz: ")
        print(chat.send(odpoved))
    except StopIteration:
        break

chat.close()  #ukonci corutinu