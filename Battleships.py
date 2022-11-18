
# https://github.com/HLGitHuber/Battleships/blob/Adam/Battleships.py
def get_empty_board(board_size):
    return  [['O' for _ in range(board_size)] for _ in range(board_size)]
def ask_for_input(ship_size):
    coordinates = input(f"Please provide position in format ie. A1, size of current ship is {ship_size}: ")
    return coordinates
def display_board(game_board):
    alphabet = 'ABCDEFGHIJ'
    display_size = len(game_board)
    first_line = [str(x) for x in range(1, display_size+1)]
    print("  " + " ".join(first_line))
    for x in range(0, (display_size)):
        print(f'{alphabet[x]} {" ".join(game_board[x])}')
def is_valid_input(player_input, size):
    alphabet = 'ABCDEFGHIJ'
    if len(player_input) ==2:
        rows = player_input[0]
        columns = player_input[1]
        coordinates = (rows, columns)
        rows = coordinates[0]
        try:
            columns = int(coordinates[1])
        except ValueError:
            columns = None
        if rows.upper()  in [*alphabet[0:size]] and columns in range(1,size+1):
            return True
        else:
            return False
    else:
        return False
def check_if_position_empty(player_coordinates, player_board):
    try:
        if player_board[int(player_coordinates[0])][int(player_coordinates[1])] == 'O':
            return True
        else:
            return False
    except IndexError:
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

def check_for_adjacency_empty_left(player_board, coordinates):
    rows = int(coordinates[0])
    columns = int(coordinates[1])
    try:
        if player_board[rows][columns-1] == 'O':
            return True
        else:
            return False
    except IndexError:
        return True

def check_for_adjacency_empty_right(player_board, coordinates):
    rows = int(coordinates[0])
    columns = int(coordinates[1])
    try:
        if player_board[rows][columns+1] == 'O':
            return True
        else:
            return False
    except IndexError:
        return True

def check_for_adjacency_empty_top(player_board, coordinates):
    rows = int(coordinates[0])
    columns = int(coordinates[1])
    try:
        if player_board[rows+1][columns] == 'O':
            return True
        else:
            return False
    except IndexError:
        return True

def check_for_adjacency_empty_bottom(player_board, coordinates):
    rows = int(coordinates[0])
    columns = int(coordinates[1])
    try:
        if player_board[rows-1][columns] == 'O':
            return True
        else:
            return False
    except IndexError:
        return True

def check_if_adjecent_empty(player_board, coordinates):
    if check_for_adjacency_empty_right(player_board, coordinates) == True and check_for_adjacency_empty_left(player_board, coordinates) == True and check_for_adjacency_empty_top(player_board, coordinates) == True and check_for_adjacency_empty_bottom(player_board, coordinates)== True:
        return True
    else:
        return False

def get_direction():
    while True:
        direction = input('Please make a choice, if ship should go to the right , or downwards from your position (type R or D and press Enter): ')
        if direction.upper() == 'R':
            return 'R'
        elif direction.upper() == 'D':
            return 'D'

def move_coordinates_down(coordinates):
    column = int(coordinates[0])+1
    return (f'{str(column)}{coordinates[1]}')

def move_coordinates_right(coordinates):
    row = int(coordinates[1])+1
    return (f'{coordinates[0]}{str(row)}')

def place_ship_size_1(player_board, coordinates):
    player_board[int(coordinates[0])][int(coordinates[1])] = 'X'

def place_ship_size_2(player_board, coordinates, coordinates_2):
    player_board[int(coordinates[0])][int(coordinates[1])] = 'X'
    player_board[int(coordinates_2[0])][int(coordinates_2[1])] = 'X'

def ships_left_to_place(ships_dict, ship_size):
    print(f'You have {ships_dict[ship_size]} ship(s) of size {ship_size} left to place')

