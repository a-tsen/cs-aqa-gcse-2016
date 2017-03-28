from Tkinter import *
from ScrolledText import ScrolledText
import random
import os
heading = ('Courier', 15)
normal = ('Courier', 13)

root = Tk()


def shift(current, new, *args):
    current.grid_remove()
    new.grid()
    if args:
        for i in args:
            try:
                i.delete(0, END)
            except TclError:
                i.delete('0.0', END)
        args[0].focus()


def gen_key():
    key = ''
    for i in range(8):
        char = random.randrange(33, 127)
        char = chr(char)
        key += char
    return key


def offset(key):
    factor = sum(ord(i) for i in key)
    factor /= 8
    return factor - 32


def encryption(key, number):
    text = to_e.get()
    save = e_save.get()
    if os.path.exists(text):
        if os.path.getsize(text) <= 45 * 1024:
            try:
                newtext = open(save, 'w')
                factor = offset(key)
                changed = (option1(text, factor), option2(text, factor))[number]
                newtext.write(changed)
                newtext.close()
                return
            except:
                e_save.delete(0, END)
                e_save.insert(END, 'Invalid file address')
        else:
            to_e.delete(0, END)
            to_e.insert(END, 'File over 45Kb')
    else:
        to_e.delete(0, END)
        to_e.insert(END, 'Invalid filename')


def option1(text, factor):
    plain = open(text, 'r')
    cipher = ''
    for char in plain.read():
        if char not in (' ', '\n'):
            char = ord(char) + factor
            if char > 126:
                char -= 94
            char = chr(char)
        cipher += char
    plain.close()
    return cipher


def option2(text, factor):
    plain = open(text, 'r')
    cipher = ''
    for char in plain.read().replace(' ', ''):
        if char != '\n':
            if (len(cipher.replace('\n', '')) - 5) % 6 == 0:
                cipher += ' '
            char = ord(char) + factor
            if char > 126:
                char -= 94
            char = chr(char)
        cipher += char
    plain.close()
    return cipher


def decryption():
    text = to_d.get()
    key = getkey.get()
    if os.path.exists(text):
        if len(key) == 8:
            cipher = open(text, 'r')
            factor = offset(key)
            plain = ''
            for char in cipher.read():
                if char not in (' ', '\n'):
                    char = ord(char) - factor
                    if char < 33:
                        char += 94
                    char = chr(char)
                plain += char
            cipher.close()
            plaintext.delete('0.0', END)
            plaintext.insert(END, plain)
            return
        getkey.delete(0, END)
        getkey.insert(END, 'Invalid key')
    else:
        to_d.delete(0, END)
        to_d.insert(END, 'Invalid file address')


def en_screen(number=0):
    Label(e_frame, text='Encryption %d' % (number + 1), font=heading).grid(row=0, column=0, columnspan=2, padx=100, pady=10)
    key = Label(e_frame, text=gen_key(), bg='deepskyblue', font=normal)
    key.grid(row=2, column=1, padx=5, pady=5, sticky=W)
    Button(e_frame, text='Encrypt', font=normal, width=12, command=lambda: encryption(key.cget('text'), number)).grid(row=4, column=0, padx=5, pady=5)
    e_frame.grid()
    shift(start, e_frame, to_e, e_save)


e_frame = Frame(root)
Label(e_frame, text='Text file to encrypt:', font=normal).grid(row=1, column=0, padx=5, pady=5, sticky=W)
to_e = Entry(e_frame, width=25, bg='pale goldenrod', font=normal)
to_e.grid(row=1, column=1, padx=5, pady=5, sticky=W)
Label(e_frame, text='Key:', font=normal).grid(row=2, column=0, padx=5, pady=5, sticky=W)
Label(e_frame, text='Save ciphertext to:', font=normal).grid(row=3, column=0, padx=5, pady=5, sticky=W)
e_save = Entry(e_frame, width=25, bg='pale goldenrod', font=normal)
e_save.grid(row=3, column=1, padx=5, pady=5, sticky=W)
Button(e_frame, text='Back to menu', font=normal, width=12, command=lambda: shift(e_frame, start)).grid(row=4, column=1, padx=5, pady=5)

d_frame = Frame(root)
Label(d_frame, text='Decryption', font=heading).grid(row=0, column=0, columnspan=2, padx=100, pady=10)
Label(d_frame, text='Text file to decrypt:', font=normal).grid(row=1, column=0, padx=5, pady=5, sticky=W)
to_d = Entry(d_frame, width=25, bg='pale goldenrod', font=normal)
to_d.grid(row=1, column=1, padx=5, pady=5, sticky=W)
Label(d_frame, text='Key:', font=normal).grid(row=2, column=0, padx=5, pady=5, sticky=W)
getkey = Entry(d_frame, width=25, bg='pale goldenrod', font=normal)
getkey.grid(row=2, column=1, padx=5, pady=5, sticky=W)
Label(d_frame, text='Plaintext:', font=normal).grid(row=3, column=0, padx=5, pady=5, sticky=N+W)
plaintext = ScrolledText(d_frame, height=5, width=29, bg='deepskyblue', wrap=WORD)
plaintext.grid(row=3, column=1, padx=5, pady=5, sticky=W)
Button(d_frame, text='Decrypt', font=normal, width=12, command=decryption).grid(row=4, column=0, pady=10)
Button(d_frame, text='Back to menu', font=normal, width=12, command=lambda: shift(d_frame, start)).grid(row=4, column=1, pady=10)

instruct = Frame(root)
Label(instruct, text="How to use the program", font=heading).grid(row=0, column=0, padx=100, pady=10)
descriptions = Text(instruct, font=normal, width=50, height=15, wrap=WORD)
descriptions.insert(END, "The encrypt options encrypt the text file given by a random 8 character long key. ")
descriptions.insert(END, "The result is then saved to the file address given by the user. ")
descriptions.insert(END, "Remember to include the ending!")
descriptions.insert(END, "\n- 'Encryption 1' does this without changing the length of the words.")
descriptions.insert(END, "\n- 'Encryption 2' groups blocks of 5 characters together and separates them with spaces.")
descriptions.insert(END, "\n\n'Decryption' decrypts the text file name given by the key inputted by the user. ")
descriptions.insert(END, "Like in the encrypt options, the result is saved to the file address given by the user.")
descriptions.insert(END, "\n\nAnd the 'How to use' option is how you got here!")
descriptions.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=W)
Button(instruct, text='Back to menu', font=normal, width=12, command=lambda: shift(instruct, start)).grid(row=2, column=0, pady=5)

start = Frame(root)
start.grid()
Label(start, text='Options', font=heading).grid(row=0, column=0, columnspan=2, padx=50, pady=10)
Button(start, text='Encryption 1', font=normal, width=12, command=en_screen).grid(row=1, column=0, padx=5, pady=5)
Button(start, text='Encryption 2', font=normal, width=12, command=lambda: en_screen(1)).grid(row=1, column=1, padx=5, pady=5)
Button(start, text='Decryption', font=normal, width=12, command=lambda: shift(start, d_frame, to_d, getkey, plaintext)).grid(row=2, column=0, padx=5, pady=5)
Button(start, text='How to use', font=normal, width=12, command=lambda: shift(start, instruct)).grid(row=2, column=1, padx=5, pady=5)

root.mainloop()