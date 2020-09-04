from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from string import ascii_letters
import random

window = Tk()
window.title("Hangman")

words_list = ["A wkward", "Bagpipes","Banjo","Bungler","Croquet","Crypt","Dwarves","Fervid","Fishhook", "Fjord","Gazebo",
              "Gypsy","Haphazard","Hyphen","Ivory","Jazzy","Jiffy","Jinx","Jukebox","Kayak","Kiosk","Klutz","Memento",
              "Mystify","Numbskull","Ostracize","Oxygen","Pajama","Phlegm","Pixel","Polka","Quad","Quip","Rhythmic",
               "Rogue","Sphinx","Squawk","Swivel","Toady","Twelfth","Unzip","Waxy","Wildebeest","Yacht","Zealous","Zigzag",
              "Zippy","Zombie"]


photos= [ImageTk.PhotoImage(file="pics/h1.JPG"),ImageTk.PhotoImage(file="E:\PycharmProjects\gui.py\pics\h2.JPG"),
         ImageTk.PhotoImage(file="E:\PycharmProjects\gui.py\pics\h3.JPG"),ImageTk.PhotoImage(file="E:\PycharmProjects\gui.py\pics\h4.JPG"),
         ImageTk.PhotoImage(file="E:\PycharmProjects\gui.py\pics\h5.JPG"),ImageTk.PhotoImage(file="E:\PycharmProjects\gui.py\pics\h6.JPG"),
         ImageTk.PhotoImage(file="E:\PycharmProjects\gui.py\pics\h7.JPG"),ImageTk.PhotoImage(file="E:\PycharmProjects\gui.py\pics\h8.JPG")
        ]

photo=[ImageTk.PhotoImage(file="pics/win.JPG")]

def newGame():
    global the_word_withSpaces
    global numberOfGuess
    global the_word
    numberOfGuess = 0
    imgLabel.config(image=photos[0])
    the_word = random.choice(words_list)
    the_word_withSpaces = " ".join(the_word)
    lb1Word.set(" ".join("_" * len(the_word)))

def guess(letter):
    global numberOfGuess
    global the_word
    if numberOfGuess<8:
        txt = list(the_word_withSpaces)
        guessed = list(lb1Word.get())
        if the_word_withSpaces.count(letter) > 0:
            for c in range(len(txt)):
                if txt[c] == letter:
                    guessed[c] = letter
                lb1Word.set("".join(guessed))
                if lb1Word.get() == the_word_withSpaces:
                    imgLabel.config(image=photo[0])
                    messagebox.showinfo("Hangman", "You guessed it!!")

        else:
            numberOfGuess += 1
            imgLabel.config(image=photos[numberOfGuess])
            if numberOfGuess == 7:
                messagebox.showwarning("Hangman","Game Over")
                messagebox.showinfo("Hangman","The correct word is "+the_word)




imgLabel = Label(window)
imgLabel.grid(row=0 ,column=0 ,columnspan=3,padx=10,pady=40)
imgLabel.config(image=photos[0])

lb1Word = StringVar()
Label(window, textvariable=lb1Word ,font=("Consolas 24 bold")).grid(row=0,column=3,columnspan=6,padx=10)

n=0
for c in ascii_letters:
    Button(window,text=c,command=lambda c=c: guess(c) ,font=("Helvetica 18"), width=4).grid(row=1+n//9 ,column=n%9)
    n+=1

Button(window,text="New\nGame", command=lambda:newGame(), font =("Helvetica 10 bold")).grid(row=6,column=7,sticky="NSWE")
newGame()
window.mainloop()