

#given the person list below,create a dictionary called answer that makes
# each and every item in each list a key and the second item a corresponding value


# using dictionery comprehension
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {thing[0]: thing[1] for thing in person}

# dictionery comprehension without using index
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {k:v for k,v in person}

#  If you have a list of pairs, you can very easily turn it into a dictionary using dict() 
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = dict(person)



answer = {}.fromkeys(['a','e','i','o','u'], 0)

#Using a dictionary comprehension:
answer = {char:0 for char in 'aeiou'} 

# using dict.fromkeys
answer = dict.fromkeys("aeiou", 0) 




#Use chr() on the numbers between 65 and 91:

answer = {count: chr(count) for count in range(65,91)} 



