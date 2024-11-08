import random

print(".....Number Guessing game")
print("You have 7 guesses")

def num_guess_game ():
   rand_num = random.randint(0, 100)
   plays = 0
   while True:
    player_input = int(input("Enter random number:"))
    if player_input == rand_num:
      print("Correct")
      break
    elif player_input > rand_num:
      print("Too high")   
    elif player_input < rand_num:
      print("Too low")   
    else:
      print("invalid response")   
    plays += 1  
    print(f"You have used: {plays} trial(s)") 
    if plays >= 7:
      print("You have run out of attempts")
      break
num_guess_game()

while True:
   play_again = input("Would you like to play again?(y/n)")
   if play_again.lower() == "y":
      num_guess_game()
   elif play_again.lower() == 'n':
      break
   else:
      print("invalid response")