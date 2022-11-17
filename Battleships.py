#BATTLESHIP GAME

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

def check_if_adjecent_empty(player_board, ship_location):
    rows = int(ship_location[0])
    columns = int(ship_location[1])
    try:
        if player_board[rows][columns-1] == 'O': #sprawdza w lewo
            if player_board[rows][columns+1] == 'O': #sprawdza w prawo
                if player_board[rows+1][columns] == 'O': #sprawdza na górze
                    if player_board[rows-1][columns] == 'O': #sprawdza na dole
                        return True
        return False
    except IndexError:
        return True

def get_direction():
    direction = input('Please make a choice, if ship should go to the right , or downwards from your position (type R or D and press Enter): ')
    while direction.upper != "R" or direction.upper != "D":
        direction = input('Please make a choice, if ship should go to the right , or downwards from your position (type R or D and press Enter: ')
    return direction.upper()

def get_ship_locations(player_board, ships_dict, board_size):
    for ship_size in range(1, len(ships_dict)+1):
        if ship_size == 1:
            while ships_dict[1]>0:
                ship_location = ask_for_input(ship_size)
                if is_valid_input(ship_location, board_size) == True:
                    coordinates = get_player_coordinates_format(ship_location) #changes player input like A1 to coordinates like '00'
                    if check_if_position_empty(coordinates, player_board) == True and check_if_adjecent_empty(player_board, coordinates)==True:
                        player_board[int(coordinates[0])][int(coordinates[1])] = 'X'
                        # player_ships.append(coordinates)
                        ships_dict[1] = ships_dict[1]-1
                else:
                    print('This seems to be a wrong coordinate')



BOARD_SIZE = 5
MAX_TURNS = 50

# board_player1 = [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]
board_player1 = get_empty_board(BOARD_SIZE)
board_player2 = get_empty_board(BOARD_SIZE)
shooting_board_player1 = get_empty_board(BOARD_SIZE)
shooting_board_player2 = get_empty_board(BOARD_SIZE)

player1_ships = [['00'], ['44'], ['22','23'], ['30', '40', '20']]

player2_ships = [['00'], ['44'], ['22','23'], ['30', '40', '20']]

ships_dict = {1:1, 2:0, 3:0, 4:0}

def win_condition(player_board):
    board_size = len(player_board)
    for row in range(board_size):
        for col in range(board_size):
            if player_board[row][col] == 'X':
                return False
    return True

def ask_for_shot():
    global shot
    shot = input('Choose the place to shoot: ')
    return shot

def shooting_phase():
    turn_count = 1
    while turn_count < MAX_TURNS:
        print("Player 1 shooting board:")
        display_board(shooting_board_player1)
        print("Player 2 shooting board")
        display_board(shooting_board_player2)
        if turn_count % 2 == 1:
            make_a_shot(player2_ships, board_player2, shooting_board_player1)
            if win_condition(board_player2):
                print("Player 1 wins!")
                quit()
            turn_count += 1
        elif turn_count % 2 == 0:
            make_a_shot(player1_ships, board_player1, shooting_board_player2)
            if win_condition(board_player1):
                print("Player 2 wins!")
                quit()
            turn_count+= 1
        
    else:
        print("No more turns, it's a draw!")
        quit()
    
def make_a_shot(player_ships, player_board, player_shooting_board):
    x = True
    while x:
        shot = ask_for_shot()
        if is_valid_input(shot, BOARD_SIZE):
            shot = get_player_coordinates_format(shot)
            for ship in range(len(player_ships)):
                if shot in player_ships[ship]:
                    player_board[int(shot[0])][int(shot[1])] = 'H'
                    player_shooting_board[int(shot[0])][int(shot[1])] = 'H'
                    player_ships[ship].remove(shot)
                    if len(player_ships[ship]) == 0:
                        player_board[int(shot[0])][int(shot[1])] = 'S'
                        player_shooting_board[int(shot[0])][int(shot[1])] = 'S'
                        rows = int(shot[0])
                        columns = int(shot[1])
                        if player_board[rows][columns-1] == 'H': #sprawdza w lewo
                            player_board[rows][columns-1] = 'S'
                            player_shooting_board[rows][columns-1] = 'S'
                        elif player_board[rows][columns+1] == 'H': #sprawdza w prawo
                            player_board[rows][columns+1] = 'S'
                            player_shooting_board[rows][columns+1] = 'S'
                        elif player_board[rows+1][columns] == 'H': #sprawdza na górze
                            player_board[rows+1][columns] = 'S'
                            player_shooting_board[rows+1][columns] = 'S'
                        elif player_board[rows-1][columns] == 'H': #sprawdza na dole
                            player_board[rows-1][columns] = 'S'
                            player_shooting_board[rows-1][columns] = 'S'

                        print("You've sunk a ship!")
                        return
                    print("You've hit a ship!")
                    return
                
            player_board[int(shot[0])][int(shot[1])] = 'M'
            player_shooting_board[int(shot[0])][int(shot[1])] = 'M'
            print("You've missed!")
            x = False
            return 
        else:
            print("Incorrect coordinates")


shooting_phase()


    


# remove z listy player_ships gdy trafi statek, jezeli 0 w tej liscie to zatopiony
# albo sprawdza boarda jezeli w poblizu nie ma kolejnego X to zatopiony

