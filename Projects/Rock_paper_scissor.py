import random

name = input("Enter your Name :")

print()
print("Welcome to the game", name.capitalize())
print("Lets begin the Game")
print()

user_wins = 0
computer_wins = 0
ties = 0

while True:
    
    user = input("Choose any one from rock, paper, scissor, or press q if you wanna quit :").lower()
    if user == 'q':
        break
    computer = random.choice(['rock', 'paper', 'scissor'])
    
    print()
    
    print("Computer Chooses :", computer)
    
    print()
    if user == 'q':
        break
    
    if user == computer:
        print("It's a tie")
        ties+=1
        
    elif user == 'rock' and computer == 'scissor':
        print(name.capitalize(), "wins!")
        user_wins+=1
        
    elif user == 'paper' and computer == 'rock':
        print(name.capitalize(), "wins!")
        user_wins+=1

    elif user == 'scissor' and computer == 'paper':
        print(name.capitalize(), "wins!")
        user_wins+=1
       
    else:
        print("Computer won!")
        computer_wins+=1

print()
if computer_wins>1 or computer_wins==0:
    print("Computer won", computer_wins, "games")
else:
    print("Computer won", computer_wins, "game")

if user_wins>1 or user_wins==0:
    print(name.capitalize(),"won", user_wins, "games")
else:
    print(name.capitalize(),"won", user_wins, "game")


print("Number of ties :", ties)
print()
print("Thanks for playing my game !")
print("See you next time 😀")