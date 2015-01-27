import os
import random
os.system('cls')

""" Single Player BattleShip Game Info:
	Boards have 100 cells in 10 rows numbered A0 through J9
	(chose to use 0-9 instead of traditional 1-10 to simplify code)
			Cells will have 3 states:
			"-" = empty or unknown
			"O" = filled
			"X" = bombed
			"@" = known hit
	players have 7 ships in their fleet:
		Aircraft Carrier (5 cells)
		Battleship (4 cells)
		Cruiser (3 cells)
		Destroyer 1 (2 cells)
		Destroyer 2 (2 cells)
		Submarine 1 (1 cell)
		Submarine 2 (1 cell)
	"""

def initialize_board(board):
	board = {}
	for c in range(65,75):
		for i in range(10):
			board[chr(c) + str(i)] = '-'
	return board

def error(): #if I screwed up
	print "D10D3, your code sucks again"
	quit()
	
def display_board(board): #displays selected board neatly
	print "    0 1 2 3 4 5 6 7 8 9"
	print "   ____________________"
	for c in range(65,75):
		char = chr(c)
		pstr = char + " |"
		for i in range(10):
			pstr += " " + board[char + str(i)]
		pstr += "|"
		print pstr
	print "  ----------------------"
	
def shipname(ship): #convert ships cell to ship name
	shiplist = [
		"Aircraft Carrier (5 cells)",
		"BattleShip (4 cells)",
		"Cruiser (3 cells)",
		"Destroyer 1 (2 cells)",
		"Destroyer 2 (2 cells)",
		"Submarine 1 (1 cell)",
		"Submarine 2 (1 cell)" ]
	shipname = ""
	shipname = shiplist[ship-1]
	return shipname

def player_setup(board): #Player places his ships
	for i in range (1,8):
		while True:
			os.system('cls')
			intro_banner()
			ships = [5,4,3,2,2,1,1] #cell size of each of the ships
			ship_length = ships[i-1]
			display_board(board)
			print "-= PLAYER BOARD SETUP =-"
			print ""
			print "   For each selection, first choose the top left ship position," 
			print "   then choose to fill to the right or down"
			print "   Where would you like to place %s" % shipname(i)
			choice = choose_cell() #player chooses coordinate
			while True:
				direction = raw_input ('   Fill in ship across or down? (A or D)> ')
				direction.lower()
				if direction == 'a':
					break
				elif direction == 'd':
					break
				else:
					print "   Please enter A or D"
			selection = generate_selection(choice,ship_length,direction)
			test = test_selection(selection,board)
			if test:
				board = write_ship(selection,board)
				break
			else:
				print ""
				print "   That ship won't fit there, choose another spot"
				raw_input ('   <Press a Enter to select again>')
	return board
	
def AI_setup(board): #AI places ships
	for i in range (1,8):
		while True:
			ships = [5,4,3,2,2,1,1] #cell size of each of the ships (+1 to help for/next iteration)
			ship_length = ships[i-1]
			choice = choose_cell_AI() #Computer chooses coordinate
			dir_pos = ["a","d"] #possible orientations: Across or Down
			direction = random.choice(dir_pos)
			selection = generate_selection(choice,ship_length,direction)
			test = test_selection(selection,board)
			if test:
				board = write_ship(selection,board)
				print "Generating game boards..."
				break
			else:
				print "Generating game boards..."
	return board

def choose_cell(): #Asks player for cell choice, returns value
	while True:
		row = raw_input ('   What Row? (A-J)> ')
		row = row.upper()
		letters = "ABCDEFGHIJ"
		if row in letters:
			break
		else:
			print "   Please type a letter from A to J"
			raw_input ('   <Press a Enter to select again>')
	while True:
		column = raw_input('   What Column? (0-9)> ')
		#column = int(column)
		numbers = '0,1,2,3,4,5,6,7,8,9'
		if column in numbers:
			break
		else:
			print "   Please type a number from 1 to 10"
			raw_input ('   <Press a Enter to select again>')
	choice = ""
	choice = choice + row + column
	return choice
	
def choose_cell_AI(): #Generates random cell choice, returns value
	letters = "ABCDEFGHIJ"
	numbers = "0123456789"
	row = random.choice(letters)
	column = random.choice(numbers)
	choice = ""
	choice = choice + row + column
	return choice

def generate_selection(choice,ship_length,direction): #Generates list of selected cells to place ship
	selection = [choice]
	if direction == 'a':
		#across stuff
		for i in range(1,ship_length):
			addrow = choice[0]
			addnum = choice[1]
			addnum = int(addnum)
			addnum += i
			addnum = str(addnum)
			addselect = ""
			addselect = addselect + addrow + addnum
			selection.append(addselect)
	else:
		#down stuff
		for i in range(1,ship_length):
			addrow = ord(choice[0]) #translates the letter into and ascii number
			addrow += (i) #iterates it by 1
			addrow = chr(addrow) #translates it back into a letter!
			addnum = choice[1]
			addselect = ""
			addselect = addselect + addrow + addnum
			selection.append(addselect)
	return selection

def test_selection(selection,board): #checks if all cells for selected ship placement are allowed
	test = False
	badcell = False
	for i in range(0,len(selection)): #creates loop based on length of selection
		if selection[i] in board:
			if board[selection[i]] == "-":
				fnord = "fnord"
			else:
				badcell = True			
		else:
			badcell = True
	if badcell:
		test = False
	else:
		test = True
	return test
	
