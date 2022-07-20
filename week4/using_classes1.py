"""
class Player:
    max_hp = 4000

# Create a variable named player1, then assigns to it an object instantiated from the Player class
player1 = Player()
print(player1.max_hp) - -- 4000

player2 = Player()
print(player2.max_hp) -- 4000

Player.max_hp = 5000
print(player1.max_hp) -- updated to 5000
print(player2.max_hp) -- updated to 5000
"""

class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.score = 0

player1 = Player("Aaron", 1200)
player2 = Player("Irene", 1300)

print("P1:", player1.name, " -- HP:", player1.hp, "-- SCORE: ", player1.score) # HP: 1200 - SCORE: 0
print("P2:", player2.name, " -- HP:", player2.hp, "-- SCORE: ", player2.score) # HP: 1300 - SCORE: 0

# Changing the value for one object created by a class doesn't change the same value for the other objects created by that same class. (It's only when you change the class value itself that it impacts all objects created by that class.)
player1.hp += 500
player1.score += 10
print("P1:", player1.name, " -- HP:", player1.hp, "-- SCORE: ", player1.score) # HP: 1700 - SCORE: 10
print("P2:", player2.name, " -- HP:", player2.hp, "-- SCORE: ", player2.score) # HP: 1300 - SCORE: 0 -- note that player2's details have remained the same. Only player1's hp and score have increased.



