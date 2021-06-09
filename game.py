from numpy import random

# picks numbers between 0 and 1
# round ends when the sum of the numbers is greater than 1
# sx is the sum of the numbers (x)
# r is the rounds that each game lasted
# rounds is a list of r for any given number of trials

rounds = []
def game():
	sx, r = 0.0, 0
	print('Your numbers:')
	while sx <= 1:
		x = random.uniform(0,1)
		sx += x
		r += 1
		print(x)
	rounds.append(r)
	#print(rounds)
	print('your game lasted ' + str(r) + ' rounds')
trials = 5
for i in range(trials):
	game()
score = sum(rounds)
avg = score/trials
print('Average rounds of games is ' + str(avg)) #comment out prints besides this line try with large trials
