# Play a Command-Line Video Game.

### Try it out

The code in this repository is actually already a working game. The trouble is, it's pretty boring. To see it run, type `python test.py` in terminal and see what happens.

Below is a list of challenges - ways you could make this game a lot better. Before you look at those suggested ways to make the game better, consider what you notice about the game. Take a moment and write down everything you might do to make the game more fun, more fair, and more interesting.

### Possible Improvements

1. Right now, you may notice that characters can reach negative health. Run the program a few times and you'll eventually see this happen.
    * Give each player an instance variable called `self.alive` that is a boolean which starts off set to `True`.
    * Remove the line of code that decreases an opponent's health, and instead write a more precise method called `decrease_health_by(self, damage)` that checks to see whether the damage will put the player at or below zero. If the damage will put them below zero, set their `self.alive` status to `False`, and set their health to zero (because negative health doesn't make much sense.)
---

2. Right now, the program is hard-coding each attack, but most videogames would probably render each entire fight as a whole object all its own.
    * In the game.py file, define a `Battle` class, which initializes with two arguments (player1, player2).
    * Define a `start` method for the Battle class that repeats until one of the two players reaches zero health. You'll probably want to use a `while` loop. (Try googling "while loop python" to find out about them.)
    * If we do this successfully, we could run an entire battle with the following lines of code in our test.py file:
  ```python

  first_fight = game.Battle(jose, lora)
  first_fight.start()
  ```
---

3. Right now, the player has no choice about what to do. The only method a Player has that can do anything is the "attack(self, target)" method. Let's give them some other options.
    * We'll need to modify the Battle class `start` method to ask the user what they want to do every turn, and then run an `input()` to see what they say.
    * We'll also need to add some more methods to the Player class. Some ideas for those methods:
      * `rest(self)` could have the player restore health that turn instead of attacking.
      * `special_attack(self, target)` could have the player do EXTRA damage that turn, but then need to skip their next turn.
      * `run_away(self)` could end the battle if you think you might lose, though this should maybe be a Battle method, and not a Player method.
---

4. Right now, the attacks are predictable, so if the player knows the numbers, there isn't any risk at all. Is there a way to add a little more randomness and chance to the `attack(self, target)` method than we have right now?
---

5. At the end of each fight, nothing happens to make the fight worthwhile. Should players get gold? Should they get experience points that contribute towards a level up?
---

6. Right now, the players' stats are set in stone. If a player levels up, their stats should go up too. Let's write a more specific `level_up` method for our Player class that in some way increases player stats when they level up.
    * Now we've created *another* problem. If the main character levels up, the enemies get too easy. As you get more powerful, the enemies should too, right?
---

7. Most fighting games have two types of items:
    * Consumable items like health potions can only be used once and then they disappear.
    * Equipment like swords or helmets boost certain stats while they are equipped, but you can only equip one sword or helmet at a time - equipping a new one means that your old one is automatically taken off.
    * If we're going to have items, we probably also need a shop where we can buy them.
    * Each player should probably also have a `self.items` list where their items can be stored.
---

8. Our Players can currently only attack each other. We should consider making an `Enemy` class to generate opponents for them. This class should have a lot of the same properties as a Player (like `self.strength` and `self.ame` etc.) but we should maybe also be able to stipulate how powerful that enemy is.
    * For example, `Enemy("Goblin", 1)` could create an enemy named Goblin that fights with similar strength to a level 1 player, and `Enemy("Troll", 7)` could be a more powerful enemy that's meant to be a challenge for a level 7 player.
---

9. Our game is getting big. It probably makes sense for us to make an entire class to hold the game. Just like our Battle class holds two characters, we should maybe make a `Game` class.
    * This game should allow our Players to choose what they want to do. If they want to start a Battle, we've already got a class for that.
    * The game could also allow our Players to visit a shop, go on training missions, etc.
