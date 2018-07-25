class Parent():
	def __init__(self, eye_color, last_name):
		print("Parent constructor called")
		self.eye_color = eye_color
		self.last_name = last_name

	def show_info(self):
		print("Last Name - "+ self.last_name)
		print("Eye Color - "+ self.eye_color)

class Child(Parent):
	"""docstring for Child"""
	def __init__(self,eye_color,last_name, number_of_toys):
		print("Child constructor called")
		Parent.__init__(self,last_name,eye_color)
		self.number_of_toys = number_of_toys

# Billy_Cyrus = Parent("Blue", "Cyrus")
# print(Billy_Cyrus.last_name)

miley_cyrus = Child("Blue","Cyrus",5)   
print(miley_cyrus.last_name)
print(miley_cyrus.number_of_toys)

# Child constructor called
# Parent constructor called
# Blue
# 5

Billy_Cyrus = Parent("Cyrus", "Blue")
Billy_Cyrus.show_info()

# Parent constructor called
# Last Name - Blue
# Eye Color - Cyrus

miley_cyrus = Child("Blue","Cyrus",5)
miley_cyrus.show_info()

# Child constructor called
# Parent constructor called
# Last Name - Blue
# Eye Color - Cyrus