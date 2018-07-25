d = dict(a=1,b=2,c=3)
d.pop() # Type error, expected at least one argument
d.pop('a') # 1
d # {'c': 3, 'b': 2}
d.pop(e) # key error


first = dict(a=1,b=2,c=3)
second = {}
second.update first
second # {'a':1,'b':2,'c':3}


# removes a random key in a dictionery
d = dict(a=1,b=2,c=3)
d.popitem() # ('d':4)
d.popitem('a') # Type error.pop item takes no argument.one given




inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!
# Make a copy of inventory and save it to a variable called stock_list
stock_list = inventory.copy()
# add the value 18 to stock_list under the key "cookie"
stock_list['cookie'] = 18
# remove 'cake' from stock_list
stock_list.pop('cake')