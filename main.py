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
    def __init__(self, parent, controller):
        super().__init__()
        self.controller = controller

        Label(self, text="Encrypt", font=("Times New Roman", 56)).pack(pady=20)
        Label(self, text="Enter a message to encrypt:", font=("Times New Roman", 35)).pack(pady=10)

        self.user_plaintext = Entry(self, height=5, font=("Times New Roman", 20))
        self.user_plaintext.pack(pady=10)

        Label(self, text="Enter a key:", font=("Times New Roman", 35)).pack(pady=10)
        self.user_key = Entry(self, font=("Times New Roman", 20))
        self.user_key.pack(pady=10)

        Button(self, text="Encrypt", font=("Times New Roman", 20), command=self.encrypt).pack(pady=10)

    def encrypt(self):
        plaintext = self.user_plaintext.get().strip()
        key = self.user_key.get().strip()
        adjustedKey = vigenere_cipher.adjusted_key(plaintext, key)
        cipher_text = vigenere_cipher.encrypted_vigenere(plaintext, key)

        return cipher_text



    


class DecryptPage(Frame):
    def __init__(self, parent, controller):
        super().__init__()





def main():
    main_app = EncryptionApp()
    encryption_page = EncryptPage(main_app)
    decryption_page = DecryptPage(main_app)
    main_app.mainloop()

main()