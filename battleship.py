shots = []
board = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
ships_start = []
ships = []


def ask_for_shot():
    shot = input('Choose the place to shoot')
    return shot

def is_shot_valid(shot):
    if shot not in board:
        print ("Your shot is outside the board, try again")
        is_shot_valid(shot)
    elif shot in shots:
        print ("You have already shot there, try again")
        is_shot_valid(shot)
    else :
        shots.append(shot)
        return True


def hit_or_miss(shot):
    if shot in ships:
        print("You hit enemy ship!")
        ships.remove(shot)
    else:
        print('You missed the shot')


