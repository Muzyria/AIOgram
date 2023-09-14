koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4

# from itertools import count
import random

random.shuffle(koloda)

print("Do you play in game ?")
count_player = 0
count_bot = 0

while True:
    choice = input("Do you need a card? y/n\n")
    if choice == "y":
        current = koloda.pop()
        print("You pick a card %d" % current)
        count_player += current
        if count_player > 21:
            print("You loss, your count = %d" % count_player)
            break
        # elif count_player == 21:
        #     print("You WIN")
        #     break
        else:
            print("You have a %d" % count_player)
    elif choice == "n":
        while True:
            current = koloda.pop()
            print("I pick a card %d" % current)
            count_bot += current
            if count_bot > 21:
                print("I loss, your count = %d" % count_bot)
                break
            elif count_bot == 21 and count_player < 21:
                print("I WIN")
                break
            else:
                print("I have a %d" % count_bot)
print("Good bye")
