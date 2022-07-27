import  numpy as np
import math

# Part-1) The simplest encryption algorithm! (mark 30%)

def ceaser_cypher(message,shift):

    encrypted = []
    for i in range(0,len(message)):
        # print(ord(message[i])+shift)
        x = chr(ord(message[i])+shift)

        # checking whether we go past 'z' or 'Z' as what lies beyond is not an alphabetical Character
        if x.isalpha():
         encrypted.append(chr(ord(message[i])+shift))

        # making wrap around capital 'A'
        elif message[i].isupper():
            encrypted.append(chr(65+(shift-(90-ord(message[i])))-1))

        # making wrap around capital 'a'
        elif message[i].islower():
            encrypted.append(chr(97 + (shift - (122 - ord(message[i])))-1))

    print(encrypted)
    # print(ord("a"),ord("A"))

ceaser_cypher("zack",2)
ceaser_cypher("HAL",1)
ceaser_cypher("cheer",7)


# Part-2) Binary Search Algorithm Implementation in Python (mark 30%)

def binary_search(myList,num):
    min = 0
    max = len(myList)-1

    while min<max:
        mid = int(np.floor((min+max)/2))

        if num == myList[mid]:
            return True
        elif num < myList[mid]:
            max = mid -1
        # elif num > myList[mid]:
        #     min = mid+1
        else:
            min = mid + 1
        #     return False
    return False

numberList = [1,2,3,4,5,6,7]
print(binary_search(numberList,6))
print(binary_search(numberList,27))

# Part-3) Formula Implementation (mark 20%)

def estimate_pi():
    k=0
    sum=0
    point = pow(10,-15)

    while True:
        term = (math.factorial(4*k)*(1103+26390*k))/(pow(math.factorial(k),4)*pow(396,(4*k)))
        k+=1
        if term > point:
            sum+=term
        else:
            break

    pi = 9801/(2*np.sqrt(2)*sum)
    return pi

print(estimate_pi())

# Part-4) Write the corresponding Python code for the following flowchart (mark 20%)

def flowChart():
    n = int(input("Please enter a Number: "))

    x=0

    while n != 0:

        if n%2 ==0:
            x = x+n
        else:
            x = x+n

        n-=1

    return x

print(flowChart())
