def outer():
	count = 0
	def inner():
		nonlocal count # helps access the count in outer method.means the count method is not defined in inner or globally but defined in a parent some other functions are nested in
		count += 1
		return count
	return inner()
