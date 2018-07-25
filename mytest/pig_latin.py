
def pig_latin(string):
	var = 'ay'
	vowel = 'way'
	string = string.lower()

	if len(string) > 0 and string.isalpha() and string !=' ':
		firstL = string[0]
		if firstL == 'a' or firstL == 'e' or firstL == 'i' or firstL == 'o' or firstL == 'u':
			new_word = string + vowel
			return new_word
			
		else:
			new_word = string
			while len(new_word):
				# if new_word[0] in ['a', 'e', 'i', '0', 'u']
				if(new_word[0] == 'a' or new_word[0] == 'e' or new_word[0] == 'i' or new_word[0] == 'o' or new_word[0] == 'u'):
					break
				new_word = new_word[1:] + new_word[0] 

			new_word = new_word + var
			return new_word
	else:
		return 'invalid data'


def user_input():
  word = str(input("Enter a word/phrase : "))
  print(pig_latin(word))

user_input()