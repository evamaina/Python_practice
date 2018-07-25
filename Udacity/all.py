# checks if the type of each item in the list is a str.  
def is_all_strings(lst):
    return all(type(l) == str for l in lst)




# using list comprehension
def is_all_strings(lst):
    return all([type(l) == str for l in lst])