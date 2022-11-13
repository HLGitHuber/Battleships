shots = []
board = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
ships_start = []
ships = ["A1"]

def ask_for_shot():
    shot = input('Choose the place to shoot ')
    return shot

def is_shot_valid(ask_for_shot):
    if ask_for_shot not in board:
        print ("Your shot is outside the board, try again")
        ask_for_shot()
    elif ask_for_shot in shots:
        print ("You have already shot there, try again")
        ask_for_shot()
    else :
        shots.append(ask_for_shot)
        return True


def hit_or_miss(ask_for_shot):
    if ask_for_shot in ships:
        print("You hit enemy ship!")
        ships.remove(ask_for_shot)
    else:
        print('You missed the shot')



