import string
import random
from datetime import datetime
import sys
from termcolor import colored

def makePassword():
    passin = input(colored("Please enter the password you would like to use to secure your diary: \n", 'yellow'))
    with open ('password.txt', 'w') as password:
        password.write(encrypt(passin))
    
    print("Password confirmed! \n Please run the program again to use the diary.")
    sys.exit(0)

def checkPassword():
    with open ('password.txt', 'r') as passfile:
        password = passfile.read()
    
    if password != "":
        password = decrypt(password).strip()
        passtry = ""
        while (password != passtry):
            passtry = input(colored("Password: \n", 'yellow'))

    else:
        makePassword()


def encrypt(text):
    alphabet = string.ascii_letters
    encrypted = ""
    for c in text:
        encrypted+=c
        encrypted+=alphabet[random.randint(0,len(alphabet)-1)]
    return encrypted[::-1]

def decrypt(message):
    sliced = message.split("|||")
    glued = ""
    for piece in sliced:
        glued += (piece[1::2])[::-1] + "\n"
    return glued

def transfer():
    print(colored("\n Write your entry and type END on a new line to finish entry.", 'green'))
    line = ""
    arrayedMessage = []
    while line != "END":
        line = input("")
        arrayedMessage.append(line)

    with open ('diary.txt', 'a') as diary:
        diary.write("%~=" +  datetime.today().strftime('%m-%d-%Y') + "%~=")
        for line in arrayedMessage:
            diary.write("|||" + encrypt(line))

checkPassword()
while True:
    action = input(colored("\n What do you want to do? (read/write/quit) \n", 'yellow'))
    if action == "write":
        transfer()
    elif action == "read":
        with open ('diary.txt', 'r') as diary:
            diary = diary.read()
        arrayed = diary.split("%~=")
        dates = arrayed[1::2]
        entries = arrayed[2::2]
        print("\n=====\n")
        for i in range(len(dates)):
            print(colored(dates[i], 'cyan') + decrypt(entries[i]))
        print("=====")
    elif action == "quit":
        sys.exit(0)