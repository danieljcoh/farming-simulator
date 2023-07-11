# By Daniel J. Cohen (Zink)
# Farming Simulator


# IMPORTS
from crop import Crop
from merchant import Merchant
from farmer import Farmer

# TURNS
TURN_COUNTER = 0


def introduction():
    print("Welcome to Farming Simulator. Let's get started.")
    name = input("What's your name? ")
    farming_name = f"Farmer {name}"

    # Instantiating the player (Farmer)
    player = Farmer(farming_name)

    print(f"Nice to meetchya {player.name}.")

    print()

    print("This here lovely little plot of land is yours.")
    print("Your land has 8 plots and each thing you grow takes up 1 plot. So you dur the math.")

    player.show_info()


# GAME PLAY
introduction()
# player.turn(turn_counter=TURN_COUNTER)






