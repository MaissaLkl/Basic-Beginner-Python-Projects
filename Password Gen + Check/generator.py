import string
import random

lenght = int(input("Enter lenght of your password (min. 8): "))
if lenght < 8:
    print("Error, the lenght of your password must be of 8 characters minimum")
else:
    print('''Availabe character set for password: 
        1- Digits 
        2- Capital Letters 
        3- Lowercase Letters  
        4- Special Characters 
        5- Exit ''') 

    gcharacters = ""

    while True:
        choice = int(input("Pick a number from the previous list: "))
        if(choice == 1): 
            gcharacters += string.digits
        elif(choice == 2):
            gcharacters += string.ascii_uppercase
        elif(choice == 3):
            gcharacters += string.ascii_lowercase
        elif(choice == 4):
            gcharacters += string.punctuation
        elif(choice == 5):
            break
        else:
            print("Please pick a number from the list")

    if gcharacters:
        gpassword = []

    for i in range(lenght):
        rcharacter = random.choice(gcharacters)
        gpassword.append(rcharacter)

    print("Your generated password is: " + "".join(gpassword))