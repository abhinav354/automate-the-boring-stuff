import random
secret = random.randint(1, 20)
print('I am thinking of a number between 1 and 20')

for i in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess > secret:
        print('Your guess is too low.')
    elif guess > secret:
        print('Your guess is too high.')
    else:
        break

if guess == secret:
    print('Good job! You guessed the number.')
    
