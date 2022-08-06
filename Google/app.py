x = 0
y = ""
z = 0
encryptedPassword = ""
decryptedPassword = ""

password = input('Enter password: ')
cipherKey = input('Enter a 36 character cipher key(if you do not have a cipher, enter "use default key"): ')

if cipherKey == "use default key":
    cipherKey = '''!@#$%^&*()_+-={}|[]:"'<>?,./~`uvwxyz'''

while x < len(password):
    if password[x] == "a":
        y = cipherKey[0]
        encryptedPassword += y
        x += 1
    elif password[x] == "b":
        y = cipherKey[1]
        encryptedPassword += y
        x += 1
    elif password[x] == "c":
        y = cipherKey[2]
        encryptedPassword += y
        x += 1
    elif password[x] == "d":
        y = cipherKey[3]
        encryptedPassword += y
        x += 1
    elif password[x] == "e":
        y = cipherKey[4]
        encryptedPassword += y
        x += 1
    elif password[x] == "f":
        y = cipherKey[5]
        encryptedPassword += y
        x += 1
    elif password[x] == "g":
        y = cipherKey[6]
        encryptedPassword += y
        x += 1
    elif password[x] == "h":
        y = cipherKey[7]
        encryptedPassword += y
        x += 1
    elif password[x] == "i":
        y = cipherKey[8]
        encryptedPassword += y
        x += 1
    elif password[x] == "j":
        y = cipherKey[9]
        encryptedPassword += y
        x += 1
    elif password[x] == "k":
        y = cipherKey[10]
        encryptedPassword += y
        x += 1
    elif password[x] == "l":
        y = cipherKey[11]
        encryptedPassword += y
        x += 1
    elif password[x] == "m":
        y = cipherKey[12]
        encryptedPassword += y
        x += 1
    elif password[x] == "n":
        y = cipherKey[13]
        encryptedPassword += y
        x += 1
    elif password[x] == "o":
        y = cipherKey[14]
        encryptedPassword += y
        x += 1
    elif password[x] == "p":
        y = cipherKey[15]
        encryptedPassword += y
        x += 1
    elif password[x] == "q":
        y = cipherKey[16]
        encryptedPassword += y
        x += 1
    elif password[x] == "r":
        y = cipherKey[17]
        encryptedPassword += y
        x += 1
    elif password[x] == "s":
        y = cipherKey[18]
        encryptedPassword += y
        x += 1
    elif password[x] == "t":
        y = cipherKey[19]
        encryptedPassword += y
        x += 1
    elif password[x] == "u":
        y = cipherKey[20]
        encryptedPassword += y
        x += 1
    elif password[x] == "v":
        y = cipherKey[21]
        encryptedPassword += y
        x += 1
    elif password[x] == "w":
        y = cipherKey[22]
        encryptedPassword += y
        x += 1
    elif password[x] == "x":
        y = cipherKey[23]
        encryptedPassword += y
        x += 1
    elif password[x] == "y":
        y = cipherKey[24]
        encryptedPassword += y
        x += 1
    elif password[x] == "z":
        y = cipherKey[25]
        encryptedPassword += y
        x += 1
    elif password[x] == "0":
        y = cipherKey[26]
        encryptedPassword += y
        x += 1
    elif password[x] == "1":
        y = cipherKey[27]
        encryptedPassword += y
        x += 1
    elif password[x] == "2":
        y = cipherKey[28]
        encryptedPassword += y
        x += 1
    elif password[x] == "3":
        y = cipherKey[29]
        encryptedPassword += y
        x += 1
    elif password[x] == "4":
        y = cipherKey[30]
        encryptedPassword += y
        x += 1
    elif password[x] == "5":
        y = cipherKey[31]
        encryptedPassword += y
        x += 1
    elif password[x] == "6":
        y = cipherKey[32]
        encryptedPassword += y
        x += 1
    elif password[x] == "7":
        y = cipherKey[33]
        encryptedPassword += y
        x += 1
    elif password[x] == "8":
        y = cipherKey[34]
        encryptedPassword += y
        x += 1
    elif password[x] == "9":
        y = cipherKey[35]
        encryptedPassword += y
        x += 1
    else:
        y = password[x]
        encryptedPassword += y
        x += 1

password = ""
print("Your encrypted password is: " + encryptedPassword)

decrypt = input('Would you like to decrypt your password? Y/N: ')

if decrypt == "y" or "Y":
    while z < len(encryptedPassword):
        if encryptedPassword[z] == cipherKey[0]:
            y = "a"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[1]:
            y = "b"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[2]:
            y = "c"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[3]:
            y = "d"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[4]:
            y = "e"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[5]:
            y = "f"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[6]:
            y = "g"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[7]:
            y = "h"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[8]:
            y = "i"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[9]:
            y = "j"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[10]:
            y = "k"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[11]:
            y = "l"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[12]:
            y = "m"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[13]:
            y = "n"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[14]:
            y = "o"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[15]:
            y = "p"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[16]:
            y = "q"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[17]:
            y = "r"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[18]:
            y = "s"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[19]:
            y = "t"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[20]:
            y = "u"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[21]:
            y = "v"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[22]:
            y = "w"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[23]:
            y = "x"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[24]:
            y = "y"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[25]:
            y = "z"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[26]:
            y = "0"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[27]:
            y = "1"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[28]:
            y = "2"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[29]:
            y = "3"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[30]:
            y = "4"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[31]:
            y = "5"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[32]:
            y = "6"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[33]:
            y = "7"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[34]:
            y = "8"
            decryptedPassword += y
            z += 1
        elif encryptedPassword[z] == cipherKey[35]:
            y = "9"
            decryptedPassword += y
            z += 1
        else:
            y = encryptedPassword[z]
            decryptedPassword += y
            z += 1

print('Your decrypted password is: ' + decryptedPassword)