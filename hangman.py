import random
import string


WORDLIST_FILENAME = "words.txt"


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
    guessed = []
    for char in secret_word:   
        if char in letters_guessed: 
            guessed.append(char)
    return len(guessed) == len(secret_word)


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''

    guessed = ''
    for char in secret_word:   
        if char in letters_guessed: 
            guessed += char
        else: 
            guessed += " _ "
    return guessed


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    lst = [char for char in string.ascii_lowercase if char not in letters_guessed]  
    return "".join([str(char) for char in lst])


def match_with_gaps(word1, word2): 
    word1_stripped = word1.replace(" ", "")
    length_of_word = len(word1)
    if len(word2)==length_of_word: 
        
        list_word1 = list(word1)
        list_word2 = list(word2)
        for i in range(0, (len(word2))):    
            if word1[i] == "_" : 
                list_word1[i] = list_word2[i]          
    word1_new = "".join(list_word1)    
    return(word1_new == word2)
    
def show_possible_matches(word1): 
    possible_matches = []
    for word in wordlist: 
        if match_with_gaps(word1, word): 
            possible_matches.append(word)
    if len(possible_matches)==0: 
        print("No matches found")
    else: 
        print("Possible matches are:" possible_matches)
 
