import random

number_chosen = random.randint(1, 11)
while True:
	user_guess = input("Guess a number between 0 and 10 : ")
	if int(user_guess) == int(number_chosen):
		print("Correct")
		break
	else:
		print("Wrong answer")
