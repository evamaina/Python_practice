def sum_all_nums(num1,num2,num3, num4):
	return num1 + num2 + num3 + num4

print(sum_all_nums(3, 4, 5,6))  #18
print(sum_all_nums(3, 4)) # missing two required positional arguments




def sum_all_nums(*args):
	print(args) # args is a tuple containibg al of the elements that we pass it

print(sum_all_nums(3, 4, 5,6))  # (3,4,5,6) returns a tuple
print(sum_all_nums(3, 4)) # None (3,4)





def sum_all_nums(*args):
	total = 0
	for num in args:
		total += num
	return total
print(sum_all_nums(3, 4, 5,6))  # 18
print(sum_all_nums(3, 4)) # 7