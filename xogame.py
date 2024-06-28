from tkinter import*
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox


c=Tk()
c.title("X/0 GAME")
c.geometry("530x380")


chick1 = ttk.Button(c,text=" ",command=lambda:buttonpress(1))
chick1.grid(row=0,column=0,ipadx=50,ipady=50)
chick2 = ttk.Button(c,text=" ",command=lambda:buttonpress(2))
chick2.grid(row=0,column=1,ipadx=50,ipady=50)
chick3 = ttk.Button(c,text=" ",command=lambda:buttonpress(3))
chick3.grid(row=0,column=2,ipadx=50,ipady=50)
chick4 = ttk.Button(c,text=" ",command=lambda:buttonpress(4))
chick4.grid(row=1,column=0,ipadx=50,ipady=50)
chick5 = ttk.Button(c,text=" ",command=lambda:buttonpress(5))
chick5.grid(row=1,column=1,ipadx=50,ipady=50)
chick6 = ttk.Button(c,text=" ",command=lambda:buttonpress(6))
chick6.grid(row=1,column=2,ipadx=50,ipady=50)
chick7 = ttk.Button(c,text=" ",command=lambda:buttonpress(7))
chick7.grid(row=2,column=0,ipadx=50,ipady=50)
chick8 = ttk.Button(c,text=" ",command=lambda:buttonpress(8))
chick8.grid(row=2,column=1,ipadx=50,ipady=50)
chick9 = ttk.Button(c,text=" ",command=lambda:buttonpress(9))
chick9.grid(row=2,column=2,ipadx=50,ipady=50)

def checkwinner():
    if (chick1["text"]=="X" and chick2["text"]=="X" and chick3["text"]=="X" or
        chick4["text"]=="X" and chick5["text"]=="X" and chick6["text"]=="X" or
        chick7["text"]=="X" and chick8["text"]=="X" and chick9["text"]=="X" or
        chick1["text"]=="X" and chick4["text"]=="X" and chick7["text"]=="X" or
        chick2["text"]=="X" and chick5["text"]=="X" and chick8["text"]=="X" or
        chick3["text"]=="X" and chick6["text"]=="X" and chick9["text"]=="X" or
        chick1["text"]=="X" and chick5["text"]=="X" and chick9["text"]=="X" or
        chick3["text"]=="X" and chick5["text"]=="X" and chick7["text"]=="X"):
        messagebox.showinfo("winner","player1 wins")

    elif (chick1["text"]=="O" and chick2["text"]=="O" and chick3["text"]=="O" or
        chick4["text"]=="O" and chick5["text"]=="O" and chick6["text"]=="O" or
        chick7["text"]=="O" and chick8["text"]=="O" and chick9["text"]=="O" or
        chick1["text"]=="O" and chick4["text"]=="O" and chick7["text"]=="O" or
        chick2["text"]=="O" and chick5["text"]=="O" and chick8["text"]=="O" or
        chick3["text"]=="O" and chick6["text"]=="O" and chick9["text"]=="O" or
        chick1["text"]=="O" and chick5["text"]=="O" and chick9["text"]=="O" or
        chick3["text"]=="O" and chick5["text"]=="O" and chick7["text"]=="O"):
         messagebox.showinfo("winner","player2 wins")

player = 1
def buttonpress(button_num):
    global player
    if button_num == 1 and player == 1:
        chick1.config(text="X")
        player = 2
    
    elif button_num == 1 and player ==2:
        chick1.config(text="O")
        player = 1
    
    if button_num == 2 and player == 1:
        chick2.config(text="X")
        player = 2
    
    elif button_num == 2 and player ==2:
        chick2.config(text="O")
        player = 1
    
    if button_num == 3 and player == 1:
        chick3.config(text="X")
        player = 2
    
    elif button_num == 3 and player ==2:
        chick3.config(text="O")
        player = 1
    
    if button_num == 4 and player == 1:
        chick4.config(text="X")
        player = 2
    
    elif button_num == 4 and player ==2:
        chick4.config(text="O")
        player = 1
    
    if button_num == 5 and player == 1:
        chick5.config(text="X")
        player = 2
    
    elif button_num == 5 and player ==2:
        chick5.config(text="O")
        player = 1
    
    if button_num == 6 and player == 1:
        chick6.config(text="X")
        player = 2
    
    elif button_num == 6 and player ==2:
        chick6.config(text="O")
        player = 1
    
    if button_num == 7 and player == 1:
        chick7.config(text="X")
        player = 2
    
    elif button_num == 7 and player ==2:
        chick7.config(text="O")
        player = 1
    
    if button_num == 8 and player == 1:
        chick8.config(text="X")
        player = 2
    
    elif button_num == 8 and player ==2:
        chick8.config(text="O")
        player = 1
    
    if button_num == 9 and player == 1:
        chick9.config(text="X")
        player = 2
    
    elif button_num == 9 and player ==2:
        chick9.config(text="O")
        player = 1
    
    checkwinner()
     
c.mainloop()