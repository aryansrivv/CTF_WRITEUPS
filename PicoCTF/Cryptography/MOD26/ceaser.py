#!/usr/bin/python
from random import randint

def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char)+s-65) % 26 + 65)
        elif (char == " "):
            result += " "
        else :
            result += chr ((ord(char)+s-97) % 26 + 97)
    return result

text = input("ENTER THE PLAINTEXT : ")
decide = input("DO YOU WANT A RANDOM OR A SPECIFIC KEY?(R/S)")
if (decide == "R"):
    s = randint(0,26)
else :
    s = int (input("WRITE THE VALUE OF THE KEY : "))

print ("Plain Text : " + text)
print ("Shift pattern : " + str(s))
print ("Cipher: " + encrypt (text,s))
