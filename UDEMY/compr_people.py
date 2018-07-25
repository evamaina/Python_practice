def who_do_you_know():
	people_they_know = input("Enter the people you know,separated by commas: ")
	lst = people_they_know.split(",")

	people_without_spaces = []
	[people_without_spaces.append(person.strip()) for person in lst]
	# for person in lst:
	# 	people_without_spaces.append(person.strip()) #removes spaces between commas in user input
	# return people_without_spaces

def ask_user():
	name =  input("What is your name?")
	if name in who_do_you_know():
		print("you know {}".format(name))
ask_user()






def who_do_you_know():
	people_they_know = input("Enter the people you know,separated by commas: ")
	lst = people_they_know.split(",")

	people_without_spaces = [person.strip() for person in lst]

	return people_without_spaces

def ask_user():
	name =  input("What is your name?")
	if name in who_do_you_know():
		print("you know {}".format(name))
ask_user()