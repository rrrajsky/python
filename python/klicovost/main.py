
weNeed = 14513
packet = 100

grows = packet * 0.8
dies = grows * 0.08

survives = grows - dies
soFar = 0

howManyPackets = 0

while soFar < weNeed:

    soFar += survives
    howManyPackets = howManyPackets + 1

print("we need " + str(howManyPackets) + " packets of seeds")