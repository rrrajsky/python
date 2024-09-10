
isDone = False

while not isDone:
    name = input("Hi, what's your name? \n")
    sure = input("Are you sure your name is " + name + "? (Y/N) \n")
    if sure == "Y" or sure == "y":
        isDone = True

print("bye bye")