from random import randint
import tkinter
from sys import argv
import argparse


GUI = False
DEBUG = False
SIZE = 4

commands = {
	"<Left>"	: lambda e: mergeNumbersLeft(),
	"<Down>"	: lambda e: mergeNumbersDown(),
	"<Right>"   : lambda e: mergeNumbersRight(),
	"<Up>"	  	: lambda e: mergeNumbersUp(),
	#----------------------------------------------------------------
	"<r>"	   	: lambda e: restart(),
	"<Escape>"  : lambda e: root.destroy(), 

	"<KeyRelease>"	: lambda e: showBoard()
}



board = [[]]
labels = []


def addNumberToBoard():
	global board
	free = []
	for x in range(SIZE):
		for y in range(SIZE):
			if board[x][y] == 0:
				free.append((x,y))

	num = randint(0, len(free)-1)
	board[free[num][0]] [free[num][1]] = 2

def showBoard():
	if GUI:
		for i in range(SIZE):
			for j in range(SIZE):
				labels[i][j].config(text = str(board[i][j]))
	else:
		if not DEBUG:
			print("\033[H\033[J", end="")

		print("-"*(SIZE*5+1))
		for i in board:
			print("|" + "|".join(["%04s"%x for x in i]) + "|")
			print("-"*(SIZE*5+1))


def _merge(board):
	changed = False

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
		if board[l] != line:
			changed = True

		board[l] = line
	return board, changed

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
	_arr, chang = _merge(_arr)

	_arr2 = []
	for i in range(SIZE):
		_arr2.append([])
		_arr2[-1] = [x[i] for x in _arr]

	board = _arr2

	if chang:
		addNumberToBoard()

def mergeNumbersLeft():
	global board
	board, chang = _merge(board)
	
	if chang:
		addNumberToBoard()

def mergeNumbersDown():
	global board
	_arr = []
	for i in range(SIZE):
		_arr.append([])
		_arr[-1] = [x[i] for x in board][::-1]
	_arr, chang = _merge(_arr)
	
	
	_arr = [i[::-1] for i in _arr]
	_arr2 = []
	for i in range(SIZE):
		_arr2.append([])
		_arr2[-1] = [x[i] for x in _arr]

	board = _arr2

	if chang:
		addNumberToBoard()

def mergeNumbersRight():
	global board
	_arr, chang = _merge([i[::-1] for i in board])
	board = [i[::-1] for i in _arr]
	
	if chang:
		addNumberToBoard()


def restart():
	global board
	
	createBoard()


def createBoard():
	global board

	board = [[]]

	for _ in range(SIZE):
		board[0].append(0)
	
	for _ in range(SIZE-1):
		board.append([])
		board[-1].extend(board[0])

	addNumberToBoard()
	addNumberToBoard()

	showBoard()


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Simple impementation of 2048 game")

	parser.add_argument("-g", "--gui", 
						help="Runs game in window mode",
						action="store_true")

	parser.add_argument("-d", "--debug",
						help="(Don't work with 'gui' argument) Prevent program from clearing console output",
						action="store_true")

	parser.add_argument("-s", "--size",
						help="Set size of game board. Must be between 4 and 8. (Default 4)", 
						default=4)

	args = parser.parse_args()

	if args.debug: DEBUG = True
	if args.gui: GUI = True

	SIZE = int(args.size)
	if SIZE > 8 or SIZE < 4: raise ValueError

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
		showBoard()

	createBoard()

	root.mainloop()