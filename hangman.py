import random
import time

from anohangman import char

name= input("what is your name?    ")

print("Hello, "+name ,"Time to play Hangman")
print("")
words=['air','water','sky','land','fire','plants','animals',
       'tea','coffee','man','program','java','python']

# waiting for sec
time.sleep(1)
print()
time.sleep(0.5)

word = random.choice(words)
# creates a varaible for secret
guesses=' '
print("Guessess the character")
# detremine the terms

turns=10
# while loop for checking the guesses
while turns > 0:
    failed=0
    # guess for the character
    if char in word:

        if char in guesses:

            print(char),
        else:
            print(" ")
        failed += 1
        # if failed equals to zero
        # then you will win
        if failed==0:
            print("You Won")

            print("The word is ",word)
# break the loops
    break

# to player guess the guesses to find our secrect word

guess=input("enter your guess:  ")
guesses += guess

if guess not in word:
    turns -= 1
    print("Wrong")
    print("You have", + turns , "more guessess" )

    # if you are out of turns
    if turns==0:
        print("You Lose")


