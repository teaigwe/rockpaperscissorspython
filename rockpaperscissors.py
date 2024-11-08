while True:
 choice = input("Select rock, paper or scissors 'q' to quit:")
 options = ("rock", "paper", "scissors")
 option = random.choice(options)
 print(f"Your choice: {choice}")
 print(f"Computers choice: {option}")

 if choice.lower() == "q":
   break
 elif choice == "rock":
   if option == choice:
      print("Draw")
   elif option == "paper":
      print("You lose")
   elif option == "scissors":
      print("You win!")

 elif choice == "paper":
   if option == "rock":
      print("You win!")     
   elif option == choice:
      print("Draw")   
   elif option == "scissors":
      print("You lose!")

 elif choice == "scissors":
   if option == "rock":
      print("You lose")
   elif option == "paper":
      print("You win")
   elif option == choice:   
      print("Draw")
 else:
   print("invalid input")
