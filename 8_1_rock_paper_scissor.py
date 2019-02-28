combinationsList = [["Rock", "Rock"], ["Rock", "Paper"], ["Rock", "Scissor"]
                    , ["Paper", "Rock"], ["Paper", "Paper"], ["Paper", "Scissor"]
                    , ["Scissor", "Rock"], ["Scissor", "Paper"], ["Scissor", "Scissor"]]

resultList = ["It's a draw", "Player 2 Wins", "Player 1 Wins"
              , "Player 1 Wins", "It's a draw", "Player 2 Wins"
              , "Player 2 Wins", "Player 1 Wins", "It's a draw"]

matchResult = []

while input("Play? Y/N : ") == "Y":
    for x in range(1, 3):
        matchResult.append(input("Player " + str(x) + ", Select Rock/Paper/Scissor : "))
    if matchResult in combinationsList:
        print(resultList[combinationsList.index(matchResult)])
    else:
        print("Invalid Values")
    matchResult = []
