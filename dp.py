from tkinter import*


def doNothing():
    print("ok okaaaay")

root= Tk()
menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="Now project!!!",command=doNothing)
subMenu.add_command(label="N!!",command=doNothing)
subMenu.add_command(label="No!",command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit",command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command()

#*******Toolbar*********
toolbar=Frame(root,bg="blue")
insertButt = Button(toolbar,text="Insert Image",command=doNothing)
insertButt.pack(side=LEFT,padx=2,pady=2)
printButt = Button(toolbar,text="Insert",command=doNothing)
printButt.pack(side=LEFT,padx=2,pady=2)

toolbar.pack(side=TOP,fill=X)

#*******Status bar *************
status = Label(root,text="prepare",bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)
root.mainloop()