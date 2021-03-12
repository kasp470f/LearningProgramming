import random
import os
import sys
from game.deck import deckGen
from game.hand import handCount
from game.hand import printHand

clear = lambda: os.system('cls')

# Generate Deck and Shuffle
deck = deckGen() 
random.shuffle(deck)

# Player hand
playerhand = []
playerhand.append(deck.pop())
playerhand.append(deck.pop())

# Draw and hit phase
while handCount(playerhand) < 21:
    print(printHand(playerhand) + " = " + str(handCount(playerhand)))
    print("Do you want to hit? (y/n)")
    answer = input()
    if answer == "y":
        playerhand.append(deck.pop())
    else:
        break

if handCount(playerhand) > 21:
    print("You Busted at " + str(handCount(playerhand)))

clear()
print("Player Hand: " + printHand(playerhand) + " = " + str(handCount(playerhand)))


# Dealer hand
dealerhand = []
dealerhand.append(deck.pop())
dealerhand.append(deck.pop()) 

if handCount(dealerhand) < 17:
    dealerhand.append(deck.pop())
elif handCount(dealerhand) > 21:
    print("Dealer Busted at " + str(handCount(dealerhand)))

print("Dealer Hand: " + printHand(dealerhand) + " = " + str(handCount(dealerhand)))

if handCount(playerhand) <= 21 and handCount(dealerhand) <= 21:
    if handCount(playerhand) > handCount(dealerhand):
        print("You won")
    elif handCount(playerhand) < handCount(dealerhand):
        print("You lose")
    else:
        if len(playerhand) < len(dealerhand):
            print("You won")
        elif len(playerhand) > len(dealerhand):
            print("You lost")
        else:
            print("It's a draw")
        

elif handCount(dealerhand) > 21:
    print("You won")
else:
    print("You lose")
 
input("\nPress any button to close")
