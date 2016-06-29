from tkinter import *

class UI:

	def __init__(self):
		self.setup_window()
		self.setup_menubar() 
		self.setup_board()
		self.setup_log()
		self.window.mainloop() # Start tkinter loop

	def setup_log(self):
		self.log = Log(self.window)

	def setup_menubar(self):
		self.menubar = MenuBar(self.window)
	
	def setup_board(self):
		self.board = Board(self.window)

	def setup_window(self):
		self.window = Tk() # Get the tk root
		self.window.title("Tiny Blue Chess UI") # Set title
		self.window.resizable(width=False, height=False) # Prevent window resizing

class MenuBar:

	'''
	Refer to menubar_heirachy() for menu organisation.
	Additional underscores mark menu level heirachy
	'''

	def __init__(self, window):
		self.window = window
		self.setup_menu()
		self.setup__game()
		self.setup__settings()
		self.setup__about()

	def setup_menu(self):
		self.menu = Menu(self.window)
		self.window.config(menu=self.menu) # Set the window menubar

	def setup__game(self):
		self._game = Menu(self.menu, tearoff=1)
		self._game.add_command(label="New Game (Ctrl+N)")
		self._game.add_command(label="Save Game (Ctrl+S)")
		self._game.add_separator()
		self._game.add_command(label="Undo Move (Ctrl+Z)")
		self._game.add_command(label="Redo Move (Ctrl+Shift+Z)")
		self.menu.add_cascade(label="Game", menu=self._game)

	def setup__settings(self):
		self._settings = Menu(self.menu, tearoff=1)
		self.setup___ai_levels()
		self.setup___themes()
		self._settings.add_command(label="Play As Black")
		self._settings.add_cascade(label="Set AI Level", menu=self.__ai_levels)
		self._settings.add_cascade(label="Set Board Theme", menu=self.__themes)
		self.menu.add_cascade(label="Settings", menu=self._settings)

	def setup___ai_levels(self):
		self.__ai_levels = Menu(self._settings)
		self.__ai_levels.add_command(label="1")
		self.__ai_levels.add_command(label="2")
		self.__ai_levels.add_command(label="3")
		self.__ai_levels.add_command(label="4")
		self.__ai_levels.add_command(label="5")

	def setup___themes(self):
		self.__themes = Menu(self._settings, tearoff=0)
		self.__themes.add_command(label="Classic")
		self.__themes.add_command(label="Alamo")

	def setup__about(self):
		self.menu.add_command(label="About")

	def menubar_heirachy(self):
		'''
		* MENU BAR HEIRACHY *
		GAME
		> New
		> Save
		> Undo Move
		> Redo Move
		SETTINGS
		> Start As Black
		> Set AI Level
		>> 1 ... 5
		> Set Theme
		>> Classic ...
		ABOUT
		'''
		return

class Log:
	def __init__(self, window):
		self.window = window
		self.log = Frame(self.window, bg="lightgreen", width=150)
		self.log.pack(fill=BOTH, side=RIGHT)

class Piece:

	def __init__(self, board):
		print("started")

class Board:

	def __init__(self, window):
		'''
		Each square is 24 x 24px
		Rank letter frame is 12 x 24px
		File number frame is 24 x 12px
		'''
		self.square_w = 24
		self.window = window
		self.setup_board()
		self.setup_file_rank()
		print("started")

	def setup_board(self):
		self.board_w = (self.square_w*8)+(self.square_w/2*2) # I know its redundant, but useful to break out dimensions
		self.board = Frame(self.window, width=self.board_w, height=self.board_w, bg="blue")
		self.board.pack(side=LEFT)
		self.setup_canvas()

	def setup_canvas(self):
		self.canvas = Canvas(self.board, width=self.board_w, height=self.board_w, bg="yellow", highlightthickness=0)
		self.canvas.grid(row=1, column=1, columnspan=8, rowspan=8)

	def setup_squares(self):
		return

	def setup_file_rank(self):
		'''
		Fix the labels to be a set w/h
		From: http://effbot.org/tkinterbook/button.htm
		'''
		file_h = rank_w = self.square_w/2

		# File labels
		for i in range(8):
			# Top labels
			label_frame_t = Frame(self.board, height=file_h, width=self.square_w, bg="yellow")
			label_frame_t.pack_propagate(0)
			label_t = Label(label_frame_t, text=chr(ord('a')+i), font=("Arial", 8))
			label_t.pack(fill=BOTH, expand=1)
			label_frame_t.grid(row=0,column=1+i)
			# Bottom labels
			label_frame_b = Frame(self.board, height=file_h, width=self.square_w, bg="yellow")
			label_frame_b.pack_propagate(0)
			label_b = Label(label_frame_b, text=chr(ord('a')+i), font=("Arial", 8))
			label_b.pack(fill=BOTH, expand=1)
			label_frame_b.grid(row=9,column=1+i)

		# Rank Labels
		for i in range(8):
			# Left labels
			label_frame_l = Frame(self.board, height=self.square_w, width=rank_w, bg="yellow")
			label_frame_l.pack_propagate(0)
			label_l=Label(label_frame_l, text=str((i-8)*-1), font=("Arial", 8))
			label_l.pack(fill=BOTH, expand=1)
			label_frame_l.grid(row=1+i,column=0)
			# Right labels
			label_frame_r = Frame(self.board, height=self.square_w, width=rank_w, bg="yellow")
			label_frame_r.pack_propagate(0)
			label_r=Label(label_frame_r, text=str((i-8)*-1), font=("Arial", 8))
			label_r.pack(fill=BOTH, expand=1)
			label_frame_r.grid(row=1+i,column=9)

ui = UI()
