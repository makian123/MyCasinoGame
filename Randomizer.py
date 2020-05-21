import random

def GenRandomColor():
	random.seed(a=None)
	number = random.randrange(37)
	if number % 2 == 0 and number != 0:
		color = 'r'
	elif number % 2 == 1:
		color = 'b'
	else:
		color = 'g'
	return color