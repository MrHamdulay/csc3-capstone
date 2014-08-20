# Question 3

# Write a module to translate sentences between English and a variant of Pig Latin (see: http://en.wikipedia.org/wiki/Pig_Latin).

# To convert from English to Pig Latin, each word must be transformed as follows:

# if the word begins with a vowel, "way" should be appended (example: apple becomes appleway)
# if the word begins with a sequence of consonants, this sequence should be moved to the end, prefixed with "a" and followed by "ay" 
#(example: please becomes easeaplay)
# Assume that the English text does not contain the letter "w".

# Write a Python module with the following functions:

# toPigLatin (s), to return the Pig Latin string for a given English string
# toEnglish (s), to return the English string for a given Pig Latin string
# Sample I/O:

# (E)nglish or (P)ig Latin?
# E
# Enter an English sentence:
# the quick black fox jumps over the lazy apple
# Pig-Latin:
# eathay uickaqay ackablay oxafay umpsajay overway eathay azyalay appleway
# Sample I/O:

# (E)nglish or (P)ig Latin?
# P
# Enter a Pig Latin sentence:
# eathay uickaqay ackablay oxafay umpsajay overway eathay azyalay appleway
# English:
# the quick black fox jumps over the lazy apple

def is_vowel(c):
	vowels = "aeiou"
	vowels.find(c.lower())
	if vowels.find(c.lower()) == -1:
		return False
	else:
		return True
#Filtering function


def toPigLatin (sent):
	new_word = ''
	dammit = ''
	for a in sent.split(" "):
		if is_vowel(a[0]):
			a = a+"way "
			dammit = dammit + a
		else:
			for i in range(len(a)):
				if  not is_vowel(a[i]):
					if i == (len(a)-1):
						new_word = a[i+1:]+"a"+a[0:i+1]+"ay "
						dammit = dammit + new_word
					new_word = a[i+1:]+"a"+a[0:i+1]+"ay " 	
				else:
					dammit = dammit + new_word
					break
	return dammit
	

def toEnglish (sent):
	sec = '' 
	for a in sent.split(" "):
		if a[-3:] == "way":
			sec = sec + a[0:-3]+ " "
		else:	
			n = -3
			new_word = ''
			while True:
				if a[n] == 'a':
					new_word = new_word+ a[:n] + " "
					break
				else:
					new_word = a[n] + new_word
					n = n-1
			sec = sec + new_word
	return(sec)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	

			
