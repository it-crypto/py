import random
from tkinter import *


secret = random.randrange(1, 100)
tries = 0
def doGuess():
    global tries
    guess=int(entry.get())
    if guess > secret:
        msg = "TOO HIGH"
        tries=tries+1
    elif guess < secret:
        msg = "TOO LOW"
        tries=tries+1
    else:
        msg = "You got it!!!"
        tries=tries+1
        label2["text"] = "You have had " + str(tries) + " tries."
    #print("the number of tries are",tries)

    label1["text"]=msg

    #clear the guess
    entry.delete(0,4)

def reset():
    global secret
    secret=random.randrange(1, 100)
    label1["text"]="NEW GAME STARTED!!"

root=Tk()

root.title("GUESS THE NUMBER")
root.geometry("400x100")

label=Label(root,text="Welcome to the guessing game!!")
label.pack()

button=Button(root,text="Guess",fg="green",command=doGuess)
button.pack(side=LEFT)

button1=Button(root,text="Reset",fg="red",command=reset)
button1.pack(side=RIGHT)

label1=Label(root,text="Good luck!!")
label1.pack()

label2=Label(root,text="")
label2.pack()

entry=Entry(root,width=5)
entry.pack()

root.mainloop()
