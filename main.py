from tkinter import *
import vigenere_cipher

class EncryptionApp(Tk):
    def __init__(self):
        super().__init__()
        self.title('FreeCrypt')
        self.geometry('375x812')
        self.resizable(False, False)

        
        