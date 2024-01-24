# step 1

# TODO-1 randomly assign a word from the word_list and assign it a variable chosen_word
import random
import hangman_words

chosen_word = random.choice(word_list)
print(f"ptsss, the chosen word is {chosen_word}")


# create an empty list called display
# for each letter in the chosen_word, add a "_" to diplay
#for example if the chosen word is apple there should be 5 "_" so the dispaly should be ["_", "_", "_", "_", "_",] representing each letter to guess 
lives = 
# print blanks
display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)
    

# TODO-2 Ask the user to chose a letter and assing the letter to a variable called guess and convert the letter to lower case

end_of_game = False

while not end_of_game:



    guess = input("Guess a letter:").lower()
# TODO-3 check if the letter the user guessed(guess) is one of the letter in the chosen word
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    if letter == guess:
        display[position] = letter
print(display)

if "_" not in display:
    end_of_game = True
print(" You win!")

