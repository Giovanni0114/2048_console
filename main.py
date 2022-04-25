from random import randint
from tkinter import Tk


commands = {
    "<Left>"    : lambda e: [mergeNumbersLeft(), showBoard()] ,
    "<Down>"    : lambda e: [mergeNumbersDown, showBoard()],
    "<Right>"   : lambda e: [mergeNumbersRight(), showBoard()],
    "<Up>"      : lambda e: [mergeNumbersUp(), showBoard()],

    #----------------------------------------------------------------
    
    "<r>"       : lambda e: print("reset"),
    "<Escape>"  : lambda e: root.destroy()
}

board = [
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0]
]


def addNumberToBoard():
	global board
	while True:
		x = randint(0,3)
		y = randint(0,3)
		if board[x][y] == 0:
			break

		board[x][y] = 2

def showBoard():
    print("\033[H\033[J", end="")
    print("---------")
    for i in board:
        print("|" + "|".join([str(x) for x in i]) + "|")
        print("---------")


def _merge(board):
    for i in board:
        length = len(i)
        cur = i[0]

        for j in range(length):
            if i[j] == cur:
                i[j] *= 2
                i = _slip(i, j)
            else:
                cur = j

def _slip(array, start):
    for q in range(start+1, len(array))[::-1]:
        array[q] = array[q-1]
    return array 


def mergeNumbersUp():
    pass

def mergeNumbersLeft():
    pass

def mergeNumbersDown():
    pass

def mergeNumbersRight():
    pass


if __name__=="__main__":
    root = Tk()
    root.withdraw()
    for command in commands.keys():
        root.bind(command, commands[command])

    print( "Press any arrow to play the game (Escape to exit):" )
    
    addNumberToBoard()
    addNumberToBoard()

    showBoard()

    # don't show the tk window
    root.mainloop()

