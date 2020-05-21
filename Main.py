from Bet import MakeBet

def main():
	print('Here are the rules:\nEvery number divisible by 2 is red\nEvery number not divisible by 2 is black, \nNumber 0 is green\n')
	balance = 100
	bet = 0
	while True:
		if balance == 0:
			break
		print("Your balance is:",balance,"$")

		pick = input("Type r for red, g for green or b for black: ")
		bet = int(input("Type your bet: "))

		if bet > balance:
			continue

		balance = MakeBet(balance, bet, pick)

if __name__ == "__main__":
	main()

print("You lost")