############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import art

while True:
    answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if answer == "y":
        print(art.logo)
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        selected_cards = []
        selected_cards_computer = []
        random_card_1 = random.choice(cards)
        random_card_2 = random.choice(cards)
        selected_cards.append(random_card_1)
        selected_cards.append(random_card_2)
        random_card_computer = random.choice(cards)
        selected_cards_computer.append(random_card_computer)
        print(f"Your cards: [{random_card_1}, {random_card_2}], current score: {sum(selected_cards)}")
        print(f"Computer's first card: {random_card_computer}")
        while(sum(selected_cards) <= 21):
            if sum(selected_cards) == 21 and len(selected_cards) == 2:
              break
            answer_1 = input("Type 'y' to get another card, type 'n' to pass: ")
            if answer_1 == "y":
              random_card = random.choice(cards)
              selected_cards.append(random_card)
              if 11 in selected_cards and sum(selected_cards) > 21:
                selected_cards.remove(11)
                selected_cards.append(1)
              print(f"Your cards: {selected_cards}, current score: {sum(selected_cards)}")
              print(f"Computer's first card: {random_card_computer}")
            else:
                break
        while(sum(selected_cards_computer) < 17):
            random_card_computer_extra = random.choice(cards)
            selected_cards_computer.append(random_card_computer_extra)
              
        print(f"Your final hand: {selected_cards}, final score: {sum(selected_cards)}")
        print(f"Computer's final hand: {selected_cards_computer}, final score: {sum(selected_cards_computer)}")

        if sum(selected_cards) > 21:
          print("You went over. You lose 😤")
        elif sum(selected_cards) == 21:
          print("You win 😁")
        elif sum(selected_cards) > sum(selected_cards_computer):
          print("Opponent went over. You win 😁")
        elif sum(selected_cards) < sum(selected_cards_computer):
          print("You went over. You lose 😤")
        elif sum(selected_cards_computer) == 21:
          print("You went over. You lose 😤")
        elif sum(selected_cards) == sum(selected_cards_computer):
          print("Draw!!!")
    else:
        break