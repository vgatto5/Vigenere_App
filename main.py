from tkinter import *
import vigenere_cipher

class EncryptionApp(Tk):
    def __init__(self):
        super().__init__()
        self.title('FreeCrypt')
        self.geometry('375x812')
        self.resizable(False, False)

        container = Frame(self)
        container.pack(fill="both", expand=True)




     

class EncryptPage(Frame):
    complete = None
    plaintext = ''
    ciphertext = ''
    key = ''
    def __init__(self, parent):

        Label(self, text="Encrypt", font=("Times New Roman", 56)).pack(pady=20)
        Label(self, text="Enter a message to encrypt:", font=("Times New Roman", 35)).pack(pady=10)

        self.user_plaintext = Entry(self, height=5, font=("Times New Roman", 20))
        self.user_plaintext.pack(pady=10)

        Label(self, text="Enter a key:", font=("Times New Roman", 35)).pack(pady=10)
        self.user_key = Entry(self, font=("Times New Roman", 20))
        self.user_key.pack(pady=10)

        Button(self, text="Encrypt", font=("Times New Roman", 20), command=self.encrypt).pack(pady=10)

        self.outputLabel = Label(self, text='', font=("Times New Roman", 20))
        self.outputLabel.pack(pady = 10)

        self.complete = False

        if (self.complete):
            Label(self, text="Ciphertext:" + self.ciphertext, font=("Times New Roman", 20)).pack(pady=10)


    def encrypt(self):
        plaintext = self.user_plaintext.get().strip()
        key = self.user_key.get().strip()
        if not plaintext or not key:
            self.outputLabel.config(text = 'Error: missing plaintext or key')
            return
        adjustedKey = vigenere_cipher.adjusted_key(plaintext, key)
        cipher_text = vigenere_cipher.encrypted_vigenere(plaintext, key)

        self.ciphertext = cipher_text
        self.complete  = True

        self.outputLabel.config(text='Ciphertext: ' + cipher_text)
    

    #buttons after encryption either "Encrypt Again" or "Decrypt"
    #need to add error handling for empty inputs or invalid keys





    


class DecryptPage(Frame):
    complete = False
    def __init__(self, parent):
        super().__init__()

        Label(self, text="Decrypt", font=("Times New Roman", 56)).pack(pady=20)
        Label(self, text="Enter a message to decrypt:", font=("Times New Roman", 35)).pack(pady=10)

        self.user_ciphertext = Entry(self, height=5, font=("Times New Roman", 20))
        self.user_ciphertext.pack(pady=10)

        Label(self, text="Enter a key:", font=("Times New Roman", 35)).pack(pady=10)
        self.user_key = Entry(self, font=("Times New Roman", 20))
        self.user_key.pack(pady=10)

        Button(self, text="Decrypt", font=("Times New Roman", 20), command=self.decrypt).pack(pady=10)

    def decrypt(self):
        ciphertext = self.user_ciphertext.get().strip()
        key = self.user_key.get().strip()
        adjustedKey = vigenere_cipher.adjusted_key(ciphertext, key)
        plain_text = vigenere_cipher.decrypted_vigenere(ciphertext, key)

        return plain_text
    
    #if (complete):
        #Label(self, text="Plaintext:" + plain_text, font=("Times New Roman", 20)).pack(pady=10)
        
 

    #buttons after encryption either "Decrypt Again" or "Encrypt"




def main():
    main_app = EncryptionApp()
    encryption_page = EncryptPage(main_app)
    decryption_page = DecryptPage(main_app)
    main_app.mainloop()

main()