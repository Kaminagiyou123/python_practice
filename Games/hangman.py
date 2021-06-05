import random
import string
from words import words

def get_valid_word(words):
 word=random.choice(words)
 while '-' in word or " " in word:
  word=random.choice(words)
 return word;

def hangman():
 word= get_valid_word(words)
 word_letters=set(word)
 alphabet=set(string.ascii_lowercase)
 used_letters=set()
 lives=6
 
 while len(word_letters)>0 and lives>0: 
  print("You have used these letters, "," ".join(used_letters) )
  word_list=[letter if letter in used_letters else "-" for letter in word]
  print(" ".join(word_list) )
  
  user_letter=input('Guess a letter: ')
  if user_letter in alphabet-used_letters:
    used_letters.add(user_letter)
    if user_letter in word_letters:
     word_letters.remove(user_letter)
    else:lives=lives-1
    
  elif user_letter in word_letters:
      print('You have already guessed that character')
  else: print("invalid character")
 while lives==0:
   print("sorry you died, the word is "+word)
 else:
   print("congrats, your guessed the word "+word)
   


hangman()

