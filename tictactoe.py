# tictactoes
# play against computer
# player can choose symbol
# X's goes first
# computer chooses random, vacant space each turn
# check for three in a row
# display win/lose message

# 9 buttons, 1 for each square

# TODO:
# function to interpret button presses
# computer AI
# check for wins

# make array of dynamic symbols
from array import *

# get GUI
import tkinter
from tkinter import Entry, Frame, Button, Label, StringVar, END

# the main GUI
root = tkinter.Tk()
root.geometry("300x200")
root.title("tictactoes")

def dummyFunc():
    print()

data = [[' ', ' ', ' '], 
        [' ', ' ', ' '], 
        [' ', ' ', ' ']]

def clickButton():
    button1=Button(root, text="button1")
    button1.grid(row=0,column=0, padx = 20, pady = 20)

    button2=Button(root, text="button2")
    button2.grid(row=0,column=1, padx = 20, pady = 20)

    button3=Button(root, text="button3")
    button3.grid(row=0,column=2, padx = 20, pady = 20)

    button4=Button(root, text="button4")
    button4.grid(row=1,column=0, padx = 20, pady = 20)

    button5=Button(root, text="button5")
    button5.grid(row=1,column=1, padx = 20, pady = 20)

    button6=Button(root, text="button5")
    button6.grid(row=1,column=2, padx = 20, pady = 20)

    button7=Button(root, text="button5")
    button7.grid(row=2,column=0, padx = 20, pady = 20)

    button8=Button(root, text="button5")
    button8.grid(row=2,column=1, padx = 20, pady = 20)

    button9=Button(root, text="button5")
    button9.grid(row=2,column=2, padx = 20, pady = 20)

clickButton()

root.mainloop()
