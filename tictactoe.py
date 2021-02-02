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

import random

# the main GUI
root = Tk()
root.geometry("300x200")
root.title("tictactoes")

initFrame = Frame(root)
initFrame.grid(row = 0,  column = 0)
frame = Frame(root)
frame.grid(row = 0,  column = 0)

playerSymbol = "initPS"
CPUSymbol = "initCS"
v = IntVar()
turn = 0 # keeps track of what turn it is

def interpretSymbol():
    # selection = "You selected the option " + str(v.get())
    # label.config(text = selection)
    initFrame.destroy()
    selected = v.get()
    # playerSymbol = str(v.get())
    # CPUSymbol = str(v.get() % 2 + 1)
    if(selected == 1):
        global playerSymbol
        playerSymbol = "X"
        global CPUSymbol
        CPUSymbol = "O"
    else:
        global playerSymbol
        playerSymbol = "O"
        global CPUSymbol
        CPUSymbol = "X"
    print(playerSymbol)
    print(CPUSymbol)
    clickButton()

def chooseSymbol():
    label = Label(initFrame, 
            text = """Choose a symbol""",
            justify = LEFT,
            padx = 20)
    label.grid(row = 0, column = 0, padx = 20, pady = 20)
    R1 = Radiobutton(initFrame, 
            text = "X",
            padx = 20, 
            variable = v, 
            value = 1,
            command = interpretSymbol)
    R1.grid(row = 1, column = 0, padx = 20, pady = 20)
    R2 = Radiobutton(initFrame, 
            text = "O",
            padx = 20, 
            variable = v, 
            value = 2,
            command = interpretSymbol)
    R2.grid(row = 2, column = 0, padx = 20, pady = 20)

chooseSymbol()

# when a button is pressed go here and change it to X or O
def interpretButton(row, column):
    buttonRow = row
    buttonColumn = column
    print(buttonRow)
    print(buttonColumn)
    data[row][column] = playerSymbol
    updateGUI(row, column)
    # info = button.grid_info()
    # print((info["row"], info["column"]))
    # data[info["row"]][info["column"]]
    
data = [[' ', ' ', ' '], 
        [' ', ' ', ' '], 
        [' ', ' ', ' ']]

buttonRow = 0
buttonColumn = 0

def clickButton():
    button1 = Button(frame, text = " ", command = lambda : interpretButton(0, 0))
    button1.grid(row = 0, column = 0, padx = 20, pady = 20)
    
    button2=Button(frame, text = " ", command = lambda : interpretButton(0, 1))
    button2.grid(row = 0, column = 1, padx = 20, pady = 20)

    button3=Button(frame, text = " ", command = lambda : interpretButton(0, 2))
    button3.grid(row = 0, column = 2, padx = 20, pady = 20)

    button4=Button(frame, text = " ", command = lambda : interpretButton(1, 0))
    button4.grid(row = 1, column = 0, padx = 20, pady = 20)

    button5=Button(frame, text = " ", command = lambda : interpretButton(1, 1))
    button5.grid(row = 1, column = 1, padx = 20, pady = 20)

    button6=Button(frame, text = " ", command = lambda : interpretButton(1, 2))
    button6.grid(row = 1, column = 2, padx = 20, pady = 20)

    button7=Button(frame, text = " ", command = lambda : interpretButton(2, 0))
    button7.grid(row = 2, column = 0, padx = 20, pady = 20)

    button8=Button(frame, text = " ", command = lambda : interpretButton(2, 1))
    button8.grid(row = 2, column = 1, padx = 20, pady = 20)

    button9=Button(frame, text = " ", command = lambda : interpretButton(2, 2))
    button9.grid(row = 2, column = 2, padx = 20, pady = 20)


def updateGUI(row, column):
    turns += 1
    # player moves
    for player in frame.grid_slaves():
        if int(player.grid_info()["row"]) == row and int(player.grid_info()["column"]) == column:
            player.grid_forget()
            strVar = StringVar()
            strVar.set(playerSymbol)
            playerText = Label(frame, textvariable = strVar)
            playerText.grid(row = row, column = column, padx = 20, pady = 20)
            #checkwins
    if(turns >= 3):
        checkWins():
    # CPU moves
    r = random.randint(0, 2)
    c = random.randint(0, 2)
    while(data[r][c] != ' '):
        r = random.randint(0, 2)
        c = random.randint(0, 2)
    for cpu in frame.grid_slaves():
        if int(cpu.grid_info()["row"]) == r and int(cpu.grid_info()["column"]) == c:
            cpu.grid_forget()
            strVar = StringVar()
            strVar.set(CPUSymbol)
            cpuText = Label(frame, textvariable = strVar)
            cpuText.grid(row = r, column = c, padx = 20, pady = 20)
            #checkwins
    if(turns >= 3):
        checkWins():
    
# check if three in a row of same symbol
def checkWins():
    if(data[][] == data[][] and data[][] == data[][]):
    if(data[][] == data[][] and data[][] == data[][]):
    if(data[][] == data[][] and data[][] == data[][]):
    if(data[][] == data[][] and data[][] == data[][]):
    if(data[][] == data[][] and data[][] == data[][]):
    if(data[][] == data[][] and data[][] == data[][]):
    if(data[][] == data[][] and data[][] == data[][]):
    if(data[][] == data[][] and data[][] == data[][]):
    else:
    print("uwu")

root.mainloop()
