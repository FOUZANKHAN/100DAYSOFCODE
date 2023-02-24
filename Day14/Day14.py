#Learn how to retrive stuff from game data
# import random to get random part from data
# store the score in a global variable
# print the logo before and after
from art import logo,vs
from game_data import data
from replit import clear
import random

def printer(index):
  n = data[index]["name"]
  d = data[index]["description"]
  f = data[index]["follower_count"]
  c = data[index]["country"]
  return n,d,f,c

def comp(f1,f2):
  if f1>f2:
    return True
  else:
    return False

def checkanswer(guess,f1,f2):
  if f1 < f2:
    return guess == "a"
  else:
    return guess == "b"

def play_game():
  print(logo)
  game_should_continue = True
  score = 0
  celeb1 = random.randint(0,49)
  celeb2 = random.randint(0,49)
  while game_should_continue:
    celeb1 = celeb2
    celeb2 = random.randint(0,50)    
    n1,d1,f1,c1 = printer(celeb1)
    print(f"Compare A: {n1},{d1}, {c1}")
    print(vs)
    n2,d2,f2,c2 = printer(celeb2)
    print(f"Against: {n2},{d2},{c2}")
    guess = input("Who has more followers type 'A' or 'B'?: ").lower()#user says A
    is_correct = checkanswer(guess,f1,f2)
    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")
  
play_game()
  
  
  
