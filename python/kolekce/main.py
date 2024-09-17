
print("BASIC CREATION OF COLLECTIONS")
exampleTuple = (1,4,5,41,8,4,"AAA", None)
exampleList = [1,4,5,41,8,4,"AAA", None]
exampleSet = {1, 4, 5, 41, 8, 4, "AAA", None}
exampleDictionary = {"1": "one", "4": "four", "AAA": "AAAAAA", "none":None, "4": "four"}
exampleString = "1,4,5,41,8,4,AAA,None"

print("tuple: ")
print(exampleTuple)

print("list: ")
print(exampleList)

print("set: ")
print(exampleSet)

print("dictionary: ")
print(exampleDictionary)

print("string: ")
print(exampleString)

print()
print("INSERTING COLLECTIONS INTO COLLECTIONS")

print("tuple: ")
exampleTuple2 = (9, exampleTuple, exampleList, exampleSet, exampleDictionary, exampleString)
print(exampleTuple2)

print("list: ")
exampleList2 = [9, exampleTuple , exampleList, exampleSet, exampleDictionary, exampleString]
print(exampleList2)

print("set: ")
exampleSet2 = {9, exampleTuple}
print(exampleSet2)
# *
# st2 = {9, tup}
# print(st2)
# you can only put tuples and strings into sets

print("dictionary: ")
exampleDictionary2 = {"nine":9, "tuple":exampleTuple, "list":exampleList, "set":exampleSet, "dictionary":exampleDictionary, "string":exampleString}
print(exampleDictionary2)

# **
# print("stri: ")
# stri2 = "9" + tup + lis + st + dic + stri
# print(stri2)
# can't directly add to string, changing types needed

print()
print("CHANGING SIZES OF COLLECTIONS")

# ***
# tuple has no method to insert on it's own
# you can only make a new tuple
# tup += tup # works
# tup.insert doesn't exist

print("list: ")
exampleList.insert(2,"inserted")
print(exampleList)

print("set: ")
exampleSet.add("inserted")
print(exampleSet)

print("dictionary: ")
exampleDictionary["insertedKey"] = "inserted"
print(exampleDictionary)

print("string: ")
exampleString += ",inserted"
print(exampleString)

print()
print("GETTING LENGTHS OF COLLECTIONS")

print("tuple: ")
print(len(exampleTuple)) #lenght of tuple
print("list: ")
print(len(exampleList)) #lenght of lists
print("set: ")
print(len(exampleSet)) #lenght of sets
print("dictionary: ")
print(len(exampleDictionary)) #lenght of dictionaries
print("string: ")
print(len(exampleString)) #lenght of strings

print()
print("DIFFERENT INSERT METHODS")

# tuple has none

print("list:")
exampleList.insert(4,"inserted2") # index and inserted object
exampleList.append("appended") # inserted object
print(exampleList)

print("set:")
exampleSet.add("inserted2") # inserted object
print(exampleSet)

print("dictionary:")
exampleDictionary["insertedKey2"] = "inserted2" # key in [] and inserted object
print(exampleDictionary)

print("string: ")
exampleString += ",inserted2" # not a method, only adding
print(exampleString)

print()
print("DELETION OF OBJECTS IN COLLECTIONS")

# tuple has none

print("list:")
exampleList.remove("inserted2") # removes specified object
exampleList.pop(1) # removes object at specified index
del exampleList[1] # removes object at specified index
print(exampleList)
exampleList.clear() # removes everything
print(exampleList)

print("set:")
exampleSet.remove("inserted2") # removes specified object
exampleSet.discard("inserted") # removes specified object
exampleSet.discard("nothing") # if such object is not there, do nothing
exampleSet.pop() # removes a random object
print(exampleSet)
exampleSet.clear() # removes everything
print(exampleSet)

print("dictionary:")
exampleDictionary.pop("insertedKey2") # removes specified object
exampleDictionary.popitem() # removes last object
del exampleDictionary["1"] # removes object with specified key
print(exampleDictionary)
exampleDictionary.clear() # removes everything
print(exampleDictionary)

# string can't delete from itself

print()
print("EDITING OBJECTS IN COLLECTIONS")

# tuple has none

print("list:")
exampleList = [1,4,5,41,8,4,"AAA", None]
exampleList[1] = "edited" # edits objects at specified index
print(exampleList)
exampleList[2:4] = ["edited2", "edited3", "edited4"] # edits objects in specified range

print("set:")
