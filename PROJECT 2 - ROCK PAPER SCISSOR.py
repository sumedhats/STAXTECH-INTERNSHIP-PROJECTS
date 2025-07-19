import random
print("Welcome to rock paper scisssor game")
while True:
 my_choice = input("ROCK/PAPER/SCISSOR??").upper()
 choice = ['rock','paper','scissor']
 computer_choice = random.choice(choice).upper()
 print(f"MY CHOICE:{my_choice}")
 print(f"COMPUTER CHOICE:{computer_choice}")
 if my_choice == computer_choice:
   print("It is a draw")
 elif my_choice == "ROCK" and computer_choice == "SCISSOR"or my_choice == "ROCK" and computer_choice == "PAPER"or my_choice == "SCISSOR" and computer_choice == "PAPER":
   print("You won the game")
 else:
  print("You lost try again")
 game=input("Do you want to continue?(y/n)")
 if game == "n":
   print("Thank you")
   break
 else:
   continue
