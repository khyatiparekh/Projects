#hangman
import pandas as pd
import random
def hangman():
    words = ['hello','cat','dog','tree']
    word = random.choice(words)

    wrong = 13
    letters = list(word)
    string = "-" * len(word)

    tried= []
    while(wrong!=0):
        letter = raw_input('Enter a letter ')
        if(letter in tried):
            print('you already tried this letter')
        else:
            if(letter in letters):
                string = list(string)
                indices = [i for i,l in enumerate(word) if l == letter]
                for i in range(0,len(indices)):
                    string[indices[i]] = word[indices[i]]
                    
                print(''.join(string))
            else:
                print('Oops wrong letter, try again! You have ',(wrong -1), 'chances left')
        
        wrong = wrong - 1
        tried.append(letter)
        string = ''.join(string)
        if(string == word):
            return 'you got it!'

    return 'better luck next time'


    if __name__ == "__main__"():
        hangman()