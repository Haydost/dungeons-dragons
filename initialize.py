from random import sample
from typing import List


def initialize_grid(n: int) -> List:
    """ This function receives the input size of grid,
    chooses a random place for your starting position and
    draw your battle filed on the terminal and returns a list
    of useful information about the current state of player """
    row_0 = " _"*n + " "
    row_i = (("|_"*n) + "|")*n
    rows_str = row_0 + row_i
    rows_list = [i for i in rows_str]
    available_places_indexes = [i for i in range(
        len(rows_list)) if (rows_list[i] == "_" and i > (2*n+1))]
    random_indexes = sample(available_places_indexes, 3)
    player_index = random_indexes[0]
    dragon_index = random_indexes[1]
    dungeon_index = random_indexes[2]
    rows_list[player_index] = "X"
    rows_str_new = "".join(rows_list)
    for i in range(n+1):
        row_i_new = f"{rows_str_new[(i)*(2*n+1):(i+1)*(2*n+1)]}"
        print(row_i_new)

    locations = [(x, y) for x in range(1, n+1) for y in range(1, n+1)]
    cordinations = dict(zip(available_places_indexes, locations))
    print(f"\nYou are currently located in room: {cordinations[player_index]}")
    limitations = []
    if cordinations[player_index][0] == 1:
        limitations.append('UP')
        if cordinations[player_index][0] == 1 and\
                cordinations[player_index][1] == 1:
            limitations.append('LEFT')
        elif cordinations[player_index][0] == 1 and\
                cordinations[player_index][1] == n:
            limitations.append('RIGHT')
    elif cordinations[player_index][0] == n:
        limitations.append('DOWN')
        if cordinations[player_index][0] == n and\
                cordinations[player_index][1] == 1:
            limitations.append('LEFT')
        elif cordinations[player_index][0] == n and\
                cordinations[player_index][1] == n:
            limitations.append('RIGHT')
    elif cordinations[player_index][1] == 1:
        limitations.append('LEFT')
        if cordinations[player_index][1] == 1 and\
                cordinations[player_index][0] == 1:
            limitations.append('UP')
        elif cordinations[player_index][1] == 1 and\
                cordinations[player_index][0] == n:
            limitations.append('DOWN')
    elif cordinations[player_index][1] == n:
        limitations.append('RIGHT')
        if cordinations[player_index][1] == n and\
                cordinations[player_index][0] == 1:
            limitations.append('UP')
        elif cordinations[player_index][1] == n and\
                cordinations[player_index][0] == n:
            limitations.append('DOWN')
    else:
        print("You can move in all four directions")
    if limitations:
        if len(limitations) == 1:
            print(f"You can't move '{limitations[0]}'")
        else:
            print("You can't move either '{}' and '{}'".format(
                limitations[0], limitations[1]))
    valuable_info = [(player_index, dragon_index, dungeon_index),
                     limitations, cordinations, rows_list,
                     available_places_indexes]
    return (valuable_info)
