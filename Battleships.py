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
    if len(player_input) ==2:
        rows = player_input[0]
        columns = player_input[1]
        coordinates = (rows, columns)
        rows = coordinates[0]
        try:
            columns = int(coordinates[1])
        except ValueError:
            columns = None
        if rows.upper()  in ['A','B','C','D', 'E', 'F', 'G','H', 'I', 'J'] and columns in range(1,size+1):
            return True
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

player1_ships =[]

def place_ship_size_1(player_board, coordinates):
    player_board[int(coordinates[0])][int(coordinates[1])] = 'X'

def place_ship_size_2(player_board, coordinates, coordinates_2):
    player_board[int(coordinates[0])][int(coordinates[1])] = 'X'
    player_board[int(coordinates_2[0])][int(coordinates_2[1])] = 'X'



def get_ship_locations(player_board, ships_dict, board_size, player_ships):
    for ship_size in range(1, len(ships_dict)+1):
        if ship_size == 1:
            while ships_dict[ship_size]>0:
                display_board(player_board)
                ship_location = ask_for_input(ship_size)
                if is_valid_input(ship_location, board_size) == True:
                    coordinates = get_player_coordinates_format(ship_location) #changes player input like A1 to coordinates like '00'
                    if check_if_position_empty(coordinates, player_board) == True and check_if_adjecent_empty(player_board, coordinates)==True:
                        place_ship_size_1(player_board, coordinates)
                        player_ships.append([coordinates])
                        ships_dict[1] = ships_dict[1]-1
                    else:
                        print('This seems to be a wrong coordinate')
        if ship_size == 2:
            while ships_dict[ship_size]>0:
                display_board(player_board)
                ship_initial_location = ask_for_input(ship_size)
                if is_valid_input(ship_initial_location, board_size) == True:
                    coordinates = get_player_coordinates_format(ship_initial_location)
                    direction = get_direction()
                    if check_if_position_empty(coordinates, player_board) == True and check_if_adjecent_empty(player_board, coordinates)==True:
                        if direction == 'R':
                            coordinates_2 = move_coordinates_right(coordinates)
                            if check_if_adjecent_empty(player_board, coordinates_2)==True and check_if_position_empty(coordinates_2, player_board) == True:
                                place_ship_size_2(player_board, coordinates, coordinates_2)
                                ships_dict[2] = ships_dict[2]-1
                                player_ships.append([coordinates, coordinates_2])
                        if direction == 'D':
                            coordinates_2 = move_coordinates_down(coordinates)
                            if check_if_adjecent_empty(player_board, coordinates_2)==True and check_if_position_empty(coordinates_2, player_board) == True:
                                place_ship_size_2(player_board, coordinates, coordinates_2)
                                ships_dict[2] = ships_dict[2]-1
                                player_ships.append([coordinates, coordinates_2])
                    else:
                        print('This seems to be a wrong coordinate')     
