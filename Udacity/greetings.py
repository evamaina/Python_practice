def special_greetings(**kwargs):
	if "David" in kwargs and kwargs["David"] == "special":
		return "you get a special greeting David"
	elif "David" in kwargs:
		return f"{kwargs['David']} David"
	return "Not sure who this is"

print(special_greetings(David = "Hello")) #Hello David
print(special_greetings(Bob = "Hello")) #Not sure who this is
print(special_greetings(David = "special")) #you get a special greeting David