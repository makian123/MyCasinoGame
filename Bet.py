from Randomizer import GenRandomColor

def MakeBet(bal, bet, pick):
	bal -= bet
	if pick == GenRandomColor():
		if pick == 'g':
			bal += 3 * bet
		else:
				bal += 2 * bet
	return bal