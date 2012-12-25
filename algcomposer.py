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

def change_key(note, scale, string):
	"""
	This takes an input sequence of notes(guitar tablature) and changes it to a different key
	
	The simplest algorithm I will implement for composing music.
	Finds each note in the sequence and changes it to the closest note in the scale
	This keeps the melody very similar, but changes what key it is in.
	The melody may not be exactly the same because notes relative to each other will
	not always be preserved the same way. 
	"""

	min = 24
	min_fret = 24
	for fret in scale[string]:
		if abs(fret - note) < min:
			min = abs(fret - note) 
			min_fret = fret
	return min_fret

def go_through_file(song, scale, method):
	"""
	Goes through the input file(a song represented as guitar tablature) and performs the desired operation

	Arguments
	song - the file to be parsed
	scale - the scale being used
	method - What the user wants to do with this song
	"""

	modified_song = ""
	string = 0
	previous_note = '-'
	for note in song:
		print note
		if string > 6:
			string = 0
		
		if note.isdigit():
			if previous_note.isdigit():
				note = previous_note + note
				note = int(note)
				previous_note = '-'
				if method == 'ck':
					str_to_add = str(change_key(note, scale, string))
					if len(str_to_add)>1:
						print 'testing ' + modified_song
						modified_song += str_to_add
						print 'testing ' + modified_song
					else:
						modified_song += str_to_add + '-'
			else:
				previous_note = note
		else:
			if previous_note.isdigit():
				note = int(previous_note)
				previous_note = '-'
				if method == 'ck':
					modified_song += str(change_key(note, scale, string)) + '-'
			else:
				if note != '\n':
					modified_song += '-'
		if note == '\n':
			previous_note = '-'
			modified_song += '\n'
			string += 1
	
	if previous_note.isdigit():
		if method == 'ck':
			modified_song += str(change_key(int(previous_note), scale, string))

	return modified_song

input = sys.stdin

print '6'.isdigit()
print int('6' + '5') + 6
print go_through_file("--5--6--7--20\n1-5-3-3-5-6-7", get_scale([5,0,7,2,9,5],[2,2,1,2,2,2,1]), 'ck')
