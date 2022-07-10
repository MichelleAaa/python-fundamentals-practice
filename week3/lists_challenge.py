import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    choice = input("Press enter to pick a card, or Q then enter to quit: ")
    if choice == 'Q':
        break
    if choice == "":
        card = diamonds.pop(diamonds.index(random.choice(diamonds)))
        hand.append(card)
        print('Your hand:', hand)
        print('Remaining cards:', diamonds)

if not diamonds:
    print('There are no more cards to pick.')