print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("player1, Make your move: ")
print("***NO CHEATING\n\n" * 20)
player2 = input("player2, Make your move: ")

if player1 == player2:
	print("It's a tie!")
elif player1 == "rock":
	if player2 == "scissors":
		print("player1 wins!")
	elif player2 == "paper":
		print("player2 wins!")

elif player1 == "paper":
	if player2 == "rock":
		print("player1 wins!")
	elif player2 == "scissors":
		print("player2 wins!")

elif player1 == "scissors":
	if player2 == "rock":
		print("player2 wins!")
	elif player2 == "paper":
		print("player1 wins!")


else:
	print("something went wrong")