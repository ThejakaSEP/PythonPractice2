# 1)

def strLength(myString):
    return len(myString)

print('String length is', strLength("Praveen"))

# 2)

def countChar(myString):
    # countDict ={}
    keys =[]
    values =[]
    for i in myString:
        keys.append(i)
        values.append(myString.count(i))

    countDict = dict(zip(keys, values))
    return countDict

print(countChar("Praveen"))

# 3)
from parse import *

name = "Praveen"

print("My name is {fname}".format(fname = name))

print(parse("My name is {}", "My name is Praveen"))
