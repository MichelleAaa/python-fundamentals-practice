import random

high_score = 0

def dice_game():
    global high_score
    while True:
        print(f'Current High Score: {high_score}\n1) Roll Dice\n2) Leave Game')
        choice = input('Enter your choice: ')
    
        if choice == "1":
            roll1 = random.randint(1, 6)
            print(f"\nYou roll a... {roll1}")
            roll2 = random.randint(1, 6)
            print(f"You roll a... {roll2}\n")
            total = roll1 + roll2
            print(f"You have rolled a total of: {total}\n\nNew high score!\n")
            high_score += total
        if choice == "2":
            break

dice_game()
