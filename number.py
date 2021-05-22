import random
chances = 0
number = random.randint(1, 10)

while chances < 5:
    guess = int(input('Enter your guess between(1,10) :'))
    chances += 1
    if guess != number:
        if number > guess:
            print("Your Guess Was Low!!")
            print("Guess a number higher than", guess)
        elif number < guess:
            print("Your Guess Was High!!")
            print("Guess a number lower than ", guess)

    if guess == number:
        print("Congratulation!! You Win")
        break
if not chances < 5:
    print("You Lose!! your number was ", number)