def get_ship_locations(player_board, ships_dict):
    board_size = len(player_board)
    for ship_size in range(1, len(ships_dict)+1):
        if ship_size == 1:
            while ships_dict[ship_size]>0:
                display_board(player_board)
                ships_left_to_place(ships_dict, ship_size)
                ship_location = ask_for_input(ship_size)
                if is_valid_input(ship_location, board_size) == False:
                    print('This seems to be wrong coordinate/wrong input/outside board')
                elif is_valid_input(ship_location, board_size) == True:
                    coordinates = get_player_coordinates_format(ship_location) #changes player input like A1 to coordinates like '00'
                    if check_if_position_empty(coordinates, player_board) == True and check_if_adjecent_empty(player_board, coordinates)==True:
                        place_ship_size_1(player_board, coordinates)
                        ships_dict[1] = ships_dict[1]-1
                    elif check_if_position_empty(coordinates, player_board) == False:
                        print('This position seems to be already occupied')
                    elif check_if_adjecent_empty(player_board, coordinates) == False:
                        print('This position seems to be too close to other ship')                
        if ship_size == 2:
            while ships_dict[ship_size]>0:
                display_board(player_board)
                ships_left_to_place(ships_dict, ship_size)
                ship_initial_location = ask_for_input(ship_size)
                if is_valid_input(ship_initial_location, board_size) == True:
                    coordinates = get_player_coordinates_format(ship_initial_location)
                    if check_if_position_empty(coordinates, player_board) == False:
                        print('This position seems to be already occupied')
                    elif check_if_adjecent_empty(player_board, coordinates) == False:
                        print('This position seems to be too close to other ship')
                    elif check_if_position_empty(coordinates, player_board) == True and check_if_adjecent_empty(player_board, coordinates)==True:
                        direction = get_direction()
                        if direction == 'R':
                            coordinates_2 = move_coordinates_right(coordinates)
                        if direction == 'D':
                            coordinates_2 = move_coordinates_down(coordinates)
                        if check_if_position_empty(coordinates_2, player_board) == False:
                            print('This direction seems to be outside of board')
                        elif check_if_adjecent_empty(player_board, coordinates_2) == False:
                            print('This direction would cause ship to be too close to other ship')
                        elif check_if_adjecent_empty(player_board, coordinates_2)==True and check_if_position_empty(coordinates_2, player_board) == True:
                            place_ship_size_2(player_board, coordinates, coordinates_2)
                            ships_dict[2] = ships_dict[2]-1

def clear_screen():
    import os
    os.system('cls')
def press_any_key():
    import msvcrt
    char = None
    print ('Press any key to continue')
    while not char:
        char = msvcrt.getch()
def end_of_ship_deployment():
    print('You have placed all of your ships')
    press_any_key()
    clear_screen()
    press_any_key()


def display_board_next_to_another(game_board1, game_board2):
    alphabet = 'ABCDEFGHIJ'
    display_size = len(game_board1)
    second_line = [str(x) for x in range(1, display_size+1)]
    print('   PLAYER 1         PLAYER 2')
    print("  " + " ".join(second_line)+"        "+" ".join(second_line))
    for x in range(0, (display_size)):
        print(f'{alphabet[x]} {" ".join(game_board1[x])}      {alphabet[x]} {" ".join(game_board2[x])}')

def shot_question():
    coordinates = input(f"Please make a shot in format (ie. A1): ")
    return coordinates
def shot_coordinates(board_size):
    coordinates = shot_question()
    while is_valid_input(coordinates, board_size) == False:
        print("Try to hit a board next time (Wrong input/data outside of board")
        coordinates = shot_question()
    return get_player_coordinates_format(coordinates)
def check_for_adjacency_ship_left(player_board, coordinates):
    rows = int(coordinates[0])
    columns = int(coordinates[1])
    try:
        if player_board[rows][columns-1] == 'X':
            return True
        else:
            return False
    except IndexError:
        return False
def check_for_adjacency_ship_right(player_board, coordinates):
    rows = int(coordinates[0])
    columns = int(coordinates[1])
    try:
        if player_board[rows][columns+1] == 'X':
            return True
        else:
            return False
    except IndexError:
        return False
def check_for_adjacency_ship_top(player_board, coordinates):
    rows = int(coordinates[0])
    columns = int(coordinates[1])
    try:
        if player_board[rows+1][columns] == 'X':
            return True
        else:
            return False
    except IndexError:
        return False
def check_for_adjacency_ship_bottom(player_board, coordinates):
    rows = int(coordinates[0])
    columns = int(coordinates[1])
    try:
        if player_board[rows-1][columns] == 'X':
            return True
        else:
            return False
    except IndexError:
        return False
