from random import randint
import tkinter

commands = {
    "<Left>"    : lambda e: print("left") ,
    "<Down>"    : lambda e: print("down"),
    "<Right>"   : lambda e: print("right"),
    "<Up>"      : lambda e: print("up"),
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
	print("---------")
	for i in board:
		print("|" + "|".join([str(x) for x in i]) + "|")
		print("---------")


if __name__=="__main__":
    root = tkinter.Tk()
    for command in commands.keys():
        root.bind(command, commands[command])

    print( "Press any arrow to play the game (Escape to exit):" )
    
    # don't show the tk window
    root.withdraw()
    root.mainloop()


    addNumberToBoard()
    addNumberToBoard()

    showBoard()

    


