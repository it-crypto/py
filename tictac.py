from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from random import randint

#Global variables
ActivePlayer=1
p1=[]
p2=[]
root=Tk()
root.title("Tic Tac Toe : Player 1")
style = ttk.Style()


# Add Buttons
but = ttk.Button(root,text='')
but.grid(row=0,column=0,sticky='snew',ipadx=40,ipady=40)
but.config(command=lambda : ButtonClick(1))

but1 = ttk.Button(root,text='')
but1.grid(row=0,column=1,sticky='snew',ipadx=40,ipady=40)
but1.config(command=lambda : ButtonClick(2))

but2 = ttk.Button(root,text='')
but2.grid(row=0,column=2,sticky='snew',ipadx=40,ipady=40)
but2.config(command=lambda : ButtonClick(3))

but3 = ttk.Button(root,text='')
but3.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)
but3.config(command=lambda : ButtonClick(4))

but4 = ttk.Button(root,text='')
but4.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)
but4.config(command=lambda : ButtonClick(5))

but5 = ttk.Button(root,text='')
but5.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)
but5.config(command=lambda : ButtonClick(6))

but6 = ttk.Button(root,text='')
but6.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
but6.config(command=lambda : ButtonClick(7))

but7 = ttk.Button(root,text='')
but7.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
but7.config(command=lambda : ButtonClick(8))

but8 = ttk.Button(root,text='')
but8.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
but8.config(command=lambda : ButtonClick(9))


def ButtonClick(id):
    #print("ID:{}".format(id))
    global ActivePlayer
    global p1
    global p2
    if(ActivePlayer==1):
        SetLayout(id,"X")
        p1.append(id)
        root.title("TIC TAC TOE:Player 2")
        ActivePlayer=2
        print("P1:{}".format(p1))
        #AutoPlay()
    elif(ActivePlayer==2):
        SetLayout(id, "O")
        p2.append(id)
        root.title("TIC TAC TOE:Player 1")
        ActivePlayer=1
        print("P2:{}".format(p2))
    CheckWinner()


def SetLayout(id,PlayerSymbol):
    if id==1:
        but.config(text=PlayerSymbol)
        but.state(['disabled'])
    elif id==2:
        but1.config(text=PlayerSymbol)
        but1.state(['disabled'])
    elif id==3:
        but2.config(text=PlayerSymbol)
        but2.state(['disabled'])
    elif id == 4:
        but3.config(text=PlayerSymbol)
        but3.state(['disabled'])
    elif id==5:
        but4.config(text=PlayerSymbol)
        but4.state(['disabled'])
    elif id == 6:
        but5.config(text=PlayerSymbol)
        but5.state(['disabled'])
    elif id==7:
        but6.config(text=PlayerSymbol)
        but6.state(['disabled'])
    elif id==8:
        but7.config(text=PlayerSymbol)
        but7.state(['disabled'])
    elif id==9:
        but8.config(text=PlayerSymbol)
        but8.state(['disabled'])


def CheckWinner():
    Winner=-1
    if( (1 in p1) and (2 in p1) and (3 in p1) ):
        Winner=1
    if ((1 in p2) and (2 in p2) and (3 in p2)):
        Winner=2

    if ((4 in p1) and (5 in p1) and (6 in p1)):
        Winner = 1
    if ((4 in p2) and (5 in p2) and (6 in p2)):
        Winner = 2

    if ((7 in p1) and (8 in p1) and (9 in p1)):
        Winner = 1
    if ((7 in p2) and (8 in p2) and (9 in p2)):
        Winner = 2

    if ((1 in p1) and (4 in p1) and (7 in p1)):
        Winner = 1
    if ((1 in p2) and (4 in p2) and (7 in p2)):
        Winner = 2

    if ((2 in p1) and (5 in p1) and (8 in p1)):
        Winner = 1
    if ((2 in p2) and (5 in p2) and (8 in p2)):
        Winner = 2

    if ((3 in p1) and (6 in p1) and (9 in p1)):
        Winner = 1
    if ((3 in p2) and (6 in p2) and (9 in p2)):
        Winner = 2

    if ((1 in p1) and (5 in p1) and (9 in p1)):
        Winner = 1
    if ((1 in p2) and (5 in p2) and (9 in p2)):
        Winner = 2

    if ((3 in p1) and (5 in p1) and (7 in p1)):
        Winner = 1
    if ((3 in p2) and (5 in p2) and (7 in p2)):
        Winner = 2

    if Winner==1:
        messagebox.showinfo(title="Congrats",message="Player 1 is the Winner")
    elif Winner==2:
        messagebox.showinfo(title="Congrats", message="Player 2 is the Winner")


def AutoPlay():
    global p1
    global p2
    EmptyCells=[]
    for cell in range(9):
        if(not ( ( cell+1 in p1) or (cell+1 in p2 ))):
            EmptyCells.append(cell+1)
    RandIndex=randint(0,len(EmptyCells)-1)
    ButtonClick(EmptyCells[RandIndex])








root.mainloop()