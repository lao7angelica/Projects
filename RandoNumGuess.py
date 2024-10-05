import random 

top_of_range = input("Guess a NUMBER between 1 to 15: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
            print('Pls type a number larger than 0 next time.')
            quit()
else:
    print('Please type a number bro next time.')
    quit()
        
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
     guesses += 1
     user_guess = input("Make your guess buddy: ")
     if user_guess.isdigit():
          user_guess = int(user_guess)
     else:
          print('Please type a number weirdo.') 
          continue
     
     if user_guess == random_number:
          print("YOU DID IT!") 
          break
     elif user_guess > random_number:
          print("Bruh you were above the number!") 
     else:
          print("Brother you were below the number!")

print("You got it in", guesses, "guesses")




