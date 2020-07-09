"""
Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
"""
import random

random_num = random.randint(1,101)
count = 0

print(random_num)
print("Let's play the guessing game!")

while(True):

	guess = int(input("What is your guess?"))
	if guess < 1 or guess > 100:
		count += 1
		print("OUT OF BOUNDS") 
		continue
	elif guess ==random_num:
		count += 1
		print(f"Correct! It took you {count} guesses")
		break
	elif count == 0 and (guess - 10 <= random_num <= guess + 10):
		count+=1
		print("WARM!")
		old_guess = guess
		continue
	elif count == 0 and not (guess - 10 <= random_num <= guess + 10):
		count+=1
		print("COLD!")
		old_guess = guess
		continue
	elif abs(guess - random_num) < abs(old_guess - random_num):
		count+=1
		print("WARMER!")
		old_guess = guess
		continue
	elif abs(guess - random_num) > abs(old_guess - random_num):
		count+=1
		print("COLDER!")
		old_guess = guess
		continue
	


