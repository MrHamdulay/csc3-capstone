def my_own(word):
	#Function that converts words to pig latin#
	
	a = len(word)
	first_let = word[0]
	vowels = 'aeiouAEIOU'
	
	if first_let in vowels:
		
		piglatin = word+'way'
		return piglatin
	
	else:
		b = 0
		for run in word:
		
			if run in vowels:
				break
			b+=1
		
		c = b-1
		
		word_1 = word[b:] # letters after the first consonants
		
		word_2 = word[0:b] # first letter consonants
		
		piglatin_2 = word_1+'a'+word_2+'ay'
		return(piglatin_2)


def toPigLatin(s):
	
	'''Function that seperates words converts the to pig latin and then recreates a sentance'''
	
	s = s + ' '
	word2 = ''
	word = ''
	
	for run in s:
		
		if run != ' ':
			
			word = word+run
			
		elif run == ' ':
			piglatin = my_own(word)+' '
			
			word2 = word2 + piglatin
			
			word=''
	
	string_len = len(word2)-1
	
	word3 = word2[:string_len]
	
	return(word3)


def my_own_2(word):
	
	a = len(word)
	b = a - 3
	c = word[b:]
	d = a - 2
	e = word[d:]
	vowels = 'aeiouAEIOU'
	
	if c == 'way':
		
		eng_word = word[:b]
		
		return(eng_word)
		
	elif e == 'ay':
		
		word_z = word[:d]
		
		word_r = word_z[::-1]

		z = 0
		
		x = len(word_r)
		
		
		for run2 in word_r:
			
			if run2 in vowels:
				break
			
			z += 1
		
		constants = word_r[:z]
		
		y = x - z - 1
		
		constants_r = constants[::-1]
		
		rest_of_letters = word_z[:y]
		
		english = constants_r + rest_of_letters
		
		return(english)


def  toEnglish(s):
	#Fuction that seperates words converts the sentance to English and then recreates a sentance'''
	
	s = s + ' '
	word2 = ''
	word = ''
	
	for run in s:
		
		if run != ' ':
			
			word = word+run
			
		elif run == ' ':
			piglatin = my_own_2(word)+' '
			
			word2 = word2 + piglatin
			
			word=''
	
	string_len = len(word2)-1
	
	word3 = word2[:string_len]
	
	return(word3)
