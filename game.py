from tkinter import *
import random

number = random.randrange(100) + 1
tries = 0


class Application(Frame):
    """ GUI application which can retrieve an auto number to guess. """

    def __init__(self, master):
        """ Initialize the frame. """
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create button, text, and entry widgets. """
        """ Instruction Label """
        # Create instruction label for Program
        self.inst_lbl = Label(self, text="Follow the Steps")
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=W)
        """ Player Name """
        # Create label for name
        self.name_lbl = Label(self, text="Player Name: ")
        self.name_lbl.grid(row=1, column=0, sticky=W)

        # Create entry widget to accept name
        self.name_ent = Entry(self)
        self.name_ent.grid(row=1, column=1, sticky=W)
        """ Guess Input """
        # Create label for entering Guess
        self.guess_lbl = Label(self, text="Enter your Guess.")
        self.guess_lbl.grid(row=2, column=0, sticky=W)
        # Create entry widget to accept Guess
        self.guess_ent = Entry(self)
        self.guess_ent.grid(row=2, column=1, sticky=W)
        # Create a space
        self.gap1_lbl = Label(self, text=" ")
        self.gap1_lbl.grid(row=3, column=0, sticky=W)
        """ Submit Button """

        # Create submit button
        self.submit_bttn = Button(self, text="Submit", command=self.reveal)
        self.submit_bttn.grid(row=6, column=0, sticky=W)
        # Create a space
        self.gap2_lbl = Label(self, text=" ")
        self.gap2_lbl.grid(row=7, column=0, sticky=W)
        """ RESET """

        # Create submit button
        self.reset_bttn = Button(self, text="Reset", command=self.reveal)
        self.reset_bttn.grid(row=6, column=1, sticky=W)
        """ Display """
        # Create text widget to display welcome_msg
        self.display1_txt = Text(self, width=45, height=1, wrap=WORD)
        self.display1_txt.grid(row=8, column=0, columnspan=2, sticky=W)
        # Create text widget to display guess_msg
        self.display2_txt = Text(self, width=45, height=1, wrap=WORD)
        self.display2_txt.grid(row=9, column=0, columnspan=2, sticky=W)
        # Create text widget to display result_msg
        self.display3_txt = Text(self, width=45, height=2, wrap=WORD)
        self.display3_txt.grid(row=10, column=0, columnspan=2, sticky=W)
        # Create text widget to display tries_msg
        self.display4_txt = Text(self, width=45, height=2, wrap=WORD)
        self.display4_txt.grid(row=11, column=0, columnspan=2, sticky=W)

    def reveal(self):
        global tries
        name = self.name_ent.get()
        guess = self.guess_ent.get()
        if int(guess) > int(number):
            result_msg = "Lower ..."
            tries += 1
        if int(guess) < int(number):
            result_msg = "Higher ..."
            tries += 1
        if int(guess) == int(number):
            result_msg = "You got it."
            tries += 1
        welcome_msg = "Welcome " + name
        guess_msg = " Your guess was: " + guess
        tries_msg = "You have had " + str(tries) + " tries."
        if tries > 10:
            welcome_msg = "End of Game."
            guess_msg = "You had too many tires."
            result_msg = " "
            tries_msg = " "
        # Display
        self.display1_txt.delete(0.0, END)
        self.display1_txt.insert(0.0, welcome_msg)
        self.display2_txt.delete(0.0, END)
        self.display2_txt.insert(0.0, guess_msg)
        self.display3_txt.delete(0.0, END)
        self.display3_txt.insert(0.0, result_msg)
        self.display4_txt.delete(0.0, END)
        self.display4_txt.insert(0.0, tries_msg)


# Main manager
root = Tk()
root.title("Guessing Game")
root.geometry("300x225")
app = Application(root)
root.mainloop()