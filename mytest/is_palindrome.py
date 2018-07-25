def is_palindrome(string):
  if string.strip() == "" or string.isdigit():
    return "invalid input"
  else:
    word = ''.join(string.split())
    if word[::-1] == word:
      return True
    else:
      return False

def history_record(params):
  if(len(params)>5):
    return params[-5:]
  return params

def user_input():
  store = []
  word = ""
  while word != 'q' or word != 'quit':
    word = str(input("Enter a word/phrase and q to quit: "))

    #If user input is q/quit ...history is returned
    if word == 'q' or word == 'quit':
      return history_record(store)

    #Gettting the value from is_palindrome function and validate if it is true, false or invalid
    #for invalid data its not stored. store both true and false value
    is_palindrome_val=is_palindrome(word)
    if is_palindrome_val=='invalid input':
      print('invalid input')
    else:
      store.append(word)
      print(is_palindrome(word))  
      
    


print(user_input())