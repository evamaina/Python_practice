def fav_colors(**kwargs):
	print(kwargs) # {'colt': 'red', 'ruby': 'red', 'ethel': 'teal'} prints a dictionary


fav_colors(colt = "red", ruby= "red",ethel= "teal")




def fav_colors(**kwargs):
	for person , color in kwargs.items():
		print(f"{person}'s favourite color is {color}")

fav_colors(colt = "purple", ruby= "red",ethel= "teal")
#colt's favourite color is purple
#ruby's favourite color is red
#ethel's favourite color is teal