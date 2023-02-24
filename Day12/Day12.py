#Number Guessing Game Objectives:
import random
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def analyzer(mode):
  if mode =="easy":
    return EASY_ATTEMPTS
  else:
    return HARD_ATTEMPTS

def check_game(guessnumber,mynumber,attempts):
  if guessnumber < mynumber:
    print("Too low")
    print(f"You've got {attempts-1} left")
    return attempts-1
  elif guessnumber > mynumber:
    print("Too high")
    print(f"You've got {attempts-1} left")
    return attempts-1
  else:
    print(f"You've guess the number right! {guessnumber}") 

def play_game():
  print("Welcome to the guesssing game\n")
  print("I am thinking a number from 1 to 100\n")
# Include an ASCII art logo.
  mynumber =  random.randint(1,101)
  #print(f"the number I guessed was {mynumber}")
  diff = input("Type a difficulty level 'easy' or 'hard'\n")
  attempts = analyzer(diff)
  guessnumber = 0
  while guessnumber!=mynumber:
    guessnumber = int(input("Guess the number? "))
    attempts = check_game(guessnumber,mynumber,attempts)
    if attempts == 0:
      print(f"Fam you lost, the number I guessed was {mynumber}")
    

play_game()
    
  
    

  
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

