#import modules
import random
from hangman_words import list_easy_words, list_hard_words
from hangman_art import stages, logo, lost_logo, congrats_logo

#Pring logo of the game
print(logo)

#Prompts a user to select the difficulty level
difficulty_level = input("Choose the level of difficulty (easy or hard): ").lower()

#Choose a random word list based on the difficulty level
chosen_word_list = random.choice(list_easy_words) if difficulty_level == "easy" else random.choice(list_hard_words)

#Determine the length of the chosen word
word_length = len(chosen_word_list)

#Initialize game variables
end_of_game = False
lives = 6

#Testing code
print(f'The randomly chosen word: {chosen_word_list}.')

#Create blanks

# Initialize a list to display guessed letters and underscores
display = ["_"] * word_length

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word_list[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong
    if guess not in chosen_word_list:
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(lost_logo)

    #Join all the elements in the list and turn it into a string
    print(f"{' '.join(display)}")

    #Check if user has got all letters
    if "_" not in display:
        end_of_game = True
        print(congrats_logo)

    # Display the appropriate hangman art based on remaining lives
    print(stages[lives])