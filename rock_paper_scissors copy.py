class Player():
    def __init__(self,name, input):
        self.name = name
        self.input = input
        
player1_name = input("Player 1 - Please provide your name ")
player1_input = input("Player 1 - Please select one option among the 3 following :\n-Rock\n-Paper\n-Scissors  \n ")
player2_name = input("Player 2 - Please provide your name ")
player2_input = input("Player 2 - Please select one option among the 3 following :\n-Rock\n-Paper\n-Scissors  \n ")
player1 = Player(player1_name, player1_input)
player2 = Player(player2_name, player2_input)

while player1.input == player2.input:
    player1.input = input(f"***DRAW*** \n {player1.name} - Please select one option among the 3 following :\n-Rock\n-Paper\n-Scissors  \n ")
    player2.input = input(f"***DRAW*** \n {player2.name} - Please select one option among the 3 following :\n-Rock\n-Paper\n-Scissors  \n ")
    print(player1.input, player2.input)

if player1.input == "Rock" and player2.input == "Scissors":
    print(f"{player1.name} Won")
elif player1.input == "Scissors" and player2.input == "Paper":
    print(f"{player1.name} Won")
elif player1.input == "Paper" and player2.input == "Rock":
    print(f"{player1.name} Won")
elif player2.input == "Rock" and player1.input == "Scissors":
    print(f"{player2.name} Won")
elif player2.input == "Scissors" and player1.input == "Paper":
    print(f"{player2.name} Won")
elif player2.input == "Paper" and player1.input == "Rock":
    print(f"{player2.name} Won")
else:
    print("Wrong combination or incorrect input")
