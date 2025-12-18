import random
import string

chars = list(string.punctuation + string.digits +" "+ string.ascii_letters)
key = chars.copy()
random.shuffle(key)


def encrypt(plain_text):
    encrypted_text = ""
    for letter in plain_text:
        index = chars.index(letter)
        encrypted_text+=key[index]
    return encrypted_text

def decrypt(encrypted_text):
    plain_text = ""
    for letter in encrypted_text:
        index = key.index(letter)
        plain_text+=chars[index]
    return plain_text

while True:
    print("----ENCRYPTION PROGRAM-----")
    print("1. encrypt")
    print("2. decrypt")
    print("3. exit")
    print("---------------------------")
    action = input("select action: ")
    if action == "1":    
        plain_text = input("enter message to encrypt: ")
        encrypted_text = encrypt(plain_text)
        print(f"plain text: {plain_text}")
        print(f"encrypted text: {encrypted_text}")
    elif action == "2":
        encrypted_text = input("enter message to decrypt: ")
        plain_text = decrypt(encrypted_text)
        print(f"encrypted text: {encrypted_text}")
        print(f"decrypted text: {plain_text}")
    elif action == "3":
        print("program exited")
        break
    else:
        print("invalid command")
    input("...")