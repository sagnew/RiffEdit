import sys

"""
Takes a text guitar tab input, and changes the music to a different key with a different melody.
This is my attempt at writing a script to perform algorithmic musical composition.

Current idea: 
Represent each scale as a 2D array corresponding to string and fret number(0 being the low E and 5 being the high e)

Input: A guitar tab text file(preferably one compatible with Guitar Pro's format)
Output: Another guitar tab text file that is modified to be a different composition with the same rhythm.
"""

def get_scale(roots, steps):
	"""
	Returns a 2D list of each note on each string that is in a specific key.
	
	Arguments:
	roots: A list of root notes of the scale corresponding to where this note is on each string
	steps: The order in which the scale steps(whole steps and half steps)

	Example: root = 5, 0, 7, 2, 9, 5, steps = 2212221 would correspond to an A major scale.
	"""

	scale = []
	for note in roots:
		scale.append([note])

	#This loop structure goes through each string, and ascends the scale all the way up to fret 24
	for string in scale:
		num = string[0]
		while num <= 24:
			for step in steps:
				num += step
				if num > 24:
					break
				string.append(num)

	#This loop does the same thing, but from the root note down to the open string(fret 0)	
	for string in scale:
		num = string[0]
		while num >= 0:
			for step in steps[::-1]:
				num -= step
				if num < 0:
					break
				string.insert(0, num)
	
	return scale

def print_scale(scale):
	"""
	Prints a representation of the neck of the guitar for this specific scale
	"""
	
	for i in scale:
		print i

def change_key(song, scale):
	"""
	This takes an input sequence of notes(guitar tablature) and changes it to a different key
	
	The simplest algorithm I will implement for composing music.
	Finds each note in the sequence and changes it to the closest note in the scale
	This keeps the melody very similar, but changes what key it is in.
	The melody may not be exactly the same because notes relative to each other will
	not always be preserved the same way. 
	"""

	string = 0
	previous_note = ''
	for note in song:
		if string > 6:
			string = 0
		if note == '\n':
			string++

		#This might be a retarded idea. Check to see if note is numeric	
		if note in range(0, 0, 9):
			previous_note = note
			continue

input = sys.stdin

get_scale([5,0,7,2,9,5],[2,2,1,2,2,2,1])
