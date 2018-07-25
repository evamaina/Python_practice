def single_letter_count(string,letter):
    return string.lower().count(letter.lower())


'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''
def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}



# returns the number ot times the search term appears in  collection
def frequency(collection, searchTerm):
    return collection.count(searchTerm)