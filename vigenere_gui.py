from tkinter import *
import vigenere_cipher
import widgets

root = Tk()
root.geometry('375x812')
root.title("Free Crypt")
icon = PhotoImage(file='logo.png')
root.iconphoto(True, icon)
root.config(bg="#60C8D8")

widgets.plaintext_label.pack(pady=20)

root.mainloop()


