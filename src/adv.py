
from room import Room
from player import Player
from items import Items

#Declare all the items

items = {
    'sword': Items("RustySword", """A rusty sword lies here."""),

    'coin': Items("GoldCoin", """There is a small gold coin here. Might be valuable."""),

    'key': Items("key", """A dingy key lies here. Might be useful."""),

    'rations': Items("rations", """Some old military rations are here. Hopefully they haven't expired."""),

    'hookshot': Items("hookshot", """A spring-loaded, trigger-pulled hook attached to
        lengthy chains. It can can attack enemies at a distance, 
        retrieve remote items, and attach onto certain surfaces 
        (like wood) to pull you across large distances."""),

    'chest': Items("chest", """A dusty old chest lies in the corner here.""")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",[items['sword']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",[items['sword'],items['key']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",[items['hookshot'],items['rations']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",[items['coin'],items['chest']]),
}






# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_1 = Player("Player_1", room["outside"])

# Write a loop that:
while True:
    player_1.current_room
    # * Prints the current room name
    print("\nYou are now in room:\n", player_1.current_room.name)
    # * Prints the current description (the textwrap module might be useful here).
    print("Description:\n", player_1.current_room.description)
    player_1.current_room.item_finder()

# * Waits for user input and decides what to do.
    print("\nWhich direction would you like to move?")
    cmd = input("Press 'n', 's,', 'e', 'w' or ('q' to quit the game):")

    try:
        verb, noun = cmd.split(" ", 1)
    except:
        verb, noun = ' ', ' '
    
        

# If the user enters "q", quit the game.
    if cmd == 'q':
        print("Thanks for playing.  Have a nice day!")
        break

# If the user enters a cardinal direction, attempt to move to the room there.

    if cmd == 'n':
        print("\nWalking north...\n")
        if player_1.current_room.n_to is None:
            print("****There is no room to the North of you, select different direction.****")
        else:
            player_1.current_room = player_1.current_room.n_to
                
    elif cmd == 's':
        print("\nWalking south...\n")
        if player_1.current_room.s_to is None:
            print("****There is no room to the South of you. Select a different direction.****")
        else:
            player_1.current_room = player_1.current_room.s_to
    elif cmd == 'e':
        print("\nWalking east...\n")
        if player_1.current_room.e_to is None:
            print("****There is no room to the East of you. Select a different direction.****")
        else:
            player_1.current_room = player_1.current_room.e_to
    elif cmd == 'w':
        print("\nWalking west...\n")
        if player_1.current_room.w_to is None:
            print("****There is no room to the West of you. Select a different direction.****")
        else:
            player_1.current_room = player_1.current_room.w_to
    elif cmd == 'i':
        player_1.check_inventory()
    elif verb == 'get':
        player_1.add_item(noun)
    elif verb == 'drop':
        player_1.drop_item(noun)
# Print an error message if the movement isn't allowed.
    else:
        print ("This movement is not allowed.")

