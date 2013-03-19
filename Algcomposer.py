import sys
import random

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

def get_scale_steps(name_of_scale):
	"""
	Returns a list of the steps in the given scale

	To be used to interpret user input.
	"""

	scales = {"minor": [2,1,2,2,1,2,2],
			  "major": [2,2,1,2,2,2,1],
			  "harmonic": [2,1,2,2,1,3,1],
			  "dorian": [2,1,2,2,2,1,2],
			  "mixolydian": [2,2,1,2,2,1,2],
			  "pentatonic": [3,2,2,3,2]
			}

	return scales[name_of_scale]

def get_root_note_positions(root):
	"""
	Returns a list of the root note position on each string for every note
	"""

	first_positions = {"e": 0,
					   "f": 1,
					   "gf": 2,
					   "g": 3,
					   "af": 4,
					   "a": 5,
					   "bf": 6,
					   "b": 7,
					   "c": 8,
					   "df": 9,
					   "d": 10,
					   "ef": 11
					}
	first = first_positions[root]
	root_positions = [first, first + 7, first + 2, first + 9, first + 5, first]

	return root_positions

def strip_empty_lines(str):
	"""
	Takes an empty string and removes lines that contain only whitespace
	"""

	final_str = ""
	for line in str.split('\n'):
		if not line.isspace() and len(line) > 0:
			final_str += line + '\n'

	return """%s """ % final_str



def print_scale(scale):
	"""
	Prints a representation of the neck of the guitar for this specific scale
	"""

	for i in scale:
		print i

def change_key(note, scale, string, accidental=-1):
	"""
	This takes an input sequence of notes(guitar tablature) and changes it to a different key

	The simplest algorithm I will implement for composing music.
	Finds each note in the sequence and changes it to the closest note in the scale
	This keeps the melody very similar, but changes what key it is in.
	The melody may not be exactly the same because notes relative to each other will
	not always be preserved the same way.
	"""

	random_offset = 0
	min = 24
	min_fret = 24
	for fret in scale[string]:
		if abs(fret - note) < min:
			min = abs(fret - note)
			min_fret = fret

	if accidental > 0:
		rand_num = random.randrange(0, accidental, 1)
		if rand_num == 1:
			rand_num = random.randrange(0,1,1)
			if rand_num == 1:
				random_offset = 1
			else:
				random_offset = -1

	return min_fret + random_offset

def go_through_file(song, scale, method, accidental=-1):
	"""
	Goes through the input file(a song represented as guitar tablature) and performs the desired operation

	Arguments
	song - the file to be parsed
	scale - the scale being used
	method - What the user wants to do with this song
	accidental - The amount of randomness the user wishes to add(explained below)

	If the user wants to add an element of randomness, he or she may choose to include the last argument.
	This will give a 1/accidental chance of a randomly placed accidental note being returned.

	Methods so far: 'ck' = changes what key the song is in

	"""

	modified_song = ""
	string = 5
	previous_note = '-'
	song = strip_empty_lines(song)

	for note in song:
		if string < 0:
			modified_song += '\n'
			string = 5

		if note.isdigit():
			if previous_note.isdigit():
				note = previous_note + note
				note = int(note)
				previous_note = '-'
				if method == 'ck':
					str_to_add = str(change_key(note, scale, string, accidental))
					if len(str_to_add)>1:
						modified_song += str_to_add
					else:
						modified_song += str_to_add + '-'
			else:
				previous_note = note
		else:
			if previous_note.isdigit():
				non_note_char = note
				note = int(previous_note)
				previous_note = '-'
				if method == 'ck':
					modified_song += str(change_key(note, scale, string, accidental)) + non_note_char
			else:
				if note != '\n':
					modified_song += note
		if note == '\n':
			previous_note = '-'
			modified_song += '\n'
			string -= 1

	if previous_note.isdigit():
		if method == 'ck':
			modified_song += str(change_key(int(previous_note), scale, string, accidental))

	return modified_song
