from random import random
def flip_coin():
	#generate a random number
	r = random()
	if r > 0.5:
		return "Heads"
	else:
		return "Tails"

# overrides
def flip_coin():
	#generate a random number
	
	if random() > 0.5:
		return "HEADS"
	else:
		return "TAILS"
print(flip_coin())