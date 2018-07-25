 d = dict(a=1,b=2,c=3)
    d.clear()
    d # {}





    d = dict(a=1,b=2,c=3)
    c = d.copy()
    c # {'a':1,'b':2,'c':3}
    c==d # True
    c is d # False not referencing to exact same place in memory



# creates key-value pairs from comma separated values
    {}.fromkeys("a","b") # 'a': 'b'


    new-user ={}.fromkeys([])
    new-user = {}.fromkeys(['name','score','email','profile'],'unknown')
# new-user = {'name':'unknown','score':'unknown','email':'unknown','profile':'unknown'}



 k = dict(a=1,b=2,c=3)
 k['a']  # 1
 k.get('a') # 1
 k['b'] # 2
 k.get('b') #  2
 k['no-key'] # key error
 k.get('no-key') # None