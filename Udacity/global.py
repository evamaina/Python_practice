total = 0
def increment():
	total += 1
	return total

increment() # Error. local variable total referenced before assignment




total = 0
def increment():
	global total
	total += 1
	return total

increment() # 1




name = "Rusty"
def greet():
	print(name)

greet() # Rusty .Accessing global variable without trying to change it works




name = "Rusty"
def greet():
	name += "Steele"
	print(name)

greet() # name is not defined in the local scope




name = "Rusty"
def greet():
	global name
	name += "Steele"
	print(name)

greet() # Rusty Steele


