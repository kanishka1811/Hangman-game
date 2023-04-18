
import random
from hangman_words import word_list

from hangman_art import logo,stages
print(logo)


# word_list = ["grapes", "cherry", "strawberry", "mango", "kiwi", "pineapple"]

chosen_word=random.choice(word_list)

print(chosen_word)
display=[]

for x in chosen_word:
    display.append("_")

for x in display:
    print(x, end=" ")

print()

# for x in word_list:
#     display+="_"
#
# print(display)

# for x in range(len(chosen_word)):
#     display+="_"
#
# print(display)

wordlength = len(chosen_word)

end_of_game=False
lives = 6

while not end_of_game:
    guess = input("Guess a letter").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(wordlength):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f" You guessed {guess}, that's not in the word. You lose a life.")
        lives=lives-1
        if lives==0:
            end_of_game=True
            print("You Lose")

    print(f"{' '.join(display)}") #Join all the elements in the list and turn it into a String.

    if "_" not in display: #Check if user has got all letters.
        end_of_game=True
        print("You Win")

    print(stages[lives])








