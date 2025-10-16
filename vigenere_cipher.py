def adjusted_key(text,key):
    adjusted=""
    key_pos=0
    for char in text:
        if 97<=ord(char)<=122:
            adjusted+=key[key_pos]
            key_pos=(key_pos+1)%len(key)
        else:
            adjusted=adjusted+char
    return adjusted

def encrypted_vigenere(text, key):
    key.lower()
    text.lower()

    adjusted=adjusted_key(text,key)
    encrypted=""

    for t in range(len(text)):
        char=text[t]
        if 97<=ord(char)<=122:
            shift=ord(adjusted[t])-97
            encryptedText=((shift+ord(char)-97)%26)+97
            encrypted+=chr(encryptedText)
        else:
            encrypted=encrypted+char

    return encrypted

def decrypt_vigenere(text, key):
    key.lower()
    text.lower()

    adjusted=adjusted_key(text,key)
    decrypted=""

    for t in range(len(text)):
        char=text[t]
        if 97<=ord(char)<=122:
            shift=ord(adjusted[t])-97
            decryptedText=((ord(char)-shift-97)%26)+97
            decrypted+=chr(decryptedText)
        else:
            decrypted=decrypted+char

    return decrypted