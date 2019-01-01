# This line of code tells the test where to find the definitions of all the objects in the game.
import game

print("\n\n === Game Start ===\n\n")

## Create the first two players, Jose and Lora. Initialize them with usernames.
jose = game.Player("Jverdugo337")
lora = game.Player("LHines868")

## prompt the player to press enter in order to run the next part of the code.
print("Press enter to begin.")
input()

## Have each player attack the other.
jose.attack(lora)
lora.attack(jose)