#BATTLESHIP GAME

def placement_phase(player):
    pass

def get_empty_board(size):
    return  [['O' for _ in range(size)] for _ in range(size)]

def display_board(game_board):
    alphabet = 'ABCDEFGHIJ'
    display_size = len(game_board)
    first_line = [str(x) for x in range(1, display_size+1)]
    print("  " + " ".join(first_line))
    for x in range(0, (display_size)):
        print(f'{alphabet[x]} {" ".join(game_board[x])}')

def ask_for_input(ship_size):
    coordinates = input("Please provide position in format ie. A1, size of current ship is {ship_size}: ")
    return coordinates


def is_valid_input(player_input, size):
    if len(player_input) ==2:
        rows = player_input[0]
        columns = player_input[1]
        coordinates = (rows, columns)
        rows = coordinates[0]
        try:
            columns = int(coordinates[1])
        except ValueError:
            columns = None
        if rows.upper()  in ['A','B','C','D', 'E', 'F', 'G','H', 'I', 'J'] and columns in range(1,size):
            return True
    else:
        return False
    
def check_if_position_empty(player_coordinates, player_board):
    if player_board[int(player_coordinates[0])][int(player_coordinates[1])] == 'O':
        return True
    else:
        return False
    
def get_player_coordinates_format(player_coordinate):
    rows_conversion_dict = {"A": 0, "B": 1, "C": 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,'H': 7, 'I': 8, 'J': 9}
    row = rows_conversion_dict[player_coordinate[0].upper()]
    column = int(player_coordinate[1])-1
    player_coordinates_format = f"{str(row)}{str(column)}"
    return player_coordinates_format


def get_valid_input(player_coordinates, player_board, ship_size): 
    player_coordinates = ask_for_input(ship_size)
    while check_if_position_empty(player_coordinates, player_board) == False or is_valid_input(player_coordinates, ship_size) == False:
        player_coordinates = ask_for_input(ship_size)
        if check_if_position_empty(player_coordinates, player_board) == True and is_valid_input(player_coordinates, ship_size) == True:
            return get_player_coordinates_format(player_coordinates)

def ship_proximity():
    #horizontal or ventical, regardless of corners
    pass

def get_ships_dict(ships_dict):
    player_ships = []
    for x in range(1, (len(ships_dict)+1)): 
        while x == 1 and ships_dict[1]>0:
            shiplocation1 = input("please provide ship coordinates(ship size is 1) in format like A1: ")
            single_ship = [shiplocation1]
            player_ships.append(single_ship)
            ships_dict[1] -=1
        while x == 2 and ships_dict[2]>0:
            shiplocation1 = input("please provide ship coordinates(ship size is 2) in format like A1: ")
            shiplocation2 = input("please provide ship coordinates(ship size is 2) in format like A1: ")
            single_ship = [shiplocation1, shiplocation2]
            player_ships.append(single_ship)
            ships_dict[2] -=1
        while x == 3 and ships_dict[3]>0:
            shiplocation1 = input("please provide ship coordinates(ship size is 3) in format like A1: ")
            shiplocation2 = input("please provide ship coordinates(ship size is 3) in format like A1: ")
            shiplocation3 = input("please provide ship coordinates(ship size is 3) in format like A1: ")
            single_ship = [shiplocation1, shiplocation2,shiplocation3]
            player_ships.append(single_ship)
            ships_dict[3] -=1
        while x == 4 and ships_dict[4]>0:
            shiplocation1 = input("please provide ship coordinates(ship size is 4) in format like A1: ")
            shiplocation2 = input("please provide ship coordinates(ship size is 4) in format like A1: ")
            shiplocation3 = input("please provide ship coordinates(ship size is 4) in format like A1: ")
            shiplocation4 = input("please provide ship coordinates(ship size is 4) in format like A1: ")
            single_ship = [shiplocation1, shiplocation2,shiplocation3, shiplocation4]
            player_ships.append(single_ship)
            ships_dict[4] -=1
    return player_ships


def what_ships():
    #creates variable with ship existing in game
    pass

def ship_placement():
    pass


def shooting_phase():
    pass

def ask_for_shot():
    pass

def is_shot_valid():
    pass

def hit_or_miss():
    pass

def is_ship_sunk():
    pass

def win_condition():
    pass

player1_board = get_empty_board()
player2_board = get_empty_board()
player1_shoots = get_empty_board()
player2_shoots = get_empty_board()






def main_logic():
    pass
