# tokeniser.py
# Kaitlynne Wilkerson
# B659 Computation and Linguistic Analysis, Fall 2019
# 
# Program should take sentences and break them into tokens

import sys
# initializes a counter for each sentence
counterstr = 0 

# reads in a line from the text file in a loop until no more lines exist
for string in sys.stdin.readlines():
# increases sentence counter by 1
	counterstr = counterstr + 1
# prints information about sentence number and what is contained in the sentence
	print('# sent_id  = ', counterstr)
	print('# text = ', string, end = "")
# gets rid of all new lines in the text
	string = string.strip('\n')
# looks at each word in the sentence until no words exist
	for char in string: 
# if the word is matches to ',:.()', then spaces are added before or after it
		if char in ',:.': 
			string = string.replace(char, ' ' + char)
		if char == '(':
			string = string.replace('(', '( ')
		if char == ')':
			string = string.replace(')', ' )')
# initializes a counter for each word
	counterword = 0
	
# splits each word in the sentence by spaces	
	for char in string.split(' '):
#increases the word counter by 1
		counterword = counterword + 1
# prints word counter(converted to a string), a tab, the word, and 8 more tabs
		print(str(counterword) + '\t' + char + '\t_' * 8)
		
# prints a new line to separate each sentence; end = "" is included because it will print two new lines due to the new line feature built into print
	print('\n', end = "")
