from tkinter import*

class Buttons:
    def __init__(self,master):
        frame = Frame (master)
        frame.pack()
        self.printButton = Button(frame, text="print message",command=self.printMessage)
        self.printButton.pack(side=LEFT)
        self.quitButton=Button(frame,text="Quit",command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("woreeee!!")
"""theLabel = Label(root, text="hi welcome")
theLabel.pack()"""
"""topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Click me", fg="red")
button2 = Button(topFrame, text="submit", fg="blue")
button3 = Button(bottomFrame, text="reset", fg="green")
button4 = Button(bottomFrame, text="try it", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM) """

"""one = Label(root,text="One", bg="red", fg="white")
one.pack()
two = Label(root,text="2", bg="green", fg="black")
two.pack(fill=X)
three = Label(root,text="One", bg="blue", fg="white")
three.pack(side=LEFT,fill=Y)"""

"""label1=Label(root,text="Name")
label2=Label(root,text="Password")
entry1=Entry(root)
entry2=Entry(root)
label1.grid(row=0,sticky=E)
label2.grid(row=1,sticky=E)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
c=Checkbutton(root,text="keep me logged in")
c.grid(columnspan=2) """

"""def printName(event):
    print("hello olaaa!!")

#button1= Button(root,text="print",command=printName)
button1 = Button(root, text="Print")
button1.bind("<Button-1>",printName)
button1.pack()"""

"""def leftClick(event):
    print("left")

def middleClick(event):
    print("middle")

def rightClick(event):
    print("right")
frame  = Frame(root, width=300 ,height=250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)
frame.pack()"""

root=Tk()
b=Buttons(root)
root.mainloop()