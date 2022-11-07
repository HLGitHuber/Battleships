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

# is ship placement valid
def valid_input():
    pass

def ship_proximity():
    #horizontal or ventical, regardless of corners
    pass

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

def win_condition(player_board):
    if is_all_ship_sunk(player_board):
        return True
    else:
        return False

def is_all_ship_sunk(player_board):
    board_size = len(player_board)
    for row in range(board_size):
        for col in range(board_size):
            if player_board[row][col] == 'X':
                return False
    return True
    
    

player1_board = get_empty_board(5)
player2_board = get_empty_board(5)
player1_shoots = get_empty_board(5)
player2_shoots = get_empty_board(5)




def main_logic():
    pass

# player1_board[0][0] = 'X'

# print(player1_board)

# print(win_condition(player1_board))
