import random

# (20 - (12 - BONUS)- (12+1)*0.5) / 20
# add 1 to bonus to factor in winning on a tie


# this code here is here to verify the result makes sense

def brute_force_poc():
	athletics_bonus = 11
	weapon_bonus = 11
	con_bonus = 3
	max_hit_dice = 10
	level = 11

	
	win_counter = [0,0,0,0]
	gold_sum = 0
	tries = 100000
	for _ in range(tries):
		wins = 0
		if random.randint(1, 20) + athletics_bonus >= random.randint(1, 12) + 12:
			wins += 1
		if random.randint(1, 20) + weapon_bonus >= random.randint(1, 12) + 12:
			wins += 1
		if random.randint(1, 20) + con_bonus + random.randint(1, max_hit_dice) >= random.randint(1, 12) + 12:
			wins += 1
		
		gold_sum += wins * 50 * level
		win_counter[wins] += 1

	print("Results from brute force: {}".format(gold_sum / tries))
	for counter, item in enumerate(win_counter):
		print("Number of wins: {}, probability {}".format(counter, item / tries * 100))

	print("End of brute force\n\n")


def calculate_earnings_math():
	athletics_bonus = 11
	weapon_bonus = 11
	con_bonus = 8 ## 3 + 1d10, rounded down
	level = 11


	a = (20-(11 - athletics_bonus)-(12+1)*0.5) / 20
	w = (20-(11 - weapon_bonus)-(12+1)*0.5) / 20
	c = (20-(11 - con_bonus)-(12+1)*0.5) / 20

	three_wins_probability = (a * w * c)
	two_wins_probability = a * w * (1 - c) + a * c * (1 - w) + w * c * (1 - a)
	one_wins_probability = a * (w-1) * (c-1) + w * (a-1) * (c-1) + c * (w - 1) * (a-1)
	zero_wins_probability = (1-a) * (1-w) * (1-c)


	average_wins = three_wins_probability * 3 + two_wins_probability * 2 + one_wins_probability * 1
	

	print("Results from math: {}".format(average_wins * level * 50)) 
	print("Number of wins: 0, probability {}".format(zero_wins_probability * 100))
	print("Number of wins: 1, probability {}".format(one_wins_probability * 100))
	print("Number of wins: 2, probability {}".format(two_wins_probability * 100))
	print("Number of wins: 3, probability {}".format(three_wins_probability * 100))


brute_force_poc()
calculate_earnings_math()
