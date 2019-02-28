# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
#
# Remember the rules:
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock


while input("Play? Y/N : ") == "Y":
    player1 = input("Chose Rock/Paper/Scissor : ")
    player2 = input("Chose Rock/Paper/Scissor : ")

    if player1 not in ["Rock", "Paper", "Scissor"] or player1 not  in ["Rock", "Paper", "Scissor"] :
        print("Invalid input")
    elif player1 == player2:
        print("It's a draw")
    elif player1 == "Rock":
        if player2 == "Paper":
            print("Player 2 Wins")
        else:
            print("Player 1 Wins")
    elif player1 == "Paper":
        if player2 == "Scissor":
            print("Player 2 Wins")
        else:
            print("Player 1 Wins")
    else:
        if player2 == "Rock":
            print("Player 2 Wins")
        else:
            print("Player 1 Wins")


