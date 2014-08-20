def toPigLatin (s):
	vowels = ('a','e','i','o','u','A','E','I','O','U')
	words = s.split(" ")
	for i, word in enumerate(words):
		if word.startswith(vowels):
			#print("In the if statement")
			words[i] = word + "way"
		elif len(words[i]) == 1:
			words[i] = "a" + word + "ay"
		else:	
			x = 1
			while not word[x::].startswith(vowels):
				x += 1
				if x == len(word):
					break
				#print("in while")
			if word[x::].startswith(vowels):
				#print("starts with vovel!!")
				words[i] = word[x::] + "a" + word[:x:] + "ay"
			else:
				#print("doesn't contain a vovel!!")
				words[i] = "a" + word + "ay"
	return (' '.join(words))
	
	
def toEnglish (s):
	words = s.split(" ")
	for i, word in enumerate(words):
		if word[-3::] == "way":
			words[i] = word[0:-3:]
		else:
			#print("in the else section")
			wordLetters = list(word[0:-2:])
			#print("here is a list of the leters of the given word", wordLetters)
			while True:
				if len(wordLetters) >= 1:
					poppedLetter = wordLetters.pop(-1)
				else:
					break
				if poppedLetter != "a":
					if len(wordLetters) >= 1:
						wordLetters[:0] = poppedLetter
					else:
						wordLetters[0] = poppedLetter
				else:
					#print("Break STATEMENT\n*********\n***********")
					break
			words[i] = ''.join(wordLetters)
	return (' '.join(words))


'''

 To convert from English to Pig Latin, each word must be transformed as follows:

    if the word begins with a vowel, "way" should be appended (example: apple becomes appleway)
    if the word begins with a sequence of consonants, this sequence should be moved to the end, prefixed with "a" and followed by "ay" (example: please becomes easeaplay)

Assume that the English text does not contain the letter "w".

Write a Python module with the following functions:

    toPigLatin (s), to return the Pig Latin string for a given English string
    toEnglish (s), to return the English string for a given Pig Latin string

 Sample I/O:

(E)nglish or (P)ig Latin?
E
Enter an English sentence:
the quick black fox jumps over the lazy apple
Pig-Latin:
eathay uickaqay ackablay oxafay umpsajay overway eathay azyalay appleway

Sample I/O:

(E)nglish or (P)ig Latin?
P
Enter a Pig Latin sentence:
eathay uickaqay ackablay oxafay umpsajay overway eathay azyalay appleway
English:
the quick black fox jumps over the lazy apple


'''
