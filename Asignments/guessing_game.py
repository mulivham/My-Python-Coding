import random

chosen_number = random.randint(1, 20)

print("Try to guess a number between 1 and 20.")

while True:
	user_guessed = input("Take a guess : ")
	if int(user_guessed) == int(chosen_number):
		print("Congrats,your guess is right.")
		break
	else:
		print("Wrong guess")