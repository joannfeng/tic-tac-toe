# tictactoes
# Joann Feng, Lara Flynn
# began January 27 2021
# last updated February 9 2021

from array import *
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
winFrame = Frame(root)
winFrame.grid(row = 0, column = 0)

playerSymbol = "initPS"
CPUSymbol = "initCS"
v = IntVar()
gameWon = False


def interpretSymbol():
    initFrame.destroy()
    selected = v.get()
    if(selected == 1):
        global playerSymbol
        playerSymbol = "X"
        global CPUSymbol
        CPUSymbol = "O"
    else:
        playerSymbol = "O"
        CPUSymbol = "X"
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
    if not gameWon:
        updateGUI(playerSymbol, playerRow, playerColumn)

    # cpu coords
    if not checkFull():
        cpuRow = random.randint(0, 2)
        cpuColumn = random.randint(0, 2)
        while data[cpuRow][cpuColumn] != ' ': # find blank
                cpuRow = random.randint(0, 2)
                cpuColumn = random.randint(0, 2)
        data[cpuRow][cpuColumn] = CPUSymbol
        if not gameWon:
            updateGUI(CPUSymbol, cpuRow, cpuColumn)


def checkFull():
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == ' ':
                return False
    return True


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


def updateGUI(symbol, row, column):
    global gameWon
    for x in frame.grid_slaves():
        if int(x.grid_info()["row"]) == row and int(x.grid_info()["column"]) == column:
            x.grid_forget()
            strVar = StringVar()
            strVar.set(symbol)
            text = Label(frame, textvariable = strVar)
            text.grid(row = row, column = column, padx = 20, pady = 20)
            b = checkWins(symbol)
            if b:
                frame.grid_forget()
                frame.destroy()
                gameWon = True
                msg = Label(winFrame, text = "congrats " + str(symbol))
                msg.grid(row = 1, column = 1, padx = 110, pady = 90)
                return
            elif checkFull() and not b:
                frame.grid_forget()
                frame.destroy()
                gameWon = True
                msg = Label(winFrame, text = "tie lmao rip")
                msg.grid(row = 1, column = 1, padx = 110, pady = 90)
                return
    

def checkHorizontal():
    rows = 3
    for r in range(rows):
        if data[r][0] != ' ':
            if data[r][0] == data[r][1] and data[r][1] == data[r][2] and data[r][0] == data[r][2]:
                return True
    return False


def checkVertical():
    columns = 3
    for c in range(columns):
        if data[0][c] != ' ':
            if data[0][c] == data[1][c] and data[1][c] == data[2][c] and data[0][c] == data[2][c]:
                return True
    return False


def checkDiagonal():
    if data[1][1] != ' ':
        if((data[0][0] == data[1][1] and data[1][1] == data[2][2] and data[0][0] == data[2][2])
        or (data[0][2] == data[1][1] and data[1][1] == data[2][0] and data[0][2] == data[2][0])):
            return True        
    return False


# check if three in a row of same symbol
def checkWins(symbol):
    b = checkHorizontal() or checkVertical() or checkDiagonal()
    return b

root.mainloop()
