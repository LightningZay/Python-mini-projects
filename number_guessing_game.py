import random
import math



if __name__ == "__main__":
    print("\nWelcome to the number guessing game")
    
    lower = int(input("Enter a lower bound:- "))
    upper = int(input("Enter a upper bound:- "))
    
    randNum = random.randint(lower, upper)
    maxGuesses = math.ceil(math.log2(upper - lower + 1))
    numGuesses = 0
    
    print("You have " + str(maxGuesses) + " attempts!\n")
    
    while(numGuesses < maxGuesses):
        numGuesses += 1
        
        guess = int(input("Enter a guess "))
        
        if guess == randNum:
            print("Correct! You win.")
            print("You got it in %d attempts" % numGuesses)
            exit()
        elif guess < randNum:
            print("Guess Higher!")
        elif guess > randNum:
            print("Guess Lower!")
            
    if numGuesses >= maxGuesses:
        print("The number was " + str(randNum))
        print("You lose. Better luck next time.")    
    
    
# end main