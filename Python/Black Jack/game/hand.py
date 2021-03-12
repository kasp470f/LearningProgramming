import re

def handCount(hand):
    count = 0
    for x in hand:
        if "T" in x or "J" in x or "Q" in x or "K" in x:
            count += 10
        elif "A" in x and count+11 > 21:
            count += 1
        elif "A" in x:
            count += 11
        else:
            count += int(re.sub('[♠♣♥♦]', '', x))

    return count

def printHand(hand):
    return "[" + "] [".join(hand) + "]"