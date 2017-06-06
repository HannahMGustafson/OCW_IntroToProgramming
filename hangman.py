# Problem Set 2, hangman.py
# Name: Hannah Gustafson
# Collaborators: Google
# Time spent: 3 Hours



WORDLIST_FILENAME = "words.txt"

def is_word_guessed(secret_word, letters_guessed):
    for x in secret_word:
        if x not in letters_guessed:
            return False
    return True

def get_available_letters(letters_guessed):
    import string
    left = string.ascii_lowercase
    for let in letters_guessed:
        left = left.replace(let,"")
    return left

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

def unique_letters(secret_word):
    uniq_str = []
    for char in secret_word:
        if char not in uniq_str:
            uniq_str.append(char)
    return len(uniq_str)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def get_guessed_word(secret_word, letters_guessed):
    ret = ''
    for let in secret_word:
        if let in letters_guessed:
            ret += let
        else:
            ret += '_ '
    return ret

# def hangman(secret_word):
#     print secret_word
#     print unique_letters(secret_word)
#     n = 6
#     len_sw = len(secret_word)
#     print 'Welcome to the game of hangman'
#     print 'The secret word contains ' + str(len_sw) + ' letters'
#     print '--------------'
#     letters_guessed = []
#     found_it = False
#     w = 3
#     while found_it is False:
#         print 'You have ' + str(n) + ' guesses remaining'
#         print 'Letters remaining: ' + get_available_letters(letters_guessed)
#         let = raw_input('What letter are you guessing? ')
#         let = str.lower(let)
#         if len(let) != 1 or not str.isalpha(let):
#             print 'Not a valid input'
#             print '--------------'
#             w -= 1
#             if w == 0:
#                 n -= 1
#                 w = 3
#                 print 'You lose a guess'
#             else:
#                 print 'You have ' + str(w) + ' warnings remaining before losing a guess'
#         else:
#             if let in letters_guessed:
#                 w -= 1
#                 print 'Silly goose, you guessed that already'
#                 if w == 0:
#                     n -= 1
#                     w = 3
#                     print 'You lose a guess'
#                     print '--------------'
#                 else:
#                     print 'You have ' + str(w) + ' warnings remaining before losing a guess'
#                     print '--------------'
#             else:
#                 letters_guessed.append(let)
#                 if let in  secret_word:
#                     print 'Good Guess! ' + get_guessed_word(secret_word, letters_guessed)
#                 else:
#                     print 'Horrible Guess... ' + get_guessed_word(secret_word, letters_guessed)
#                 print '--------------'
#                 if let not in secret_word and let in ['a', 'e', 'i', 'o', 'u']:
#                     n -= 2
#                 elif let not in secret_word:
#                     n -= 1
#                 if n == 0:
#                     print "You ran out of guesses"
#                     print "The word was " + secret_word
#                     break
#                 if is_word_guessed(secret_word, letters_guessed):
#                     print "You found it"
#                     print "Your score is " + str(unique_letters(secret_word)*n)
#                     break


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    temp = my_word.replace(' ', '')
    if len(temp) == len(other_word):
        n = 0
        for char in temp:
            if (char == '_' and other_word[n] not in temp) or char == other_word[n]:
                n += 1
            else:
                return False
                break
        return True
    else:
        return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possibles = []
    for word_hint in wordlist:
        if match_with_gaps(my_word, word_hint):
            possibles.append(word_hint)
    if len(possibles) != 0 :
        print possibles
    else:
        print 'No matches found'



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
    print secret_word
    print unique_letters(secret_word)
    n = 6
    len_sw = len(secret_word)
    print 'Welcome to the game of hangman'
    print 'The secret word contains ' + str(len_sw) + ' letters'
    print '--------------'
    letters_guessed = []
    found_it = False
    w = 3
    while found_it is False:
        print 'You have ' + str(n) + ' guesses remaining'
        print 'Letters remaining: ' + get_available_letters(letters_guessed)
        let = raw_input('What letter are you guessing? ')
        let = str.lower(let)
        if let == '*':
            word_with_gaps = get_guessed_word(secret_word, letters_guessed)
            show_possible_matches(word_with_gaps)
            n -= 1
        elif len(let) != 1 or not str.isalpha(let):
            print 'Not a valid input'
            print '--------------'
            w -= 1
            if w == 0:
                n -= 1
                w = 3
                print 'You lose a guess'
            else:
                print 'You have ' + str(w) + ' warnings remaining before losing a guess'
        else:
            if let in letters_guessed:
                w -= 1
                print 'Silly goose, you guessed that already'
                if w == 0:
                    n -= 1
                    w = 3
                    print 'You lose a guess'
                    print '--------------'
                else:
                    print 'You have ' + str(w) + ' warnings remaining before losing a guess'
                    print '--------------'
            else:
                letters_guessed.append(let)
                if let in  secret_word:
                    print 'Good Guess! ' + get_guessed_word(secret_word, letters_guessed)
                else:
                    print 'Horrible Guess... ' + get_guessed_word(secret_word, letters_guessed)
                print '--------------'
                if let not in secret_word and let in ['a', 'e', 'i', 'o', 'u']:
                    n -= 2
                elif let not in secret_word:
                    n -= 1
                if n == 0:
                    print "You ran out of guesses"
                    print "The word was " + secret_word
                    break
                if is_word_guessed(secret_word, letters_guessed):
                    print "You found it"
                    print "Your score is " + str(unique_letters(secret_word)*n)
                    break



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
