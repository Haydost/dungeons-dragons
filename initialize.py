from random import sample
from typing import Tuple, List


def make_grid(n: int) -> List[Tuple[int, int, int] | List[str]]:
    """ This function receives the input size of the grid as "n",
    chooses a random place for your starting position and
    draw your battle filed on the terminal and returns a list
    of useful information about the game situation. """

    first_row_pattern = " _"*n + " "
    other_rows_pattern = (("|_"*n) + "|")*n
    rows_str = first_row_pattern + other_rows_pattern
    rows_list = list(rows_str)

    available_places_indexes = [i for i in range(
        len(rows_list)) if (rows_list[i] == "_" and i > (2*n+1))]

    random_indexes = sample(available_places_indexes, 3)
    player_index = random_indexes[0]
    dragon_index = random_indexes[1]
    dungeon_index = random_indexes[2]

    rows_list[player_index] = "X"

    rows_str = "".join(rows_list)

    locations = [(x, y) for x in range(1, n+1) for y in range(1, n+1)]
    cordinations = dict(zip(available_places_indexes, locations))
    limitations = []

    def draw_grid():
        for i in range(n+1):
            others_row_new = "{}".format(
                rows_str[(i)*(2*n+1):(i+1)*(2*n+1)])
            print(others_row_new)
        print("\nYou are currently located in room: {}".format(
            cordinations[player_index]))
    draw_grid()

    def check_limitation():
        if cordinations[player_index][0] == 1:
            limitations.append('UP')
            if cordinations[player_index][0] == 1 and \
                    cordinations[player_index][1] == 1:
                limitations.append('LEFT')
            elif cordinations[player_index][0] == 1 and \
                    cordinations[player_index][1] == n:
                limitations.append('RIGHT')
        elif cordinations[player_index][0] == n:
            limitations.append('DOWN')
            if cordinations[player_index][0] == n and \
                    cordinations[player_index][1] == 1:
                limitations.append('LEFT')
            elif cordinations[player_index][0] == n and \
                    cordinations[player_index][1] == n:
                limitations.append('RIGHT')
        elif cordinations[player_index][1] == 1:
            limitations.append('LEFT')
            if cordinations[player_index][1] == 1 and \
                    cordinations[player_index][0] == 1:
                limitations.append('UP')
            elif cordinations[player_index][1] == 1 and \
                    cordinations[player_index][0] == n:
                limitations.append('DOWN')
        elif cordinations[player_index][1] == n:
            limitations.append('RIGHT')
            if cordinations[player_index][1] == n and \
                    cordinations[player_index][0] == 1:
                limitations.append('UP')
            elif cordinations[player_index][1] == n and \
                    cordinations[player_index][0] == n:
                limitations.append('DOWN')
        else:
            print("\nYou can move in all four directions")
        if limitations:
            if len(limitations) == 1:
                print(f"You can't move '{limitations[0]}'\n")
            else:
                print("You can't move either '{}' and '{}'\n".format(
                    limitations[0], limitations[1]))
    check_limitation()

    return [(player_index, dragon_index, dungeon_index), limitations]
