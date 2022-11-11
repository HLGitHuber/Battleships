# is ship placement valid
def valid_input(ships, board):
    
    for ship in range(len(ships)):
        if ships[ship][0] > len(board)-1 or ships[ship][1] > len(board)-1:
            return False
        elif board[ships[ship][0]][ships[ship][1]] in list('X'):
            return False
    return True

def get_empty_board(size):
    return  [['O' for _ in range(size)] for _ in range(size)]

board = get_empty_board(10)

board[4][4] = 'X'

# player1_ships = [[0,0], [4,3], [2,2], [2,3], [3,0], [9,0]]

player1_ship = [[4,3]]

print(valid_input(player1_ship, board))

