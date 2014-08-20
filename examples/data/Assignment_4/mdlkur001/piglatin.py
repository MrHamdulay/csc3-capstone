#MDLKUR001

def Kuresh(word):

	
	at = len(word)
	first_letter = word[0]
	vowels = 'aeiouAEIOU'
	
	if first_letter in vowels:
		
		piglatin = word+'way'
		return piglatin
	
	else:
		bj = 0
		for run in word:
		
			if run in vowels:
				break
			bj+=1
		
		co = bj-1
		
		word_1 = word[bj:] 
		
		word_2 = word[0:bj]
		
		piglatin_2 = word_1+'a'+word_2+'ay'
		return(piglatin_2)


def toPigLatin(s):
	
	
	
	s = s + ' '
	word2 = ''
	word = ''
	
	for run in s:
		
		if run != ' ':
			
			word = word+run
			
		elif run == ' ':
			piglatin = Kuresh(word)+' '
			
			word2 = word2 + piglatin
			
			word=''
	
	string_length = len(word2)-1
	
	word3 = word2[:string_length]
	
	return(word3)


def Kuresh2(word):
	
	at = len(word)
	bj = at - 3
	co = word[bj:]
	d = at - 2
	e = word[d:]
	vowels = 'aeiouAEIOU'
	
	if co == 'way':
		
		english_word = word[:bj]
		
		return(english_word)
		
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
	
	
	s = s + ' '
	word2 = ''
	word = ''
	
	for run in s:
		
		if run != ' ':
			
			word = word+run
			
		elif run == ' ':
			piglatin = Kuresh2(word)+' '
			
			word2 = word2 + piglatin
			
			word=''
	
	string_length = len(word2)-1
	
	word3 = word2[:string_length]
	
	return(word3)
