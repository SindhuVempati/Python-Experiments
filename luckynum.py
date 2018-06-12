from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)
turn =1
guesses_left = 3
while guesses_left!=0:
  print "Turn ",turn
  guess = int(raw_input("Your guess: "))
  if random_number == guess:
    print "You win!"
    break
  guesses_left-=1
  turn+=1
else:
  print "You lose."
