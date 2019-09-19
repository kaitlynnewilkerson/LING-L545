# segmenter.py
# Kaitlynne Wilkerson
# B659: Computation and Linguistic Analysis, Fall 2019
#
# Program should take a corpus and break it into sentences based on the presence of full stops

import sys

# reads in characters in a for loop (stops when there is no more input)
for char in sys.stdin.read():
# checks if character in variable char is an alphabetic character
# if so, saves current value of char to variable called charPrev
	if char.isalpha(): 
		charPrev = char
# checks if character in variable char is a full stop
# if so, saves current value of char to charPrev
	if char == '.': 
		charPrev = char
# checks if character in variable char is a space
# if so, checks if charPrev was a full stop
# if so, changes current value of char to new line
	if char == ' ':
		if charPrev == '.':
			char = "\n"
# prints char without new line (puts all characters on same line until full stop encountered)
	print(char, end = "")
# ensures that current value of char is saved to charPrev before new value is added to char
	charPrev = char

	
