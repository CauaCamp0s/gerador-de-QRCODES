# import tkinter as Tk
from tkinter import *
import pyqrcode
from PIL import Image, ImageTk

root = Tk()
root.title("QRCode Generator")
root.geometry('500x550')


def create_code():
    text = my_entry.get()
    qr_code = pyqrcode.create(text)
    qr_code_image = qr_code.png('qr_code.png', scale=8)
    qr_code_image = Image.open('qr_code.png')
    qr_code_image = ImageTk.PhotoImage(qr_code_image)
    my_label.config(image=qr_code_image)
    my_label.image = qr_code_image


def clear_all():
    my_entry.delete(0, END)
    my_label.config(image='')


# gerando o GUI
my_entry = Entry(root, font=("helvetica", 16))
my_entry.pack(pady=20)

my_button = Button(root, text='criar QRCode',  command=create_code)
my_button.pack(pady=20)

my_button2 = Button(root, text='limpar',  command=clear_all)
my_button2.pack()

my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()