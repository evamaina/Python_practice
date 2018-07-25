n= [1, 2 ,3, 4]

doubles = list(map(lambda x: x * 2 ,n))   # [2,4,6,8]




names = [
{'first': 'Rusty', 'last': 'steele'},
{'first': 'Colt', 'last': 'steele'},
{'first': 'Blue', 'last': 'steele'}
]

first_names = list(map(lambda x:x['first'], names))

# first_names  ['Rusty', 'Colt', 'Blue']



# returns a copy of the list decreased by one
def decrement_list(l):
    return list(map(lambda n: n-1, l))