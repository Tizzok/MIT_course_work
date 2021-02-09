# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# 
# 
# Name          : Matt Clarkson
# Collaborators : <your collaborators>
# Time spent    : Too Long

import math
import random
import string
import re

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*':0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    
    word_sum = 0
    word = word.lower()
    word_length = int(len(word))
    for i in word:
        word_sum = word_sum + SCRABBLE_LETTER_VALUES[i]        
        
    if (7*word_length - 3*(n-word_length)) > 1:
        return word_sum*(7*word_length- 3*(n-word_length))
    else:
        return 1*word_sum
    
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    
    # pass  # TO DO... Remove this line when you implement this function

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print() 
#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    hand['*'] = 1
    num_vowels = int(math.ceil(n / 3)) - 1

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    #     ## building dictionary out of guessed word
    # word = word.lower()
    # #make copy of original hand
    
    # new_hand = hand.copy()
    # # create a dictionary of the word guessed
    # word_dict = {}
    # for i in word:
    #     word_dict[i] = word_dict.get(i, 0) + 1
    #     print(word_dict)

    # # use the dictionary of the word to subtract from the dictionary of the hand
    # for i in word_dict:
    #     new_hand[i] = new_hand.get(i, 0) - word_dict[i]
    # # prevents dictionary from going under 0
    
    # delete = []
    # # for key, val in new_hand.items():
    # #     if val < 0:
    # #         val = 0
    # print(new_hand['*'])
    
    # for i in delete:
    #     del new_hand[i]
        
    # print(new_hand)
    # print(delete)


    new_hand = hand.copy()
    word = str.lower(word)
    
    for let in new_hand.keys():
        for i in range(len(word)):
            if let in word[i]:
                new_hand[let] = new_hand[let] - 1
    return new_hand


# hand= {'h': 1, 'e': 1, 'l': 2, 'o': 1}
# word = "HELLO"
# print(update_hand(hand,word))


    # pass  # TO DO... Remove this line when you implement this function

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    # word = word.lower()
    # word_real = word

    # # no_wild = False
    # # wildcard = False
    # wild_loc = -1
    
    # if word.find('*') >= 0:
    #     wild_loc = word.find('*')


    # for getting_it in word_list:
    #     if re.search(word, getting_it) and getting_it[wild_loc] in VOWELS:
    #         word_real = getting_it
    #         break
    # if word_real.find('*') >= 0:
    #     return False

    # # return word in word_list and all(hand.get(a, 0) >= b for a, b in get_frequency_dict(word).items())
    
    # return word_real in word_list and all(hand.get(a, 0) >= b for a, b in get_frequency_dict(word).items())





    # word_manip = word
    # word_manip = word_manip.lower()




    # # no_wild = False
    # # wildcard = False
    # wild_loc = -1
    # if word.find('*') >= 0:
    #    wild_loc = word.find('*')

    # for getting_it in word_list:
    #    if re.search(word_manip, getting_it) and getting_it[wild_loc] in VOWELS:
    #        word_manip = getting_it
    #        break

    # # if word_real.find('*') >= 0:
    # #     return False
    # # return word in word_list and all(hand.get(a, 0) >= b for a, b in get_frequency_dict(word).items())
    
    # return word_manip in word_list and all(hand.get(a, 0) >= b for a, b in get_frequency_dict(word.lower()).items())


    test = []
    test_list = []
    word = str.lower(word)
    word_copy = word
    if '*' not in word:
        for i in range(len(word)):
            if word[i] in hand and hand[word[i]] >= word.count(word[i]) and word in word_list:
                test.append(1)
            else:
                test.append(0)
        if sum(test) == len(word):
            return True
        else:
            return False
    elif '*' in word_copy:
        for i in range(len(VOWELS)):
            if word_copy.replace('*', VOWELS[i]) in word_list:
                test_list.append(1)
                for j in range(len(word_copy)):
                    if word_copy[j] in hand and hand[word_copy[j]] >= word_copy.count(word_copy[j]):
                        test.append(1)
                    else:
                        test.append(0)
                if sum(test) == len(word_copy):
                    return True
                else:
                    return False
            else:
                test_list.append(0)
        if sum(test_list) != len(VOWELS):
            return False





    pass  # TO DO... Remove this line when you implement this function

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    
    return sum(hand.values())
    
    pass  # TO DO... Remove this line when you implement this function

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """


    
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    total_score = 0
    while True:
        if calculate_handlen(hand) == 0:
            print()
            print('Ran out of letters. Total score for this hand:', total_score)
            break
        print()
        print('Current hand:', end=' '), display_hand(hand)
        user_input = str.lower(input('Please enter a word, or "!!" to indicate that you are finished: '))
        if user_input == '!!':
            print('Total score for this hand:', total_score)
            break
        else:
            if is_valid_word(user_input, hand, word_list):
                current_word_score = get_word_score(user_input, calculate_handlen(hand))
                total_score = current_word_score + total_score
                hand = update_hand(hand, user_input)
                print('"%s"' % user_input, 'earned', current_word_score, 'points. Total:', total_score, 'points')
            else:
                print('That is not a valid word. Please choose another word.')
                hand = update_hand(hand, user_input)
    return total_score


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    
    
    x = str(letter.lower())
    hand_copy = hand.copy()
    if x not in hand.keys():
        return hand
    all_letters = VOWELS+CONSONANTS

    while x in hand.keys():
        x = random.choice(all_letters)
    
    hand[x] = hand[letter]
    del hand[letter]
    return hand
    
    
    
    pass  # TO DO... Remove this line when you implement this function
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    n_hands = int(input('How many hands would you like to play? '))
    sub_count = 1
    replay_hand = 1
    total_score = 0

    while n_hands >= 1:
        new_score = 0
        
        # get hand and display it
        hand = deal_hand(HAND_SIZE)
        display_hand(hand)
        # as if they want to swap out a letter
        # Yes path for swapping out a letter
        if sub_count > 0:
            print(sub_count)
            sub_ans = (input('Do you want to swap out a letter? y or n ')).lower()
            if sub_ans == 'y':
            # add number to prevent swapping out a second time in a game. 
                sub_count -= 1 
                letter = (input('Mmmhmmm and which letter? It must be different ')).lower()
            # sub out the letter and present
                hand = substitute_hand(hand,letter)
        score = play_hand(hand,word_list)
        
        if replay_hand > 0:
            print('Replaying hand')
            replay_ans = (input('Do you want to retry that hand? Once per game. y or n ')).lower()
            if replay_ans == 'y':
                print('You said replaying hand')
                replay_hand = replay_hand - 1
                if sub_count > 0:
                    sub_ans = (input('Do you want to swap out a letter? Once per game y or n ')).lower()
                    if sub_ans == 'y':
                        letter = (input('Mmmhmmm and which letter? It must be different ')).lower()
                        sub_count = sub_count - 1
                        hand = substitute_hand((hand,letter))
                    # else:
                        # break # = choice for sub no                
                # else:
                    # break # No sub option
            
            # replay base
            new_score = play_hand(hand,word_list)
        print(score)
        print(new_score)
        total_score = total_score + max(score, new_score)
        n_hands -= 1
    print('And your final score is....')
    print(total_score)
        
  
        
        
        
    # print("play_game not implemented.") # TO DO... Remove this line when you implement this function
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)


# play_hand({'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1},word_list)
#play_game(word_list)