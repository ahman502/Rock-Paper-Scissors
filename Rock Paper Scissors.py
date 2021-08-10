from random import randint

print ("This is a rock, paper, scissors game. \n\nPlease only type in lower case when entering your play.\n")

List = ["rock", "paper", "scissors"]

u1 = input("How many players (1/2): ")

def player1():

    robot_input = List[randint(0,2)]
    print ("Robot chose:", robot_input)
    user_input = input("\nrock, paper, or scissors: ")
 
    if user_input == "rock" and  robot_input == "rock":
         print ("This was a draw, you both chose rock.")
    
    elif user_input == "paper" and  robot_input == "paper":
         print ("This was a draw, you both chose paper.")

    elif user_input == "scissors" and  robot_input == "scissors":
         print ("This was a draw, you both chose scissors.")

    elif user_input == "rock" and  robot_input == "scissors":
         print ("You win!")

    elif user_input == "paper" and  robot_input == "rock":
         print ("You win!")
    
    elif user_input == "scissors" and  robot_input == "paper":
         print ("You win!")

    elif robot_input == "rock" and  user_input == "scissors":
         print ("Robot wins")

    elif robot_input == "paper" and  user_input == "rock":
         print ("Robot wins")
    
    elif robot_input == "scissors" and  user_input == "paper":
         print ("Robot wins")

    else: 
        print ("\nValue not inended. Try again.")
    
def player2():

    user_input = input("\nrock, paper, or scissors: ")
    user_input2 = input("\nrock, paper, or scissors: ")

 
    if user_input == "rock" and  user_input2 == "rock":
         print ("This was a draw, you both chose rock.")
    
    elif user_input == "paper" and  user_input2 == "paper":
         print ("This was a draw, you both chose paper.")

    elif user_input == "scissors" and  user_input2 == "scissors":
         print ("This was a draw, you both chose scissors.")

    elif user_input == "rock" and  user_input2 == "scissors":
         print ("You win!")

    elif user_input == "paper" and  user_input2 == "rock":
         print ("You win!")
    
    elif user_input == "scissors" and  user_input2 == "paper":
         print ("You win!")

    elif user_input2 == "rock" and  user_input == "scissors":
         print ("User 2 wins")

    elif user_input2 == "paper" and  user_input == "rock":
         print ("User 2 wins")
    
    elif user_input2 == "scissors" and  user_input == "paper":
         print ("User 2 wins")

    else: 
        print ("Value not inended. Try again.")

while True:
    if u1 == "1":
        player1()
        
    elif u1 == "2":
        player2()
        
    else:
        print ("\nPlease enter a value that is either 1 or 2")
        
    end = input("\nDo you want to continue playing (y/n): ")
    
    if end == "n":
        break
    
    elif end == "y":
        u1 = input("\nHow many players (1/2): ")
        
    else:
        print ("\nPlease input (y) or (n)")
        u1 = input("\nHow many players (1/2): ")
