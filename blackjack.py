# Create a deal_card() function that uses the list below to return a random card
import random

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Creat a function called calculate_score() that takes a list of cards as input and returns  the score
def calculate_score(cards):
    """Take a list of cards and  return the score calculate from the cards"""
# inside calculate_score check for the blackjack(a hand with only 2 cards: ace + 10) and return 0 instead of actual score, 0 will represent blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0

# inside calculate_score() check for an 11(ace). if the score is already over 21, remove the 11 and replace it with a 1, you might need to look up append() and remove()
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards) 

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "Lose!, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over, you lose!"
    elif computer_score > 21:
        return "Opponent went over, You win"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"
# Deal the user and computer 2 cards each using deal_card()
def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    # for a loop to run twice
    for _ in range(2):
        # new_card = deal_card()
        # user_cards.append(new_card)
        user_cards.append(deal_card)
        computer_cards.append(deal_card)

    while not is_game_over:    

        user_score =  calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first card: {computer_score[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:   
                is_game_over = True 


    while computer_score != 0 and computer_score > 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f" Your final hand: {user_cards}, final score: {user_score}")
    print(f" Computer's finsl hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))    


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()