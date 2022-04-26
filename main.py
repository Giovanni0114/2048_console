from random import randint
import tkinter
from sys import argv

GUI = False
DEBUG = False
SIZE = 4

commands = {
	"<Left>"	: lambda e: [mergeNumbersLeft(), showBoard(), addNumberToBoard()] ,
	"<Down>"	: lambda e: [mergeNumbersDown(), showBoard(), addNumberToBoard()],
	"<Right>"   : lambda e: [mergeNumbersRight(), showBoard(), addNumberToBoard()],
	"<Up>"	  : lambda e: [mergeNumbersUp(), showBoard(), addNumberToBoard()],

	#----------------------------------------------------------------
	
	"<r>"	   : lambda e: [restart(), showBoard()],
	"<Escape>"  : lambda e: root.destroy()
}

_startingBoard =  [[]]

board = [[]]

labels = []


def addNumberToBoard():
	global board
	while True:
		x,y = randint(0,SIZE-1),randint(0,SIZE-1)
		if board[x][y] == 0:
			break

	board[x][y] = 2

def showBoard():
	if GUI:
		for i in range(SIZE):
			for j in range(SIZE):
				labels[i][j].config(text = str(board[i][j]))
	else:
		if not DEBUG:
			print("\033[H\033[J", end="")

		print("-"*(SIZE*2+1))
		for i in board:
			print("|" + "|".join(["%04s"%x for x in i]) + "|")
			print("-"*(SIZE*5+1))


def _merge(board):
	for l in range(SIZE):
		line = board[l]
		cur = -1

		for i in range(SIZE):
			for _ in range(SIZE-1):
				if line[i] == 0:
					line = _slip(line, i)
			if line[i] == cur:
				line[i-1] *= 2
				line = _slip(line, i)
				pass
			else:
				cur = line[i]
		board[l] = line
	return board

def _slip(array, start):
	for q in range(start, SIZE-1):
		array[q] = array[q+1] 
	array[-1] = 0
	return array 

def mergeNumbersUp():
	global board
	_arr = []
	for i in range(SIZE):
		_arr.append([])
		_arr[-1] = [x[i] for x in board]
	_arr = _merge(_arr)

	_arr2 = []
	for i in range(SIZE):
		_arr2.append([])
		_arr2[-1] = [x[i] for x in _arr]

	board = _arr2

def mergeNumbersLeft():
	global board
	board = _merge(board)

def mergeNumbersDown():
	global board
	_arr = []
	for i in range(SIZE):
		_arr.append([])
		_arr[-1] = [x[i] for x in board][::-1]
	_arr = _merge(_arr)
	_arr = [i[::-1] for i in _arr]
	_arr2 = []
	for i in range(SIZE):
		_arr2.append([])
		_arr2[-1] = [x[i] for x in _arr]

	board = _arr2

def mergeNumbersRight():
	global board
	_arr = _merge([i[::-1] for i in board])
	board = [i[::-1] for i in _arr]


def restart():
	global board
	board = _startingBoard
	addNumberToBoard()
	addNumberToBoard()

def createBoard():
	global _startingBoard
	global board

	for _ in range(SIZE):_startingBoard[0].append(0)
	for _ in range(SIZE-1):
		_startingBoard.append([])
		_startingBoard[-1].extend(_startingBoard[0])

	board = _startingBoard


if __name__=="__main__":
	if len(argv) > 1:
		if "debug" in argv:
			DEBUG = True

		if "gui" in argv:
			GUI = True
		
		if argv[1] == "--size" or argv[1] == "-s":
			_s = int(argv[2])
			if _s >= 4 and _s <= 8:
				SIZE = _s

	createBoard()

	root = tkinter.Tk()
	for command in commands.keys():
		root.bind(command, commands[command])

	if GUI:
		root.title = f"2048 - {SIZE}x{SIZE}"
		root.geometry(f"{SIZE*50}x{SIZE*50}")
		for i in range(SIZE):
			labels.append([])
			for j in range(SIZE):
				labels[-1].append(tkinter.Label(root, text="0", padx=10, pady=10, justify="center"))
				labels[-1][-1].grid(row=i, column=j)
	else:
		root.withdraw()

	addNumberToBoard()
	addNumberToBoard()

	showBoard()

	root.mainloop()