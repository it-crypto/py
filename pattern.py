from tkinter import *
import re


def compare(rna):
    corna_protein = "auuaaagguuuauaccuucccagguaacaaaccaaccaacuuucgaucucuuguagaucuguucucuaaacgaacuuuaaaaucuguguggcugucacucggcugcaugcuuagugcacucacgcaguauaauuaauaacuaauuacugucguugacaggacacgaguaacucgucuaucuucugcaggcugcuuacgguuucguccguguugcagccgaucaucagcacaucuagguuucguccgggugugaccgaaagguaag"
    if (rna == corna_protein):
        print("positive")

    else:
        print("negative")


def validation_check():
    input_rna = input("input the  RNA sequence: ").upper()
    if re.match(r"^[AUGCT]+$", input_rna):
        print("Correct! it is a  valid sequence.")
        print(compare(input_rna))
    else:
        print("not valid check the sequence and try again.")
        validation_check()


# for checking if pattern consists of a,u,g,c or not
validation_check()

root=Tk()

root.title("Pattern matching")
root.geometry("600x200")

C_name = Entry(root, width=30)
C_name.grid(row=0, column=1, padx=20)

C_name_label = Label(root, text="enter the string")
C_name_label.grid(row=0, column=0)

submit_btn = Button(root, text="pattern matching ",command=validation_check())
submit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)



root.mainloop()