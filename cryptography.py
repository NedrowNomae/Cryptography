"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
todo = input("Enter e to encrypt, d to decrypt, or q to quit: ")
options = ["e","d","q"]
encryptlist = []


while todo not in options:
    print("Did not understand command, try again.")
    todo = input("Enter e to encrypt, d to decrypt, or q to quit: ")
if todo == "e":
    msg = input("Message: ")
    code = ""
    for i in range(0,len(msg)):
        code = code + str(associations.find(str(msg[i])))
        encryptlist.append(str(associations.find(str(msg[i]))))
if todo == "d":
    print("d")
if todo == "q":
    print("q")
print(code)
print(encryptlist)
back = ""
for q in range(0,len(encryptlist)):
    back = back + str(associations[q])
#associations[index]