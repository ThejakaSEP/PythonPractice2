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

