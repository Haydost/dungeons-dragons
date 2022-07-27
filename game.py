from initialize import initialize_grid
from update_move import update_grid


print("_______Welcome to Dungeons and Dragons game_______")
print("____First you should determine the grid size____")
n = int(input("____Enter the grid size(n>1): "))
print("____Here is what your battle field looks like: ")
initial_information = initialize_grid(n)

current_index = initial_information[0][0]
dragon_index = initial_information[0][1]
dungeon_index = initial_information[0][2]
limited_places = initial_information[1]

print(" \nEnter 'QUIT' to exit!")
user_command = input("Which direction do you want to move? ")
while user_command != 'QUIT':
    if user_command == 'LEFT':
        if user_command not in limited_places:
            new_player_index = current_index - 2
            if new_player_index == dragon_index:
                print("Oh no! unfortunately you lost the game!")
                break
            elif new_player_index == dungeon_index:
                print("Hooray! you win the game!")
                break
            else:
                inf = update_grid(new_player_index, n)
                current_index = inf[0]
                limited_places = inf[1]

        else:
            print("You can't move in that direction as I said before!")
    elif user_command == 'RIGHT':
        if user_command not in limited_places:
            new_player_index = current_index + 2
            if new_player_index == dragon_index:
                print("Oh no! unfortunately you lost the game!")
                break
            elif new_player_index == dungeon_index:
                print("Hooray! you win the game!")
                break
            else:
                inf = update_grid(new_player_index, n)
                current_index = inf[0]
                limited_places = inf[1]
        else:
            print("You can't move in that direction as I said before!")
    elif user_command == 'UP':
        if user_command not in limited_places:
            new_player_index = current_index - (2*n+1)
            if new_player_index == dragon_index:
                print("Oh no! unfortunately you lost the game!")
                break
            elif new_player_index == dungeon_index:
                print("Hooray! you win the game!")
                break
            else:
                inf = update_grid(new_player_index, n)
                current_index = inf[0]
                limited_places = inf[1]
        else:
            print("You can't move in that direction as I said before!")
    elif user_command == 'DOWN':
        if user_command not in limited_places:
            new_player_index = current_index + (2*n+1)
            if new_player_index == dragon_index:
                print("Oh no! unfortunately you lost the game!")
                break
            elif new_player_index == dungeon_index:
                print("Hooray! you win the game!")
                break
            else:
                inf = update_grid(new_player_index, n)
                current_index = inf[0]
                limited_places = inf[1]
        else:
            print("You can't move in that direction as I said before!")
    else:
        print("You entered an invalid format please enter a valid command!")
        print("You are only allowed to use: 'UP', 'DOWN', 'LEFT', 'RIGHT' and 'QUIT'")
    print(" \nEnter 'QUIT' to exit!")
    user_command = input("Which direction do you want to move? ")
else:
    print("Byebye, See you soon!")
    exit()
