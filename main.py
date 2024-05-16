from art import logo
#from replit import clear
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
  return random.choice(cards)

def card_total(card_list):
  total=0
  for card in card_list:
    total+=card
  if total==21 and len(card_list)==2:
    total=0
  elif total>21 and 11 in card_list:
    card_list.remove(11)
    card_list.append(1)
    total=card_total(card_list)
  return total

play=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while play=='y':
  #clear()
  print(logo)
  my_card=[]
  comp_card=[]
  for _ in range(2):
    my_card.append(deal_card())
    comp_card.append(deal_card())
  my_total=card_total(my_card)
  comp_total=card_total(comp_card)
  if comp_total==0:
    print(f"  Your final hand: {my_card}, final score: {my_total}")
    print(f"  Computer's final hand: {comp_card}, final score: {comp_total}")
    print("You lose. Computer has a blackjack.")
  elif my_total==0:
    print(f"  Your final hand: {my_card}, final score: {my_total}")
    print("You win. You have a blackjack.")
  else:
    another_card='y'
    while another_card=='y':
      print(f"  Your cards: {my_card}, current score: {my_total}")
      print(f"  Computer's first card: {comp_card[0]}")
      another_card=input("Type 'y' to get another card, type 'n' to pass: ")
      if another_card=='y':
        my_card.append(deal_card())
        my_total=card_total(my_card)
        if my_total>21:
          print(f"  Your final hand: {my_card}, final score: {my_total}")
          print(f"  Computer's final hand: {comp_card}, final score: {comp_total}")
          print("You went over.You lose")
          another_card='n'
      else:
        print(f"  Your final hand: {my_card}, final score: {my_total}")
        while comp_total<17:
          comp_card.append(deal_card())
          comp_total=card_total(comp_card)
        print(f"  Computer's final hand: {comp_card}, final score: {comp_total}")
        if comp_total>21:
          print("Opponent went over. You win.")
        elif comp_total>my_total:
          print("You lose.")
        elif comp_total==my_total:
          print("Draw.")
        else:
          print("You win.")

  play=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")