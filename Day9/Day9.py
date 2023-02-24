from replit import clear
from art import logo
print(logo)
print("Welcome to the secret auction")
bidders_dict={}
f = True
while f:
  flag = input("Are there other bidders? type yes or no?: ").lower()
  if flag == "yes":
    name1 = input("Whats your name?: ")
    bid = input("What's your bid?: $")
    bidders_dict[name1]=bid
  else:
    print(f"The winner of the bid is {max(bidders_dict)}")
    f = False

  



#HINT: You can call clear() to clear the output in the console.
