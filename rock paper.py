import random
user_score = 0
computer_score = 0
options = ['rock', 'paper', 'scissors']
while user_score < 2 and computer_score < 2:
    user = input("rock, paper or scissors: ").lower()
    if user not in options:
        print("invalid")
        continue
    computer = random.choice(options)
    print("computer chose", computer)
    if user == computer:
        print("tie")
    elif (user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper'):
        print("you win this round")
        user_score += 1
    else:
        print("computer wins this round")
        computer_score += 1
    print("score:", user_score, "-", computer_score)
if user_score == 2:
    print("you won the game")
else:
    print("computer won the game")
