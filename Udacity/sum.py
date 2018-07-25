def sum_of_odd_numbers(numbers):
	total = 0
	for num in numbers:
		if num % 2 != 0:
			total += num
		return total # return inside a for loop reurns 1 coz it loops only once

print(sum_of_odd_numbers([1,2,3,4,5,6]))






def sum_of_odd_numbers(numbers):
	total = 0
	for num in numbers:
		if num % 2 != 0:
			total += num
	return total # return outside the for loop returns 9 coz it loops till the end.only returns after the loop finishes running

print(sum_of_odd_numbers([1,2,3,4,5,6]))