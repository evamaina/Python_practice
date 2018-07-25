{x ** 2 for x in range(10)}
#{1,4,9,16,25,36,49,64,81,0} we get a set

{x:x ** 2 for x in range(10)}
#{0:0,1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81} we get a dictionery

{char.upper() for char in 'hello'}
# {'O','L','H','E'.'L'}

def all_vowels_in_string(string):
	return len({char for char in string if char in 'aeiuo'}) == 5