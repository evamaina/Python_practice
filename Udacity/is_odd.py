def is_odd_number(num):
	if num % 2 != 0:
		return True
	else: # unnecesary else
		return False
print(is_odd_number(4))
print(is_odd_number(3))


def is_odd_number(num):
	if num % 2 != 0:
		return True  
	return False  # without else
print(is_odd_number(4))
print(is_odd_number(3))