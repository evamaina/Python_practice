import random
random_number = random.randint(1,10)
guess = None

while guess != random_number:
	guess = input("pick a number from 1 to 10: ")
	guess = int(guess)
	
	if guess < random_number:
		print("Your guess is too low")
	elif guess > random_number:
		print("Your guess is too high")
	else:
		print("You got it")