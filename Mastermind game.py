print("Welcome player 1")
player1=input("Please enter a 4 digit number with spacing : ")
player1=player1.split()
print(player1)
print("Player 2's turn")

for i in range(50):
      print('***')
while True:
      guess=input("Please guess a 4 digit number with spacing:")
      guess=guess.split()
      print(guess)
 
      if guess==player1:
            print("congradulations you win.")
            break

      else:
            if guess[0]==player1[0]:
                  print("Your first digit is right")
            if guess[1]==player1[1]:
                  print("Your second digit is right")
            if guess[2]==player1[2]:
                  print("Your third digit is right")
            if guess[3]==player1[3]:
                  print("Your last digit is right")

      continue


