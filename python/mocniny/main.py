import math

exponent = int(input("enter exponent: "))
while exponent <= 0:
    print("invalid exponent")
    exponent = int(input("enter exponent: "))
root = int(input("enter root: "))

result = math.pow(root, exponent)
print(result)