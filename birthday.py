#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Git them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is

import random
ppl = 25
days = 365
trial = 10000
dup = 0
for i in range(trial):
	#creat empty calendar of zeros
	calendar = []
	for j in range(days):
		calendar.append(0)
	#print(calendar)
	#fill w/ random bdays
	for j in range(ppl):
		bday = random.randint(0, days-1)
		calendar[bday] += 1
	#print(calendar)
	#check for dups
	for day in calendar:
		if day > 1:
			dup += 1 
			break #how many calendars have a duplicate
print(dup, trial, dup/trial)
		 
	
	
	
"""
repeat trial
	create empty calendar
	fill w/ random bdays
	check for dups
	record
report dup/trial
"""
"""
python3 birthday.py
0.571
"""

