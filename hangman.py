import random
from collections import Counter

somewords = '''television car apartment guitar nintendo videogame boardgame table church music choir comic lemon onion garlic melon apple'''
somewords = somewords.split(' ')
word = random.choice(somewords)


if __name__ == "__main__":
    print("Welcome to the Hangman game!")
    for i in word:
        print('_', end = " ")
    print()
    
    flag = 0
    lettersGuessed = ''
    guess = ''
    
    chances = len(word) + 2
    
    try:
        while chances >= 0 and flag == 0:
            print()
            chances -= 1
            
            try:
                guess = str(input("Try and make a guess! "))
            except:
                print("Please enter a letter!")
                continue
                
            if not guess.isalpha():
                print("Please enter a LETTER!")
                continue
            
            elif len(guess) > 1:
                print("Please enter a SINGLE letter")
                continue
            
            elif guess in lettersGuessed:
                print("You already guessed that letter!")
                continue
                                
            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    lettersGuessed += guess
                    
            for ch in word:
                if ch in lettersGuessed and Counter(lettersGuessed) != Counter(word):
                    print(ch, end = ' ')
                
                elif Counter(lettersGuessed) == Counter(word):
                    print("Congrats! You win! The word was: {}".format(word))
                    flag = 1
                    break
                
                else:
                    print('_', end = ' ')
        
        if chances < 0 and Counter(lettersGuessed) != Counter(word):
            print()
            print("Sorry, you lost!")
            print("The word was {}".format(word))
        
    except KeyboardInterrupt:
        print()
        print("Bye! Better luck next time")
        exit()
    
    