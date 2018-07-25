numbers = dict(first= 1, second= 2, third = 3)
squared_numbers = {key: value ** 2 for key, value in numbers.items()}
print(squared_numbers)


{num: num **2 for num in [1,2,3,4,5]}
# 1:1,2:4,3:9,4:16,5:25

str1 = "ABC"
str2 = "123"
combo = {str1[i] : str2[i] for i in range(0,len(str1))}
print(combo)


num_list = [1,2,3,4]
{num: ("even" if num % 2 == 0 else "odd") for num in num_list}
# 1:'odd', 2:'even',3 :'odd', 4:'even'


list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[i] : list2[i] for i in range(0,len(list1))}

# advanced solution zip()
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
 
dict(zip(list1,list2)) 