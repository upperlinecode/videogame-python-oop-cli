import random

class Player:
  # Class variables that are shared among ALL players
  player_list = [] #Each time we create a player, we will push them into this list.
  player_count = 0

  def __init__(self, name):
    ## These instance variables should be unique to each user. Every user will HAVE a name, but each user will probably have a different name.
    self.name = name
    self.strength = random.randint(8, 12) # The stat values will all be random, but within a range of reasonableness
    self.defense = random.randint(8, 12)
    self.speed = random.randint(8, 12)
    self.max_health = random.randint(18, 24) # The max health value will be random, but higher than the others.
    self.health = self.max_health # Set the current health equal to the max health.
    print("Player " + self.name + " has entered the game. \n  Strength: " + str(self.strength) + "\n  Defense: " + str(self.defense) + "\n  Speed: " + str(self.speed) + "\n  Maximum health: " + str(self.max_health) + ".\n")
    ## We're going to also manipulate the two class variables - While each user has their own specific defense or strength, the users all share the class variables defined above this method.
    Player.player_list.append(self) ## The player will be added to the list of players.
    Player.player_count += 1 ## The player count should go up by one.
    print("There are currently " + str(Player.player_count) + " player(s) in the game.\n\n")

  def attack(self, target):
    ## With a CLI, we want to print out all the information our users need to play this game.
    ## Let's show the attacker and defender's names here.
    print("Player " + self.name + " attacks " + target.name + "!!!")
    print(self.name + "'s strength is " + str(self.strength) + " and target " + target.name + "'s defense is " + str(target.defense) + ".")
    ## The battle will go differently depending on who is stronger.
    if self.strength < target.defense:
      print("Due to the target's strong defense, the attack only does half damage...")
      damage = self.strength / 2
    elif self.strength > target.defense:
      print("Since the target is weaker than you are, the attack does double damage!")
      damage = self.strength * 2
    else:
      print("These players are evenly matched. The attack goes through normally.")
      damage = self.strength
    target.health -= damage
    ## Let's print out the new totals so that we know the final results of the fight.
    print(target.name + " now has " + str(target.health) + "/" + str(target.max_health) + " health remaining.\n\n")

  ## All other methods you code for the player class will fit best below this line.
  ## Make sure to indent instance methods properly so the computer knows they're part of the class.
