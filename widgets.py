from tkinter import *
from tkinter.ttk import *
from turtle import title
import vigenere_cipher

TK_SILENCE_DEPRECATION = 1


def main():
    root = Tk() #instantiate instance of window
    root.title("Free Crypt")
    root.geometry('375x812')
    root.config(bg="#60C8D8")
    icon = PhotoImage(file='logo.png')
    root.iconphoto(True, icon)
    
    notebook = Notebook(root)
    notebook.pack(expand=True, fill='both')

    frameEncrypt = Frame(notebook, width='375', height='812')
    frameDecrypt = Frame(notebook, width='375', height='812')
   
    titleEncrypt = Label(frameEncrypt, text="Vigenère Cipher", font=("Times New Roman", 45))
    titleEncrypt.pack()
    titleDecrypt = Label(frameDecrypt, text="Vigenère Cipher", font=("Times New Roman", 45))
    titleDecrypt.pack()





   
    frameEncrypt.pack(fill='both', expand=True)
    frameDecrypt.pack(fill='both', expand=True) 
    
    notebook.add(frameEncrypt, text='Encrypt')
    notebook.add(frameDecrypt, text='Decrypt')



    root.mainloop()


'''title = Label(
    root,
    text="Vigenère Cipher",
    font=("Times New Roman", 52),
    fg="white",
    pady='30',
    bg="#60C8D8",
)
title.pack(pady=20)



encrypt_button = Button(
    root,
    text="Encrypt",
    font=("Times New Roman", 24),
    fg="white",
    bg="#60C8D8",
    #command=lambda: set_mode(True)
)
encrypt_button.pack(pady=10)

decrypt_button = Button(
    root,
    text="Decrypt",
    font=("Times New Roman", 24),
    fg="white",
    bg="#60C8D8",
    #command=lambda: set_mode(False)
)
decrypt_button.pack(pady=10)


#end of mode selection sequence



plaintext_label = Label(
    root,
    text="Enter Your Plaintext:",
    font=("Times New Roman", 24),
    fg="white",
    bg="#60C8D8",
)
plaintext_label.pack(pady=5)

PLAINTEXT_ENTRYBOX = Text(
    root,
    bg='white',
    fg='black',
    font=('Times New Roman', 24),
    width=25,
    height=2,
    border=0,
    xscrollcommand=True,
    yscrollcommand=True,

    insertborderwidth=0
)
PLAINTEXT_ENTRYBOX.pack()

key_label = Label(
    root,
    text="Enter Key:",
    font=("Times New Roman", 24),
    fg="white",
    bg="#60C8D8",
)
key_label.pack(pady=5)

KEY_ENTRYBOX = Text(
    root,
    bg='white',
    fg='black',
    font=('Times New Roman', 24),
    width=25,
    height=2,
    border=0,
    xscrollcommand=True,
)'''



#USER_PLAINTEXT = PLAINTEXT_ENTRYBOX.get()
#USER_KEY = KEY_ENTRYBOX.get()
#if(mode == "encrypt"):
#vigenere_cipher.encrypted_vigenere()

 #places window on screen and listens for events
 
main()