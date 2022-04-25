from random import randint
import sys
import tkinter as tk

END_OF_TEXT = chr(3)  # CTRL+C (prints nothing)
END_OF_FILE = chr(4)  # CTRL+D (prints nothing)
CANCEL      = chr(24) # CTRL+X
ESCAPE      = chr(27) # Escape
CONTROL     = ESCAPE +'['

ARROW_UP    = CONTROL+'A'
ARROW_DOWN  = CONTROL+'B'
ARROW_RIGHT = CONTROL+'C'
ARROW_LEFT  = CONTROL+'D'

commands = {
    ARROW_UP   :'up arrow',
    ARROW_DOWN :'down arrow',
    ARROW_RIGHT:'right arrow',
    ARROW_LEFT :'left arrow',
}

board = [
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0]
]

def getch():
    k = sys.stdin.read(1)[0]
    if k in {END_OF_TEXT, END_OF_FILE, CANCEL}: raise KeyboardInterrupt
    print('raw input 0x%X'%ord(k),end='\r\n')
    return k

def add():
	global board
	while True:
		x = randint(0,3)
		y = randint(0,3)
		if board[x][y] == 0:
			break

		board[x][y] = 2

def show():
	print("---------")
	for i in board:
		print("|" + "|".join([str(x) for x in i]) + "|")
		print("---------")



add()
add()

show()

def key(event):
    """shows key or tk code for the key"""
    if event.keysym == 'Escape':
        root.destroy()
    if event.char == event.keysym:
        # normal number and letter characters
        print( 'Normal Key %r' % event.char )
    elif len(event.char) == 1:
        # charcters like []/.,><#$ also Return and ctrl/key
        print( 'Punctuation Key %r (%r)' % (event.keysym, event.char) )
    else:
        # f1 to f12, shift keys, caps lock, Home, End, Delete ...
        print( 'Special Key %r' % event.keysym )


root = tk.Tk(8)
print( "Press a key (Escape key to exit):" )
root.bind_all('<Key>', key)
# don't show the tk window
root.withdraw()
root.mainloop()