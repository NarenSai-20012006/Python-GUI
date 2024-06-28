from tkinter import *
import tkinter as tk

def button_press(key):
    if key == "=":
        result = eval(c.get())
        c.delete(0, END)
        c.insert(END, str(result))
        
    elif key == "clear":
        c.delete(0, END)
    else:
        c.insert(END, key)

a=tk.Tk()
a.geometry("255x480")
a.title("CALCULATOR")
a.config(bg="light blue")
b=PhotoImage(file=r"C:\Users\ANAND\Downloads\calculator-icon-8175.png")
a.iconphoto(False,b)
c=Entry(a, font=40,bg="light blue")
c.grid(row=0,column=0,ipadx=35,ipady=30)

d=Button(a,text="1", command=lambda: button_press("1"),bg="black",fg="gold",activebackground="green",activeforeground="red")
d.grid(row=5,column=0,ipadx=34,ipady=20,sticky="w")
e=Button(a,text="4", command=lambda: button_press("4"),bg="black",fg="gold",activebackground="green",activeforeground="red")
e.grid(row=6,column=0,ipadx=34,ipady=20,sticky="w")
f=Button(a,text="7", command=lambda: button_press("7"),bg="black",fg="gold",activebackground="green",activeforeground="red")
f.grid(row=7,column=0,ipadx=34,ipady=20,sticky="w")
g=Button(a,text="%", command=lambda: button_press("/"),bg="black",fg="gold",activebackground="green",activeforeground="red")
g.grid(row=8,column=0,ipadx=32,ipady=20,sticky="w")
z=Button(a,text="+", command=lambda: button_press("+"),bg="black",fg="gold",activebackground="green",activeforeground="red")
z.grid(row=9,column=0,ipadx=33,ipady=20,sticky="w")

h=Button(a,text="2", command=lambda: button_press("2"),bg="black",fg="gold",activebackground="green",activeforeground="red")
h.grid(row=5,column=0,ipadx=34,ipady=20,sticky="n")
i=Button(a,text="5", command=lambda: button_press("5"),bg="black",fg="gold",activebackground="green",activeforeground="red")
i.grid(row=6,column=0,ipadx=34,ipady=20,sticky="n")
j=Button(a,text="8", command=lambda: button_press("8"),bg="black",fg="gold",activebackground="green",activeforeground="red")
j.grid(row=7,column=0,ipadx=34,ipady=20,sticky="n")
k=Button(a,text="X", command=lambda: button_press("*"),bg="black",fg="gold",activebackground="green",activeforeground="red")
k.grid(row=8,column=0,ipadx=33,ipady=20,sticky="n")
y=Button(a,text="-", command=lambda: button_press("-"),bg="black",fg="gold",activebackground="green",activeforeground="red")
y.grid(row=9,column=0,ipadx=34,ipady=20,sticky="n")

l=Button(a,text="3", command=lambda: button_press("3"),bg="black",fg="gold",activebackground="green",activeforeground="red")
l.grid(row=5,column=0,ipadx=34,ipady=20,sticky="e")
m=Button(a,text="6", command=lambda: button_press("6"),bg="black",fg="gold",activebackground="green",activeforeground="red")
m.grid(row=6,column=0,ipadx=34,ipady=20,sticky="e")
n=Button(a,text="9", command=lambda: button_press("9"),bg="black",fg="gold",activebackground="green",activeforeground="red")
n.grid(row=7,column=0,ipadx=34,ipady=20,sticky="e")
o=Button(a,text="0", command=lambda: button_press("0"),bg="black",fg="gold",activebackground="green",activeforeground="red")
o.grid(row=8,column=0,ipadx=34,ipady=20,sticky="e")
x=Button(a,text="clear", command=lambda: button_press("clear"),bg="black",fg="gold",activebackground="green",activeforeground="red")
x.grid(row=9,column=0,ipadx=24,ipady=20,sticky="e")
x=Button(a,text="=", command=lambda: button_press("="),bg="black",fg="gold",activebackground="green",activeforeground="red")
x.grid(row=10,column=0,ipadx=32,ipady=20,sticky="s")

a.mainloop()