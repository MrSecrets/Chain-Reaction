import numpy as np
from colorama import Fore, Back, Style 

print(f"Do not make a gris larger than 54x54, otherwise you cant exit")
grid_row = int(input(f"enter grid row size: "))
grid_col = int(input(f"enter grid column size: "))

player_map = np.zeros([grid_row,grid_col],dtype=int)
visible_map = np.zeros([grid_row,grid_col],dtype=int)
current_map = np.zeros([grid_row,grid_col],dtype=int)

weight_map = 3*np.ones([grid_row,grid_col],dtype=int)
weight_map[1:-1,1:-1] = 4
weight_map[0,0] = 2
weight_map[0,-1] = 2
weight_map[-1,0] = 2
weight_map[-1,-1] = 2

player_dict = {1:2, 2:1}
player = 2
game_round = 0

def checker(row, col, player):

	if row ==54:
		if col ==54:
			updater(row,col,player,game_round)
	elif row > grid_row-1:
		print(f"invalid move")
		player = player_dict[player]
		play(player,game_round)
	elif col > grid_col-1:
		print(f"invalid move")
		player = player_dict[player]
		play(player,game_round)
	elif player_map[row,col] == player:
		updater(row,col,player,game_round)
	elif player_map[row,col] == 0:
		updater(row,col,player,game_round)
	else:
		print(f"invalid move")
		player = player_dict[player]
		play(player,game_round)

def updater(row, col, player,game_round):

	player_map[row,col] = player
	current_map[row,col] +=1
	if current_map[row,col] == weight_map[row,col]:
		explosion(row,col,player,game_round)
	else:
		winner(player,game_round)
		play(player,game_round)

def explosion_updater(row, col, player,game_round):

	player_map[row,col] = player
	current_map[row,col] +=1
	if current_map[row,col] == weight_map[row,col]:
		explosion(row,col,player,game_round)

def explosion(row, col,player,game_round):

	player_map[row,col] = 0
	current_map[row,col] = 0
	if row-1>=0:
		print(1)
		explosion_updater(row-1,col,player,game_round)
	if row+1<5:
		print(2)
		explosion_updater(row+1,col,player,game_round)
	if col-1>=0:
		print(3)
		explosion_updater(row,col-1,player,game_round)
	if col+1<5:
		print(4)
		explosion_updater(row,col+1,player,game_round)
	
	winner(player,game_round)
	play(player,game_round)

def winner(player,game_round):

	result = np.any(player_map == player_dict[player])
	# if game_round <1:
		# play(player,game_round)
	if not result:
		print(f"Congratulation, player {player} has won")
		return
	else:
		play(player,game_round)

def get_color_coded_background(i,j):
	
	return "\033[4{}m {} \033[0m".format(i+1, j)

def printer():
	
	visible_map = np.vectorize(get_color_coded_background)(player_map,current_map)
	n, m = visible_map.shape
	row_sep=""
	fmt_str = "\n".join([row_sep.join(["{}"]*m)]*n)
	print(fmt_str.format(*visible_map.ravel()))

def play(player,game_round):

	printer()
	player = player_dict[player]
	try:
		in_row, in_col = input(f"player {player} enter row and column: ").split()
	except:
		print(f" type 55 55 to exit script")
		print(f"invalid move, check input format")
		play(player_dict[player],game_round)
	game_round+=1
	# print(game_round)
	checker(int(in_row)-1,int(in_col)-1,player)

play(player,game_round)

