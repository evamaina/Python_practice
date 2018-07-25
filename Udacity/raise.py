def colorize(text, color):
	if type(text) is not str:
		raise TypeError("text must be insatnce of string")
	print(f"{text} in color {color}")



colorize("Hello","Red")
colorize(50,"Red")