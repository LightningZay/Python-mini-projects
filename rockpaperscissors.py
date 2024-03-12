import random

moves = {1 : "Rock", 
           2 : "Paper", 
           3 : "Scissors"}

move = 0

if __name__ == "__main__":
    print("Welcome to the Rock Paper Scissors Game!")
    
    while move < 1 or move > 3:
        move = int(input("Please input a valid choice: "
                        + "\n1 -> Rock "
                        + "\n2 - > Paper "
                        + "\n3 - > Scissors "
                        + "\n"))
        
    computerMove = random.choice(range(1,3))
    # print(computerMove)
    print()
    print("{} <--- VS ---> {}".format(moves[move], moves[computerMove]))
    print()
    if moves[move] == "Rock" and moves[computerMove] == "Paper":
        print("Computer wins with {}".format(moves[computerMove]))
    elif moves[move] == "Rock" and moves[computerMove] == "Scissors":
        print("Player wins with {}".format(moves[move]))
        
    elif moves[move] == "Paper" and moves[computerMove] == "Scissors":
        print("Computer wins with {}".format(moves[computerMove]))
    elif moves[move] == "Paper" and moves[computerMove] == "Rock":
        print("Player wins with {}".format(moves[move]))
        
    elif moves[move] == "Scissors" and moves[computerMove] == "Rock":
        print("Computer wins with {}".format(moves[computerMove]))
    elif moves[move] == "Scissors" and moves[computerMove] == "Paper":
        print("Player wins with {}".format(moves[move]))
    
    else:
        print("It's a tie!")
        
    exit()