import random

def get_choices():
    player_choice = input("enter a choice(rock, paper, scissors): ")
    opitions = ["rock" , "paper" , "scissors"]
    computer_choice = random.choice(opitions)
    choices = { "player" : player_choice , "computer" : computer_choice }
    return choices

def check_win(player, computer):
    print(f"you chose {player} , computer chose {computer} ")
    if player == computer:
        return "it's a tie"
    
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
        
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose."

    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."
        

choice = get_choices()
result = check_win(choice["player"],choice["computer"])
print(result)


