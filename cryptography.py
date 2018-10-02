"""
cryptography.py
Author: Eamon
Credit: none

Assignment: cryptography

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
todo = input("Enter e to encrypt, d to decrypt, or q to quit: ")
options = ["e","d","q"]
a=1
b=1


while a == b:
    if todo not in options:
        print("Did not understand command, try again.")
        todo = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if todo == "e":
        msg = input("Message: ")
        key = input("Key: ")
        msglist = list(msg)
        k = len(key)
        m = len(msg)
        keylist = list(key)
        while k<m:
            keylist.extend(keylist)
            k = len(keylist)
        while k>m:
            keylist.pop()
            k = len(keylist)
        #print(keylist)
        #print(k)
        encryptlist = ""
        e = len(msglist)
        for q in range(0,e):
            w = associations[(associations.find(msglist[q]) + associations.find(keylist[q]))%85]
            encryptlist = encryptlist + str(w)
        print(encryptlist)
        todo = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if todo == "d":
        msg = input("Message: ")
        key = input("Key: ")
        msglist = list(msg)
        k = len(key)
        m = len(msg)
        keylist = list(key)
        while k<m:
            keylist.extend(keylist)
            k = len(keylist)
        while k>m:
            keylist.pop()
            k = len(keylist)
        #print(keylist)
        #print(k)
        uncryptlist = ""
        e = len(msglist)
        for q in range(0,e):
            w = associations[(associations.find(msglist[q]) - associations.find(keylist[q]))%85]
            uncryptlist = uncryptlist + str(w)
        print(uncryptlist)
        todo = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    else:
        print("Goodbye!")
        b=2
    
    
    #if todo == "q":
        #print("Goodbye!")
        #b=2
        #a=5
        #todo = "q



