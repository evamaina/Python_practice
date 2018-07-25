from random import randint
print("Rock...")
print("Paper...")
print("Scissors...")

player = input("player, Make your move: ").lower()
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
	else:
		print("computer wins!")

elif player == "paper":
	if computer == "rock":
		print("player wins!")
	else:
		print("computer wins!")

elif player == "scissors":
	if computer == "rock":
		print("computer wins!")
	else:
		print("player wins!")


else:
	print("please enter a valid move")