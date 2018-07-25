def ensure_correct_info(*args):
	if "colt" in args and "steel" in args:
		return "welcome back colt"
	return "Not sure who you are"

print(ensure_correct_info()) # welcome back colt
print(ensure_correct_info(1,"colt",True,"steel")) # Not sure who you are