# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "ps2/words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    
    # Store distinct letters in secret_word
    word_as_obj = {}
    uniqe_letter_count = 0
    for secret_letter in secret_word:
      if secret_letter not in word_as_obj:
        word_as_obj[secret_letter] = 1
        uniqe_letter_count += 1
				
    correct_letter_guessed = 0

    for letter in letters_guessed:
      if letter in word_as_obj and word_as_obj[letter] > 0:
        word_as_obj[letter] -= 1
        correct_letter_guessed += 1
        if correct_letter_guessed == uniqe_letter_count:
            return True
    return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    res = ["_ "] * len(secret_word)
    curr_word = secret_word
    for letter in letters_guessed:
      letter_index = curr_word.find(letter)
      while letter_index >= 0:
                    curr_word = curr_word.replace(letter, '*', 1)
                    res[letter_index] = letter
                    letter_index = curr_word.find(letter)
    return ''.join(res)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    all_alphabet_array = list(string.ascii_lowercase)
    for letter in letters_guessed:
        letter_index = ord(letter) - 97
        all_alphabet_array[letter_index] = ""
    return "".join(all_alphabet_array)

    
def is_input_valid(input: str, letters_guessed: list):
    '''
    input: a string of user input, must be an alphabet
    
    The input can be uppercase or lowercase
		'''
    lowercase_input = input.lower()
    if ord(lowercase_input) < 97 or ord(lowercase_input) > 123:
        return {
            "message": "Oops! That is not a valid letter.",
            "is_valid": False 
				}
    if lowercase_input in letters_guessed:
        return {
            "message": "You've already guessed that letter.",
            "is_valid": False 
				}
    return {
        "message": "",
        "is_valid": True
		}

def get_unique_letters_of_secret_word(secret_word: str):
    count = 0
    letters_dict = {}
    for letter in secret_word:
        if letter not in letters_dict:
            letters_dict[letter] = 1
            count += 1
    return count

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    available_guess = 6
    letters_guessed = []
    available_warnings = 3
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long")
    while not is_word_guessed(secret_word, letters_guessed) and available_guess > 0:
        print("-"*10)
        print(f"You have {available_guess} guesses left")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        letter = input("Please guess a letter: ")
        validated_input = is_input_valid(letter, letters_guessed)
        letters_guessed.append(letter)
        
        if not validated_input.get("is_valid"):
            available_warnings = available_warnings - 1
            if available_warnings < 0:
                print(f"{validated_input.get('message')} You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
                available_guess = available_guess - 1
            else:
                print(f"{validated_input.get('message')} You have {available_warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
        else:
            if letter in secret_word:
                print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
            else:
                print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
                available_guess = available_guess - 1
    if available_guess == 0:
        print("-"*10)
        print(f"Sorry, you ran out of guesses. The word was {secret_word}")
    else:
        print("-"*10)
        print("Congratulations, you won!")
        # use len on secret_word for now, need to change to unique letters of secret_word
        print(f"Your total score for this game is: {available_guess * get_unique_letters_of_secret_word(secret_word)}")
    return



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word: str, other_word: str):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word_without_space = my_word.replace(" ", "")
    if len(my_word_without_space) != len(other_word):
      return False
    # The letters that has not been guessed
    possible_guess_left = {}

    for i in range(len(other_word)):
      if my_word_without_space[i] != "_":
        if my_word_without_space[i] != other_word[i] or other_word[i] in possible_guess_left:
          return False
      else:
        possible_guess_left[other_word[i]] = True
    
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matches = []
    for word in wordlist:
      if (match_with_gaps(my_word, word)):
        matches.append(word)
    if len(matches) == 0:
      print("No matches found")
    matches_as_string = " ".join(matches)
    print(matches_as_string)



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
		secret_word = choose_word(wordlist)
		hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
