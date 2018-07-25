n= [1, 2 ,3, 4]

evens = list(filter(lambda x: x%2 == 0 ,n)) 

#evens = [2,4]


# removes all negatives
def remove_negatives(nums):
    return list(filter(lambda l: l >= 0, nums))




'''
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''
# filter out every number not divisible by 4 and return a new list where every number is tripled
def triple_and_filter(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))







'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
'''

# the function should return a new list with first and last name keys in each dictionery concatenated
def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))

   