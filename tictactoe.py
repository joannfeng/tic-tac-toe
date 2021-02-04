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
# args here are the player coords
def interpretButton(playerRow, playerColumn):
    # player coords
    data[playerRow][playerColumn] = playerSymbol

    # cpu coords
    cpuRow = random.randint(0, 2)
    cpuColumn = random.randint(0, 2)
    while data[cpuRow][cpuColumn] != ' ': # find blank
        cpuRow = random.randint(0, 2)
        cpuColumn = random.randint(0, 2)
    data[cpuRow][cpuColumn] = CPUSymbol
    updateGUI(playerRow, playerColumn, cpuRow, cpuColumn)

    
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


def updateGUI(playerRow, playerColumn, cpuRow, cpuColumn):
    # player moves
    for player in frame.grid_slaves():
        if int(player.grid_info()["row"]) == playerRow and int(player.grid_info()["column"]) == playerColumn:
            player.grid_forget()
            strVar = StringVar()
            strVar.set(playerSymbol)
            playerText = Label(frame, textvariable = strVar)
            playerText.grid(row = playerRow, column = playerColumn, padx = 20, pady = 20)
            if checkWins(playerSymbol):
                return
    # CPU moves
    for cpu in frame.grid_slaves():
        if int(cpu.grid_info()["row"]) == cpuRow and int(cpu.grid_info()["column"]) == cpuColumn:
            cpu.grid_forget()
            strVar = StringVar()
            strVar.set(CPUSymbol)
            cpuText = Label(frame, textvariable = strVar)
            cpuText.grid(row = cpuRow, column = cpuColumn, padx = 20, pady = 20)
            if checkWins(CPUSymbol):
                return
    
def checkHorizontal():
    rows = 3
    for r in range(rows):
        print(r)
        if data[r][0] != ' ':
            if data[r][0] == data[r][1] and data[r][1] == data[r][2]:
                return True
    return False
        
def checkVertical():
    columns = 3
    for c in range(columns):
        if data[0][c] != ' ':
            if data[0][c] == data[1][c] and data[1][c] == data[2][c]:
                return True
    return False

def checkDiagonal():
    if((data[0][0] != ' ' and data[0][0] == data[1][1] and data[1][1] == data[2][2])
    or (data[0][2] != ' ' and data[0][2] == data[1][1] and data[1][1] == data[2][0])):
        return True
    return False

# check if three in a row of same symbol
def checkWins(symbol):
    b = checkHorizontal() or checkVertical() or checkDiagonal()
    if (b):
        s = " won!"
        print(symbol + s)
    else:
        print("no win")
    print(b)
    print(data)
    return b
    
root.mainloop()
