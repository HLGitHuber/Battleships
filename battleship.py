shots = ["B2"]
board = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
ships_start = []
ships = ["A1"]

def ask_for_shot():
    global shot
    shot = input('Choose the place to shoot ')
    return shot


def is_shot_valid(ask_for_shot):
    while shot not in board:
        print ("Your shot is not valid, try again")
        is_shot_valid(ask_for_shot)
    while shot in shots:
        print ("You have already shot there, try again")
        is_shot_valid(ask_for_shot)
    while shot in board and shot not in shots :
        shots.append(shot)
        return True


def hit_or_miss(ask_for_shot):
    if shot in ships:
        print("You hit enemy ship!")
        ships.remove(shot)
    else:
        print('You missed the shot')
        

ask_for_shot()
print(shots)
print(ships)
print(is_shot_valid(ask_for_shot))
print(shots)
hit_or_miss(ask_for_shot)
print(ships)