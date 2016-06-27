from tkinter import *
from PIL import ImageTk, Image

# Initialise Tkinter window
window = Tk()
# Prevent resize
window.resizable(width=False, height=False)
# Set title
window.title("Tiny Blue UI")

############################

def board_mouse_callback(event):
	print(event.x, event.y, event.type)

############################

# Create menu bar
menu_bar = Menu(window)

# Add game menu
game_menu = Menu(menu_bar, tearoff=1)
game_menu.add_command(label="New Game (Ctrl+N)")
game_menu.add_command(label="Save Game (Ctrl+S)")
game_menu.add_separator()
game_menu.add_command(label="Undo Move (Ctrl+Z)")
game_menu.add_command(label="Redo Move (Ctrl+Shift+Z)")
menu_bar.add_cascade(label="Game", menu=game_menu)

# Add settings menu
settings_menu = Menu(menu_bar, tearoff=1)

# Setup AI level menu
ai_level = Menu(settings_menu, tearoff=0)
ai_level.add_command(label="1")
ai_level.add_command(label="2")
ai_level.add_command(label="3")
ai_level.add_command(label="4")
ai_level.add_command(label="5")

# Setup theme Menu
theme_option = Menu(settings_menu, tearoff=0)
theme_option.add_command(label="Classic")
theme_option .add_command(label="Alamo")

# Add settings menu options
settings_menu.add_command(label="Start As Black")
settings_menu.add_cascade(label="Set AI Level", menu=ai_level)
settings_menu.add_cascade(label="Set Theme", menu=theme_option)

menu_bar.add_cascade(label="Settings", menu=settings_menu)

# Add about Section
menu_bar.add_command(label="About")

# Display menu
window.config(menu=menu_bar)

############################

# Create board
# Board details
# Each square is 24 x 24px
# Row letter spacing is 12 x 24px
# Col number spacing is 24 x 12px

board_w = (24*8) + (12*2)
board = Frame(window, width=board_w, height=board_w)
board.pack(side=LEFT)

# Create grid

# Top letters 
for i in range(8):
	# Fix the labels to be a set w/h
	# From: http://effbot.org/tkinterbook/button.htm
	letter_frame = Frame(board, height=12, width=24, bg="yellow")
	letter_frame.pack_propagate(0)

	l=Label(letter_frame, text=chr(ord('a')+i), font=("Arial", 8))
	l.pack(fill=BOTH, expand=1)
	letter_frame.grid(row=0,column=1+i)

# Bottom letters
for i in range(8):
	letter_frame = Frame(board, height=12, width=24, bg="yellow")
	letter_frame.pack_propagate(0)

	l=Label(letter_frame, text=chr(ord('a')+i), font=("Arial", 8))
	l.pack(fill=BOTH, expand=1)
	letter_frame.grid(row=9,column=1+i)
	#Label(board, text=chr(ord('a')+i)).grid(row=9,column=1+i) # Old method

# Left numbers
for i in range(8):
	letter_frame = Frame(board, height=24, width=12, bg="yellow")
	letter_frame.pack_propagate(0)

	l=Label(letter_frame, text=str((i-8)*-1), font=("Arial", 8))
	l.pack(fill=BOTH, expand=1)
	letter_frame.grid(row=1+i,column=0)
	#Label(board, text=str((i-8)*-1)).grid(row=1+i,column=0) # Old method

# Right numbers
for i in range(8):
	letter_frame = Frame(board, height=24, width=12, bg="yellow")
	letter_frame.pack_propagate(0)

	l=Label(letter_frame, text=str((i-8)*-1), font=("Arial", 8))
	l.pack(fill=BOTH, expand=1)
	letter_frame.grid(row=1+i,column=9)

# Build tiles
# Important to remember that the chess tile of the bottomost lef (a1) is black 

tile_board = Canvas(board, width=(24*8), height=(24*8), bg="yellow", highlightthickness=0)
tile_board.grid(row=1, column=1, columnspan=8, rowspan=8, padx=0, pady=0, ipadx=0, ipady=0)
for i in range(8):
	for j in range(8):

		if(i%2==1): # Odd row
			if(j%2==1):
				tile_color="lightgrey"
			else:
				tile_color="grey"
		else:
			if(j%2==1):
				tile_color="grey"
			else:
				tile_color="lightgrey"

		tile_board.create_rectangle(24*i, 24*j, (24*i)+24, (24*j)+24, fill=tile_color, activefill="cyan", width=0)

tile_board.bind("<Button-1>", board_mouse_callback)
#tile_board.bind("<B1-Motion>", board_mouse_callback)
tile_board.bind("<Motion>", board_mouse_callback)
tile_board.bind("<ButtonRelease-1>", board_mouse_callback)


'''
for i in range(8):
	for j in range(8):
		tile_frame = Frame(board, height=24, width=24, bg="yellow")
		tile_frame.pack_propagate(0)

		if(i%2==1): # Odd row
			if(j%2==1):
				tile_color="lightgrey"
			else:
				tile_color="grey"
		else:
			if(j%2==1):
				tile_color="grey"
			else:
				tile_color="lightgrey"

		t=Button(tile_frame, bg=tile_color, activebackground=tile_color, borderwidth=1, font=("Arial", 8))
		t.pack(fill=BOTH, expand=1)
		tile_frame.grid(row=1+i,column=1+j)
'''

############################

# Create log
log = Frame(window, bg="blue", width=150, height=board_w)
log.pack(side=RIGHT)

############################

# Start Tkinter loop
window.mainloop()


board = [['r','n','b','q'  ,'k'  ,'kb' ,'kn' ,'kr' ],
		 ['p','p','b','p' ,'kp' ,'kbp','knp','krp'],
		 [''   ,''   ,''   ,''   ,''   ,''   ,''   ,''   ],
		 [''   ,''   ,''   ,''   ,''   ,''   ,''   ,''   ],
		 [''   ,''   ,''   ,''   ,''   ,''   ,''   ,''   ],
		 [''   ,''   ,''   ,''   ,''   ,''   ,''   ,''   ],
		 ['QRP','QNP','QBP','QP' ,'KP' ,'KBP','KNP','KRP'],
		 ['QR' ,'QN' ,'QB' ,'Q'  ,'K'  ,'KB' ,'KN' ,'KR' ]]

