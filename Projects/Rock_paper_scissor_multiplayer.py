import random

p1 = input("Enter your Name :")
p2 = input("Enter second players name :")

print()
print("Welcome to the game")
print("Lets begin the Game !")
print()

p1_wins = 0
p2_wins = 0
ties = 0

while True:

    print()

    print(p1.capitalize(), ", game starts with your choice!")

    p1_input = input("Please choose any one from rock, paper, scissor :").lower()

    rps_list = ['rock', 'paper', 'scissor']
    if p1_input not in rps_list:
        print("Enter valid value!")
        break
    print()
    print(p2.capitalize(), ", its your turn now!")

    p2_input = input("Please choose any one from rock, paper, scissor :").lower()

    if p2_input not in rps_list:
        print("Enter valid value!")
        break
    print()
    

    if p1_input == p2_input:
        print("It's a tie")
        ties += 1

    elif p1_input == 'rock' and p2_input == 'scissor':
        print(p1.capitalize(), "wins!")
        p1_wins += 1
        
    elif p1_input == 'paper' and p2_input == 'rock':
        print(p1.capitalize(), "wins!")
        p1_wins += 1
        
    elif p1_input == 'scissor' and p2_input == 'paper':
        print(p1.capitalize(), "wins!")
        p1_wins += 1
        
    else:
        print(p2, "wins")
        p2_wins += 1
    comp = input("Press n to exit the game or press enter to continue :")
    
    if comp == 'n':
        break
    
print()

if p2_wins > 1 or p2_wins == 0:
    print(p2.capitalize(), "won", p2_wins, "games")
    
else:
    print(p2.capitalize(), "won", p2_wins, "game")

if p1_wins > 1 or p1_wins == 0:
    print(p1.capitalize(), "won", p1_wins, "games")
    
else:
    print(p1.capitalize(), "won", p1_wins, "game")


print("Number of ties :", ties)
print()
print("Thanks for playing my game !")
print("See you next time 😀")
