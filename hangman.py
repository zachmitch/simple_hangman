#BASIC HANGMAN GAME by Zach Mitchell v1.0 11/11/15


still_left = "These are the letters you have yet to choose: \n"
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
word = raw_input("Player one, choose a word for player two to guess: ").upper()
while word.isalpha() == False:
	word = raw_input("Please enter a word that contains ONLY letters: ").upper()
chances = len(word)
spacer = "*\n" * 20

print spacer
unguessed = [" _ "] * len(word)
wordout = []
emptylist = []
print "Player two:  You have been given %r chances.\nTry to guess this word: %r\n\n" % (chances, unguessed)
hereitis = "Here is the word thus far: %r\n You can miss %r more time/s." 
	
def checker(word):
	for x in word:
		emptylist.append(x)
		wordout.append(x)		
checker(word)

def available(choice):
	if choice.isalpha():
		choice = choice.upper()
		if choice in letters:
			gotit = letters.index(choice)
			letters[gotit] = "-"
		else:
			print "You guessed that already.  Sorry, you've lost a turn.\n" + hereitis  % (unguessed, chances)
	else:
		print "LETTERS only please.  Sorry, you've lost a turn."
		
def is_true(choice):
	return choice in word
	
def in_list(choice):
	return choice in emptylist
		
def visible(choice):
	print choice
	while in_list(choice) == True:
		if is_true(choice) == True:
			for t in word:
				if t == choice:
					plop = emptylist.index(t)
					emptylist[plop] = ""
					unguessed[plop] = choice
			print "YES!" + hereitis  % (unguessed, chances)
	if (in_list(choice) == False and is_true(choice) == False):
		print spacer
		print "Nope." + hereitis  % (unguessed, chances)
		
		
while chances >= 0:
	if unguessed == wordout:
		print spacer
		print "You win!  The word is %r." % word
		break
	elif chances == 0:
		print spacer
		print "You lose, sorry.  The word was %r." % word
		print "You only had %r." % unguessed
		break
	print still_left, letters
	choice = raw_input("\nChoose a letter: ").upper()
	if len(choice) > 1:
		choice = choice[0]
	print spacer
	loseit = choice in emptylist
	if loseit == False:
		chances -= 1
	in_list(choice)
	is_true(choice)
	available(choice)
	visible(choice)
	


	

	
		