def check_bigger_ship_hit(player_board, coordinates):
    if check_for_adjacency_ship_left(player_board, coordinates) == True or check_for_adjacency_ship_right(player_board, coordinates) == True or check_for_adjacency_ship_top(player_board, coordinates) == True or check_for_adjacency_ship_bottom(player_board, coordinates) == True:
        return True
    else:
        return False
def complete_sink_on_left(player_board, coordinates):
    rows = int(coordinates[0])
    columns = int(coordinates[1])
    try:
        if player_board[rows][columns-1] == 'H':
            player_board[rows][columns-1] ='S'
            player_board[rows][columns] = 'S'
            print('You sunk a ship')
    except IndexError:
        pass
def complete_sink_on_right(player_board, coordinates):
    rows = int(coordinates[0])
    columns = int(coordinates[1])
    try:
        if player_board[rows][columns+1] == 'X':
            player_board[rows][columns+1] ='S'
            player_board[rows][columns] = 'S'
            print('You sunk a ship')
    except IndexError:
        pass
def complete_sink_on_top(player_board, coordinates):
    rows = int(coordinates[0])
    columns = int(coordinates[1])
    try:
        if player_board[rows+1][columns] == 'X':
            player_board[rows+1][columns] ='S'
            player_board[rows][columns] = 'S'
            print('You sunk a ship')
    except IndexError:
        pass
def complete_sink_on_bottom(player_board, coordinates):
    rows = int(coordinates[0])
    columns = int(coordinates[1])
    try:
        if player_board[rows-1][columns] == 'X':
            player_board[rows-1][columns] ='S'
            player_board[rows][columns] = 'S'
            print('You sunk a ship')
    except IndexError:
        pass
def check_and_sink(player_board, coordinates):
    complete_sink_on_left(player_board, coordinates)
    complete_sink_on_right(player_board, coordinates)
    complete_sink_on_top(player_board, coordinates)
    complete_sink_on_top(player_board, coordinates)


def shot_sequence(target_board, game_board_shots): #for example if its player 1, it will be player2_board, player1_shots and coordinates from player1, game board is target board
    coordinates = shot_coordinates(len(target_board))
    rows = int(coordinates[0])
    columns = int(coordinates[1])
    if target_board[rows][columns] == 'O':
        game_board_shots[rows][columns] = 'M'
        print('You missed')
    elif target_board[rows][columns] == 'X':
        if check_bigger_ship_hit(target_board, coordinates) == False:
            game_board_shots[rows][columns] = 'S'
            target_board[rows][columns] = 'S'
            print('Ship sunk')
        elif check_bigger_ship_hit(target_board, coordinates) == True:
            game_board_shots[rows][columns] = 'H'
            target_board[rows][columns] = 'H'
            print('Ship hit')
            check_and_sink(game_board_shots, coordinates)

def win_condition(player_board):
    win_board = [item for sublist in player_board for item in sublist]
    if 'X' in win_board:
        return False
    else:
        return True

def game_main_logic():
    board_size = 5
    player1_board = get_empty_board(board_size)
    player2_board = get_empty_board(board_size)
    player1_shots = get_empty_board(board_size)
    player2_shots = get_empty_board(board_size)
    p1_ships_dict = {1: 1, 2: 1}
    p2_ships_dict = {1: 1, 2: 1}
    get_ship_locations(player1_board, p1_ships_dict)
    display_board(player1_board)
    end_of_ship_deployment()
    get_ship_locations(player2_board, p2_ships_dict)
    display_board(player2_board)
    end_of_ship_deployment()
    turn_count = 1
    turn_limit = 50
    while turn_count < turn_limit:
        if turn_count % 2 == 1:
            turn_count +=1
            print("It is player 1 shot")
            display_board_next_to_another(player1_shots, player2_shots)
            shot_sequence(player2_board, player1_shots)
            if win_condition(player2_board) == True:
                print('Player 1 won, gg')
                break
        elif turn_count % 2 == 0:
            turn_count +=1
            print("It is player 2 shot")
            display_board_next_to_another(player1_shots, player2_shots)
            shot_sequence(player1_board, player2_shots)
            if win_condition(player1_board) == True:
                print('Player 2 won, gg')
                break

game_main_logic()
