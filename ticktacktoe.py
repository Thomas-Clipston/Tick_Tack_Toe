from ast import Delete
from cProfile import label
from cgitb import text
from doctest import master
from inspect import _void
from itertools import count
from multiprocessing import BufferTooShort
from operator import truediv
from re import X
import tkinter as tk
from tkinter import CENTER, END, Button, Toplevel, font
from turtle import left, width
from click import command

window = tk.Tk()
window.resizable(width=False, height=False)


window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.columnconfigure(2,weight=1)


 
    

def winnerscreen(Win):
    winner = Toplevel(master)
    winner.geometry("200x200")
    
    results = tk.Label(winner,text="Therefore the winner was ")
    results2 = tk.Label(winner,text=Win+"\n\n\n",font=40)
    results.pack()
    results2.pack()
    
    def quit():
        window.destroy()

    def playagain():
        global count
        count = 0
        window.deiconify()
        r11["text"] = ""
        r12["text"] = ""
        r13["text"] = ""
        r21["text"] = ""
        r22["text"] = ""
        r23["text"] = ""
        r31["text"] = ""
        r32["text"] = ""
        r33["text"] = ""
        winner.withdraw()


    exit = tk.Button(winner,text="Quit",command=quit)
    Playagain = tk.Button(winner,text="Playagain",command=playagain)
    exit.pack()
    Playagain.pack()
    
    
count = 0
click = False
def switch(r):
    global count
    global click
    if click == False and r["text"] == "":
        r.config(text="O")
        click = True
        count = count+1
    if click == True and r["text"] == "":
       r.config(text="X")
       click = False
       count = count+1
    print(count)
  

    if r11["text"] == "X" and r21["text"] == "X" and r31["text"] == "X" or r12["text"] == "X" and r22["text"] == "X" and r32["text"] == "X" or r13["text"] == "X" and r23["text"] == "X" and r33["text"] == "X" or r11["text"] == "X" and r12["text"] == "X" and r13["text"] == "X" or r21["text"] == "X" and r22["text"] == "X" and r23["text"] == "X" or r31["text"] == "X" and r32["text"] == "X" and r33["text"] == "X" or r11["text"] == "X" and r22["text"] == "X" and r33["text"] == "X" or r31["text"] == "X" and r22["text"] == "X" and r13["text"] == "X" :
        window.withdraw()
        winnerscreen("X.")
    elif r11["text"] == "O" and r21["text"] == "O" and r31["text"] == "O" or r12["text"] == "O" and r22["text"] == "O" and r32["text"] == "O" or r13["text"] == "O" and r23["text"] == "O" and r33["text"] == "O" or r11["text"] == "O" and r12["text"] == "O" and r13["text"] == "O" or r21["text"] == "O" and r22["text"] == "O" and r23["text"] == "O" or r31["text"] == "O" and r32["text"] == "O" and r33["text"] == "O" or r11["text"] == "O" and r22["text"] == "O" and r33["text"] == "O" or r31["text"] == "O" and r22["text"] == "O" and r13["text"] == "O" :
        window.withdraw()
        winnerscreen("O.")
    elif count == 9:
        window.withdraw()
        winnerscreen("tie.")




r11 = tk.Button(window,width=10,height=5,bg="green",command=lambda:switch(r11))
r11.grid(column=0,row=0)
r21 = tk.Button(window,width=10,height=5,bg="green",command=lambda:switch(r21))
r21.grid(column=1,row=0)
r31 = tk.Button(window,width=10,height=5,bg="green",command=lambda:switch(r31))
r31.grid(column=2,row=0)

r12 = tk.Button(window,width=10,height=5,bg="green",command=lambda:switch(r12))
r12.grid(column=0,row=1)
r22 = tk.Button(window,width=10,height=5,bg="green",command=lambda:switch(r22))
r22.grid(column=1,row=1)
r32 = tk.Button(window,width=10,height=5,bg="green",command=lambda:switch(r32))
r32.grid(column=2,row=1)

r13 = tk.Button(window,width=10,height=5,bg="green",command=lambda:switch(r13))
r13.grid(column=0,row=2)
r23 = tk.Button(window,width=10,height=5,bg="green",command=lambda:switch(r23))
r23.grid(column=1,row=2)
r33 = tk.Button(window,width=10,height=5,bg="green",command=lambda:switch(r33))
r33.grid(column=2,row=2)



window.mainloop()

