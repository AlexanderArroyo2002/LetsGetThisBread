import random
from words import words
import string


def word_choice(words):
    word = 'planetxolo'  # chooses word used in the hangman
    while '_' in word or ' ' in word:
        word = random.choice(words)  # makes sure that the word choices is just letter
    return word.upper()  # use everything in uppercase to eliminate differences due to case


def hangman():
    word = word_choice(words)  # runs the wordChoice function and gets the word
    word_letters = set(word)  # separates the letters in the word so when guess we know how many are left
    alphabet = set(string.ascii_uppercase)  # Letters to choose from
    used_letters = set()  # This holds the letters that the user has used already

    # Needs a way to ask the user what letter they want to guess, but also add to the new used letters and remove a
    # letter from teh word letters function so we can keep track of how many letter are left in the word

    while len(word_letters) > 0:
        # Need a way to display the letters that have already been guessed Ex: Guessed: A B C D E
        print("These are the letters that have been used already:", ' '.join(used_letters))

        # Needs a way to show current outlook of the word to the user. Ex: _ _ _ A _
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('This is what the current state of your word(s) looks like:', ' '.join(word_list))
        guess = input('Guess a letter: ').upper()
        print("")
        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
        elif guess in used_letters:
            print('Already used that letter silly. Try again')
        else:
            print('That is a invalid answer. Try again')
    print('Congrats, you got it! The word(s) was:', word)


hangman()
