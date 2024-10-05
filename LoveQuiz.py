print("Welcome To My Love Quiz!")

playing = input("Do you want to play my love quiz? ")

if playing.lower() != "yes":
    quit()

print("Okay! It will be fun, let's go: ")
score = 0

answer = input("What month is our WEDDING anniversary? ")
if answer.lower() == "april":
    print('Correct! So cute!')
    score += 1
else:
    print("WRONG! So SAD")

answer = input("What state did we meet? ")
if answer.lower() == "kansas":
    print('Wow so sweet, so love!')
    score += 1
else:
    print("IS THERE NO LOVE")

answer = input("What is the doggos name? ")
if answer.lower() == "nelson":
    print('BEST BOI')
    score += 1
else:
    print("YOU not best BOI")

answer = input("kitties names? ")
if answer.lower() == "nala and nikki":
    print('Yes So CUTE')
    score += 1
else:
    print("They gonna get YOU")

print("You got " + str(score) + " questions correct! You DO love me! <3")
print("You got " + str((score / 4) * 100) + "%. ")