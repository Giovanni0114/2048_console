from random import randint
from tkinter import Tk
from sys import argv


DEBUG = False
SIZE = 4

commands = {
	"<Left>"	: lambda e: [mergeNumbersLeft(), showBoard()] ,
	"<Down>"	: lambda e: [mergeNumbersDown(), showBoard()],
	"<Right>"   : lambda e: [mergeNumbersRight(), showBoard()],
	"<Up>"	  : lambda e: [mergeNumbersUp(), showBoard()],

	#----------------------------------------------------------------
	
	"<r>"	   : lambda e: [restart(), showBoard()],
	"<Escape>"  : lambda e: root.destroy()
}

_startingBoard =  [[]]

board = [[]]

def addNumberToBoard():
	global board
	while True:
		x,y = randint(0,SIZE-1),randint(0,SIZE-1)
		if board[x][y] == 0:
			break

	board[x][y] = 2

def showBoard():
	if not DEBUG:
		print("\033[H\033[J", end="")

	print("---------")
	for i in board:
		print("|" + "|".join([str(x) for x in i]) + "|")
		print("---------")


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
		if argv[1] == "debug":
			# Disable clearing console
			DEBUG = True
		elif argv[1] == "--size" or argv[1] == "-s":
			_s = int(argv[2])
			if _s >= 4 and _s <= 8:
				SIZE = _s

	createBoard()

	root = Tk()
	for command in commands.keys():
		root.bind(command, commands[command])

	print( "Press any arrow to play the game (Escape to exit):" )
	
	addNumberToBoard()
	addNumberToBoard()
	board[0] = [0,2,2,4]

	showBoard()

	# don't show the tk window
	# root.withdraw()
	root.mainloop()