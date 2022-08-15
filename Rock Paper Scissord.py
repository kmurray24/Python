from random import randint

win_combo = [ ['Paper',    'Rock',     'covers'], 
	         ['Scissors', 'Paper',    'cuts'],
		    ['Rock',     'Scissors', 'smashes'] ]

Choices = ["Rock", "Paper", "Scissors"]

while True:
	player_choice   = input("\n\nRock, Paper, Scissors? ")
	computer_choice = Choices[randint(0,2)]
	choice_combo    = [player_choice, computer_choice]
	print( 'You chose', choice_combo[0],'.  Computer chose', choice_combo[1], '.')

	if choice_combo[0] == choice_combo[1]:
		print('Tie Game!')
		continue

	for scenario in win_combo:
		if choice_combo[0] == scenario[0] and choice_combo[1] == scenario[1]:
			print('You win! ', scenario[0], scenario[2], scenario[1])
		elif choice_combo[1] == scenario[0] and choice_combo[0] == scenario[1]:
			print('You lose! ', scenario[0], scenario[2], scenario[1])

	play_again = input("Play again? (y/n): ")
	if play_again.lower() != "y":
		break