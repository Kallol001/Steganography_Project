import cv2
import os
import string

def create_mapping():
    char_to_int = {char: i for i, char in enumerate(string.printable)}
    int_to_char = {i: char for i, char in enumerate(string.printable)}
    return char_to_int, int_to_char

def encrypt_message(img, msg, mapping):
    n, m, z = 0, 0, 0

    for char in msg:
        img[n, m, z] = mapping[char]
        n += 1
        m += 1
        z = (z + 1) % 3

    return img

def decrypt_message(img, mapping):
    message = ""
    n, m, z = 0, 0, 0

    for i in range(len(msg)):
        message += mapping[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3

    return message

img = cv2.imread("mypic.jpg")
msg = input("Enter The Message Here: ")
password = input("Enter password: ")

char_to_int, int_to_char = create_mapping()

# Encryption
img = encrypt_message(img, msg, char_to_int)

cv2.imwrite("Encryptedmsg.jpg", img)
os.system("start Encryptedmsg.jpg")

# Decryption
message = ""

pas = input("Enter Password for Decryption: ")

if password == pas:
    message = decrypt_message(img, int_to_char)
    print("Decrypted message: ", message)
else:
    print("Wrong Password")