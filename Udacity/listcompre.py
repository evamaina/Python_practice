numbers = [1, 2, 3, 4, 5, 6]
even = [num for num in numbers if num % 2 == 2]
odd = [num for num in numbers if num % 2 != 2]
[num * 2 for num in numbers if num % 2 == 0 else num / 2 for num in numbers]



with_vowels = "This is so much fun!"
''.join(char for char in with_vowels if char not in "aeiou")

answer = [letter[0] for letter in ["Elie","Tim","Matt"]]
answer2 = [num for num in [1,2,3,4,5,6] if num % 2 == 0]


answer = []
for person in ["Elie", "Tim", "Matt"]:
    answer.append(person[0])

answer2 = []
for num in [1,2,3,4,5,6]:
    if num % 2 == 0:
        answer2.append(num)

answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
#the slice [::-1] is a quick way to reverse a string
answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]


answer = []
for x in [1,2,3,4]:
    if x in [3,4,5,6]:
        answer.append(x)
answer2 = []
for name in ["Elie", "Tim", "Matt"]:
    answer2.append(name[::-1].lower())

    answer = [[num for num in range(0,10)] for val in range(0,10)]