def test_shot(selection,board): #checks if shot is valid
	test = False
	badcell = False
	for i in range(0,len(selection)): #creates loop based on length of selection
		if selection[i] in board:
			if board[selection[i]] == "-":
				fnord = "fnord"
			elif board[selection[i]] == "O":
				fnord = "fnord"
			elif board[selection[i]] == "X":
				badcell = True
			elif board[selection[i]] == "@":
				badcell = True
			else:
				badcell = True			
		else:
			badcell = True
	if badcell:
		test = False
	else:
		test = True
	return test

def write_ship(selection,board): #writes the (now checked) ship selection to the board
	# writecell = 0
	for i in range(0,len(selection)): #creates loop based on length of selection
		board[selection[i]] = "O"
	return board
	
def intro_banner(): #fancy graphics
	print"""
	______  ___ _____ _____ _      _____ _____ _   _ ___________
	| ___ \/ _ \_   _|_   _| |    |  ___/  ___| | | |_   _| ___ \\
	| |_/ / /_\ \| |   | | | |    | |__ \ `--.| |_| | | | | |_/ /
	| ___ \  _  || |   | | | |    |  __| `--. \  _  | | | |  __/
	| |_/ / | | || |   | | | |____| |___/\__/ / | | |_| |_| |
	\____/\_| |_/\_/   \_/ \_____/\____/\____/\_| |_/\___/\_|
	
	Ver 0.9  by D10D3
	"""

def did_anyone_win(p_board,c_board):
	#uses a letter loop and a number loop to check
	#every cell of both boards for intact ship cells
	#if none found on a board, the opponent is the winner
	o_count_player = 0
	o_count_computer = 0
	for i in range(0,10):#letter loop
		letter_index = "ABCDEFGHIJ"
		letter = letter_index[i]
		letter = str(letter)
		for j in range(0,10):#number loop
			number_index = range(0,10)
			number = number_index[j]
			number = str(number)
			checkcell = letter + number
			if p_board[checkcell] == "O":
				o_count_player += 1
			# else:
			# 	fnord = "fnord"
			if c_board[checkcell] == "O":
				o_count_computer += 1
			# else:
			# 	fnord = "fnord"
	if o_count_player == 0:
		winner = "computer"
	elif o_count_computer == 0:
		winner = "player"
	else:
		winner = None
	return winner

def win_lose(winner): #declare winner, ask if play again
	print ""
	if winner == "player":
		print "   You Win!"
	else:
		print "   You Lose"
	print ""
	while True:
		again = raw_input ('   Play Again? Y or N> ')
		again.lower
		if again == "y" or again == "Y":
			break
		elif again == "n" or again == "N":
			print "Thanks for playing!"
			quit()
		else:
			print "   Enter Y or N"

def man_or_ran(player_board): #choose manual or random player board setup
	while True: #choose manual or random player ship placement
		print ""
		print '   Would you like to place your ships manually or randomly?'
		setup = raw_input('   <M>anual or <R>andom? > ')
		setup.lower()
		if setup == 'm':
			player_board = player_setup(player_board)
			break
		elif setup == 'r':
			player_board = AI_setup(player_board)
			break
		else:
			print "   Please enter M or R"
	return player_board

#***INITIALIZE AND SETUP***
os.system('cls')
intro_banner()
player_board = {}
computer_board = {}
hit_board = {}
player_board = initialize_board(player_board)
computer_board = initialize_board(computer_board)
hit_board = initialize_board(hit_board)
player_board = man_or_ran(player_board)
computer_board = AI_setup(computer_board)


#***BEGIN GAME LOOP***
while True:
	while True: #did anyone win? if so play again?
		winner = did_anyone_win(player_board,computer_board)
		if winner:
			win_lose(winner)
			os.system('cls')
			intro_banner()
			player_board = {}
			computer_board = {}
			hit_board = {}
			player_board = initialize_board(player_board)
			computer_board = initialize_board(computer_board)
			hit_board = initialize_board(hit_board)
			player_board = man_or_ran(player_board)
			computer_board = AI_setup(computer_board)
			break
		else:
			fnord = "fnord"
			break
	os.system('cls')
	intro_banner()
	print "    -= PLAYER SHIPS =-"
	print ""
	display_board(player_board)
	print ""
	print "        -= Enemy =-"
	display_board(hit_board) #Show the player where they have shot(and hit) so far
	#display_board(computer_board) #cheat mode for debugging
	print ""
	
	#Player Attack
	while True:
		print "   Choose A Cell to Attack!"
		target = choose_cell() #player chooses coordinate
		shooting = [target]
		test = test_shot(shooting,computer_board)
		print ""
		if test:
			if computer_board[target] == "-":
				computer_board[target] = "X"
				hit_board[target] = "X"
				print "   You didn't hit anything."
				break
			else:
				computer_board[target] = "@"
				print "You hit an enemy ship!"
				hit_board[target] = "@"
				break
		else:
			print ""
			print "   That is not a valid target!"
			raw_input ('   <Press a Enter to select again>')
	
	#Computer Attack
	while True:
		target = choose_cell_AI() #AI chooses coordinate
		shooting = [target]
		test = test_shot(shooting,player_board)
		if test:
			if player_board[target] == "-":
				player_board[target] = "X"
				print "   Computer attacks %s and misses" % target
				raw_input ('   <Press a Enter to continue>')
				break
			else:
				player_board[target] = "@"
				print "   Computer attacks %s and hits!" % target
				raw_input ('   <Press a Enter to continue>')
				break
		else:
			fnord = "fnord"
