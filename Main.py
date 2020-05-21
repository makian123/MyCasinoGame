from Randomizer import GenRandomColor

def main():
	balance = 100
	bet = 0
	while True:
		if balance == 0:
			break
		print("Your balance is: ",balance,"$")

		pick = input("Type r for red, g for green or b for black: ")
		bet = int(input("Type your bet: "))

		if bet > balance:
			continue

		balance -= bet
		if pick == GenRandomColor():
			if pick == 'g':
				balance += 3 * bet
			else:
				balance += 2 * bet

if __name__ == "__main__":
	main()

print("You lost")