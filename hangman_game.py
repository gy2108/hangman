import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    l1=list(secretWord)
    l2=lettersGuessed
    for i in l1:
      if i not in l2:
        return False
    return True
    

def getGuessedWord(secretWord, lettersGuessed):
    l3=list(secretWord)
    l4=lettersGuessed
    l5=[]
    for i in l3:
      if i in l4:
       l5.append(i)
      else:
       l5.append('_')
    return ' '.join(l5)

def getAvailableLetters(lettersGuessed):
    l=[]
    for i in range(97,123):
      if (chr(i) not in lettersGuessed):
        l.append(chr(i))
    return ''.join(l)
    
def check_if_won(secretWord, lettersGuessed):
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True

def hangman(secretWord):
    lettersGuessed=[]
    g=0
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is "+str(len(secretWord))+" letters long.")
    print("-------------")
    while((8-g)>0):
        
        print("You have "+str(8-g)+" guesses left.")
        print("Available letters: "+str(getAvailableLetters(lettersGuessed)))
        guess=str((input("Please guess a letter: ")))
    
        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed.append(guess)
            print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
            if check_if_won(secretWord, lettersGuessed):
                print("!!!!!!!!!!! CONGRATULATIONS YOU GUESSED IT RIGHT !!!!!!!!!!!!!!!!!!!!")
                break
        elif guess in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        elif guess not in secretWord:
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
            lettersGuessed.append(guess)
            g=g+1
        print('------------')
        if ((8-g)==0):
            print('Sorry, you ran out of guesses. The word was', secretWord)
            break
        else:
            continue

#It starts here
wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
