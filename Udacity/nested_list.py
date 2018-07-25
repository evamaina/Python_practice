nested_list = [[1,2,3], [4,5,6], [7,8,9]]
nested_list [0][1]  # 2
nested_list [1][-1] # 6
nested_list [-1][-2] # 8
nested_list [2] [1] # 5
nested_list [-1]  #[7,8,9]

for i in nested_list:
	for val in i:
		print(val) # 1,2,3,4,5,6,7,8,9