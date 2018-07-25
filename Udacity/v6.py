from random import randint
computer_wins = 0
player_wins = 0
winning_score = 3
while player_wins < winning_score and computer_wins < winning_score:
	print(f"player score: {player_wins} computer score: {computer_wins}")
	print("Rock...")
	print("Paper...")
	print("Scissors...")

	player = input("player, Make your move: ").lower()
	if player == "quit" or player == "q":
		break
	rand_numb = randint(0,2)
	if rand_numb == 0:
		computer= "rock"
	elif rand_numb == 1:
		computer = "paper"
	else:
		computer ="scissors"
	print(f"computer plays {computer}")

	if player == computer:
		print("It's a tie!")
	elif player == "rock":
		if computer == "scissors":
			print("player wins!")
			player_wins += 1
		else:
			print("computer wins!")
			computer_wins +=1

	elif player == "paper":
		if computer == "rock":
			print("player wins!")
			player_wins += 1
		else:
			print("computer wins!")
			computer_wins +=1

	elif player == "scissors":
		if computer == "rock":
			print("computer wins!")
			computer_wins += 1
		else:
			print("player wins!")
			player_wins += 1


	else:
		print("please enter a valid move")

if player_wins > computer_wins:
	print("CONGRATS, YOU WIN!")
elif player_wins == computer_wins:
	print("OOPS! IT'S TIE")
else:
	print("OH NO!, COMPUTER WON..")


		# in this case it plays continously as long as the win is less than two times