def exponent(num, power):
	return num ** power

print(exponent(2,3)) # 8
print(exponent(3,2)) # 9
print(exponent(2)) # type error : missing one positional argument


def exponent(num, power = 2): # default value for power
	return num ** power

print(exponent(2,3)) # 8
print(exponent(3)) # 9
print(exponent(2)) # 4