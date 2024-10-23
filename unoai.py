# code by David Hack and James Combista and AI
# implemented +2 and Skip Turn

import random


def start_game():
    colours = ("Red", "Yellow", "Green", "Blue")
    ranks = list(range(1, 11)) + ["+2"] + ["Skip Turn"]  # Add "+2" and Skip Turn as special ranks
    deck = [(rank, colour) for rank in ranks for colour in colours]
    random.shuffle(deck)

    p1 = [deck.pop(0) for _ in range(7)]
    p2 = [deck.pop(0) for _ in range(7)]

    central_card = deck.pop(0)
    main_loop(p1, p2, deck, central_card, 0)


def main_loop(p1, p2, deck, central_card, whose_turn):
    #count = 0
    while len(p1) > 0 and len(p2) > 0:

        print(f"\nPlayer {whose_turn + 1}'s turn, here is your hand {p1}")
        print(f"Central card is: {central_card}")


        ans = int(input("You have a choice. You can (0) draw or (1) play: "))
        if ans != 1 and ans != 0:
            for _ in range(100):
                ans = int(input("Bad Choice. You can (0) draw or (1) play: "))
                if ans == 1 or ans == 0:
                    break
        skip_turn = True


# +2 card code

            if ((player_card)[0]) == "+2":
                print("The opponent must draw 2 cards!")
                p2.append(deck.pop(0))
                p2.append(deck.pop(0))

# Skip turn card code ->
        
            if central_card[0] == "Skip Turn" and skip_turn == True:
                print("The opponent turn has been skipped!")
                whose_turn = (whose_turn + 1)
                skip_turn = False
                #count += 1

        elif ans == 0:
            draw_card = deck.pop(0)
            p1.append(draw_card)

        if skip_turn:
            ai_turn(p2, central_card, deck)

       # count += 1

        #whose_turn = (whose_turn + 1) % 2

def ai_turn(ai_hand, central, deck):
    # chances are, at the end of the ai_turn, they will have modified the central_card
    # This function should return the new central_card. 

    # 1st: is there a playable card in the ai_hand??
        # loop over all the cards in the ai_hand
        # if we find a valid card (using valid_play), we remove that card from the ai hand
        # and we place it on top of the central card
    # if no playable card is found, ai draws a card

    position_count = 0
    for card in range(len(ai_hand)):
        valid = valid_play(central, ai_hand)
        if valid:
            ai_card = ai_hand[card_count]
            central_card = ai_hand.pop(position_card)
            break
        position_count += 1


    return central

# Determining winner code
    if count % 2 == 0:
        print(f"Player 2 wins")
    else:
        print("Player 1 wins!!!1")

def valid_play(card1, card2):
    return card1[0] == card2[0] or card1[1] == card2[1]

start_game()
