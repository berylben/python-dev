from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# A function that checks user's guess against actual answer
def check_answer(guess, answer, turns):
    """chexk answer against guess, returns the number of guesses left"""
    if guess > answer:
        print("Too high!")
        return turns - 1
    elif guess < answer:
        print("Too high!")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")

# A function that sets difficulty
def set_difficulty():
    level = input("Choose difficulty. Type 'easy' or 'hard'")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS    


# Choosing a random number between 1 and 100
def game():
    print("Wecome to the guessing game!")
    print("I am thinking of a number betwen 1 and 100")

    answer = randint(1,100)
    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number.")

    # Repeat guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts  remaining to guess the number")

    # Let the user guess a number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        # track the number at turns and reduce by 1 if they get it wrong
        if turns == 0:
            print("Youve run out of guesses and you lose")
            return
    

# Trac the number of turns and reduce by 1  if they get it wrong



game()
