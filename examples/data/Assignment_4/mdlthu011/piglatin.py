

def toPigLatin(s):
	VOWELS = ('a', 'e', 'i', 'o', 'u')
	list_of_words = s.split(' ')
	new_sentence = ""   # we'll keep concatenating words to this...
	for word in list_of_words:
		first_letter = word[0]
		if first_letter in VOWELS:
			convert_word = word + "way"
		else:
			convert_word = word[1:] + word[0] + "ay"
		new_sentence = new_sentence + convert_word    # ...like this
		new_sentence = new_sentence + " "   # but don't forget the space!
	return new_sentence

def toEnglish(s):
	VOWELS = ('a', 'e', 'i', 'o', 'u')
	list_of_words = s.split(' ')
	new_sentence = "" 
	for word in list_of_words:
		first_letter = word[0]
		if first_letter in VOWELS:
			c_word = word[:3]
		else:
			c_word = word[3] + word[:2]
		new_sentence = new_sentence + c_word    # ...like this
		new_sentence = new_sentence + " "   # but don't forget the space!
	return new_sentence