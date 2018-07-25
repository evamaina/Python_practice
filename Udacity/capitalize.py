
# Slicing the first character (up to index 1) and capitalizing it
# Adding that to the rest of the string (from index 1 onward)

# funcion accepts string and returns the same string with the first letter capitalized

'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''
def capitalize(string):
    return string[:1].upper() + string[1:]