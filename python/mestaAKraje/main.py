praha = ["praha"]
ustecky = ["ustí nad labem", "most"]
zlinsky = ["zlín", "kroměříž"]
regions = {"praha" : praha, "ustecky" : ustecky, "zlinsky" : zlinsky}

searched = input("enter a region or a city\n")
if searched in regions:
    print(regions[searched])
elif searched in praha:
    print("praha")
elif searched in ustecky:
    print("ustecky")
elif searched in zlinsky:
    print("zlinsky")
else:
    print("region or city not found")