# the function accepts a list a nd returns a list of all truthy values without any falsy value

'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''
def compact(l):
    return [val for val in l if val]



# Without a list comprehension

def compact(l):
    truthy_vals = []
    for val in l:
        if val: truthy_vals.append(val)
    return truthy_vals