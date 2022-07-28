# 1)
import string


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

print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.punctuation)
print("My name is {fname}".format(fname = name))
print(parse("My name is {}", "My name is not Praveen"))
print("Sexy {0!s}".format('Praveen',1,34))
print('{:<30}'.format('left aligned'))
print('{:>60}'.format('right aligned'))


#4)

myTuple = (3, 5)
print('X: {0[0]};  Y: {0[1]}'.format(myTuple))

myList = [192, 168, 0, 1]
print('{:02X}{:02X}{:02X}{:02X}'.format(*myList))

print('{0}{1}{0}{2}'.format('abra', 'cad','Praveen'))

from string import Template
d = dict(who='Praveen')
print(Template('$who likes time travel').safe_substitute(d))
