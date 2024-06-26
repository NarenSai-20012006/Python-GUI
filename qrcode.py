from tkinter import *
import tkinter as tk 
from PIL import ImageTk, Image
import qrcode
import os

a = tk.Tk()

def generate():
    title = text.get()
    name = link.get()
    # Generate and save the QR code
    qr = qrcode.make(name)
    qr.save(f"qrcode/{title}.png")

    # Load and display the QR code image
    img = ImageTk.PhotoImage(Image.open(f"qrcode/{title}.png"))
    c.config(image=img)
    c.image = img  # Keep a reference to avoid garbage collection

# Set window properties
a.title("QR Code Generator")
a.geometry("1000x700")
a.config(bg="green")

# Set window icon
b = PhotoImage(file=r"C:\Users\ANAND\Pictures\Screenshots\Screenshot (43).png")
a.iconphoto(True, b)

# Create and place widgets
c = Label(a, bg="yellow")
c.pack(padx=50, pady=10, side=RIGHT)

Label(a, text="Title", fg="White", bg="black", font=("Arial", 15)).place(x=10, y=10)
text = Entry(a, width=15, font=("Arial", 15))
text.place(x=100, y=10)

Label(a, text="Link", fg="White", bg="black", font=("Arial", 15)).place(x=10, y=40)
link = Entry(a, width=15, font=("Arial", 15))
link.place(x=100, y=40)

Button(a, text="Generate", bg="Blue", fg="white", font=("Arial", 15), command=generate).place(x=10, y=80)

a.mainloop()