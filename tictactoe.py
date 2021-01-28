# tictactoes
# play against computer
# player can choose symbol
# X's goes first
# computer chooses random, vacant space each turn
# check for three in a row
# display win/lose message

# 9 buttons, 1 for each square

# TODO:
# interpretButton is executing automatically, not on click :((
# function to interpret button presses
# computer AI
# check for wins

# make array of dynamic symbols
from array import *

# get GUI
from tkinter import *

# the main GUI
root = Tk()
root.geometry("300x200")
root.title("tictactoes")

frame = Frame(root)
frame.grid(row = 0,  column = 0)

playerSymbol = ""
CPUSymbol = ""
v = IntVar()

def interpretSymbol():
   # selection = "You selected the option " + str(v.get())
   # label.config(text = selection)  
    playerSymbol = str(v.get())
    CPUSymbol = str(v.get() % 2 + 1)
    print(playerSymbol)
    print(CPUSymbol)
    frame.destroy()
    clickButton()

def chooseSymbol():
    label = Label(frame, 
            text = """Choose a symbol""",
            justify = LEFT,
            padx = 20)
    label.grid(row = 0,column = 0, padx = 20, pady = 20)
    R1 = Radiobutton(frame, 
            text = "X",
            padx = 20, 
            variable = v, 
            value = 1,
            command = interpretSymbol)
    R1.grid(row = 1,column = 0, padx = 20, pady = 20)
    R2 = Radiobutton(frame, 
            text = "O",
            padx = 20, 
            variable = v, 
            value = 2,
            command = interpretSymbol)
    R2.grid(row = 2,column = 0, padx = 20, pady = 20)

chooseSymbol()

# when a button is pressed go here and change it to X or O
def interpretButton(row, column):
    buttonRow = row
    buttonColumn = column
    print(buttonRow)
    print(buttonColumn)
    # info = button.grid_info()
    # print((info["row"], info["column"]))
    # data[info["row"]][info["column"]]
    

data = [[' ', ' ', ' '], 
        [' ', ' ', ' '], 
        [' ', ' ', ' ']]

buttonRow = 0
buttonColumn = 0

def clickButton():
    button1 = Button(root, text = " ", command = interpretButton(0, 0))
    button1.grid(row = 0, column = 0, padx = 20, pady = 20)
    
    button2=Button(root, text = " ", command = interpretButton(0, 1))
    button2.grid(row = 0, column = 1, padx = 20, pady = 20)

    button3=Button(root, text = " ", command = interpretButton(0, 2))
    button3.grid(row = 0, column = 2, padx = 20, pady = 20)

    button4=Button(root, text = " ", command = interpretButton(1, 0))
    button4.grid(row = 1, column = 0, padx = 20, pady = 20)

    button5=Button(root, text = " ", command = interpretButton(1, 1))
    button5.grid(row = 1, column = 1, padx = 20, pady = 20)

    button6=Button(root, text = " ", command = interpretButton(1, 2))
    button6.grid(row = 1, column = 2, padx = 20, pady = 20)

    button7=Button(root, text = " ", command = interpretButton(2, 0))
    button7.grid(row = 2, column = 0, padx = 20, pady = 20)

    button8=Button(root, text = " ", command = interpretButton(2, 1))
    button8.grid(row = 2, column = 1, padx = 20, pady = 20)

    button9=Button(root, text = " ", command = interpretButton(2, 2))
    button9.grid(row = 2, column = 2, padx = 20, pady = 20)

root.mainloop()
