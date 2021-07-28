#!/usr/bin/python

ciphertext = "DFBtFS"
keyset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for key in range (len(keyset)):
    translation = ""
    for symbol in ciphertext :
        if symbol in keyset :
            num = keyset.find(symbol)
            num = num - key
            if num <0 :
                num = num + len(keyset)
            translation = translation + keyset[num]
        else :
            translation = translation + symbol 
    print("plaintext with key #%s : %s" % (key, translation))
