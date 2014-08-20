#Sachin Murugan
#MRGSAC001

def word(w):

	
	mn = len(w)
	first_letter = w[0]
	vowels = 'aeiouAEIOU'
	
	if first_letter in vowels:
		
		piglatin = w+'way'
		return piglatin
	
	else:
		pq = 0
		for run in w:
		
			if run in vowels:
				break
			pq+=1
		
		st = pq-1
		
		WordOne = w[pq:] 
		
		WordTwo = w[0:pq]
		
		piglatin_2 = WordOne+'a'+WordTwo+'ay'
		return(piglatin_2)


def toPigLatin (s):
	
	
	
	s = s + ' '
	WordTwo = ''
	w =''
	
	for run in s:
		
		if run != ' ':
			
			w = w+run
			
		elif run == ' ':
			piglatin = word(w)+ ' '
			
			WordTwo = WordTwo + piglatin
			
			w=''
	
	StringLength = len(WordTwo)-1
	
	WordThree = WordTwo[:StringLength]
	
	return(WordThree)


def word2 (w):
	
	mn = len(w)
	pq = mn - 3
	st = w[pq:]
	k = mn - 2
	l = w[k:]
	vowels = 'aeiouAEIOU'
	
	if st == 'way':
		
		EnglishWord = w[:pq]
		
		return(EnglishWord)
		
	elif l == 'ay':
		
		WordZ = w[:k]
		
		WordR = WordZ[::-1]

		z = 0
		
		x = len(WordR)
		
		
		for run2 in WordR:
			
			if run2 in vowels:
				break
			
			z += 1
		
		constants = WordR[:z]
		
		y = x - z - 1
		
		ConstantsR = constants[::-1]
		
		RestOfLetters = WordZ[:y]
		
		english = ConstantsR + RestOfLetters
		
		return(english)


def toEnglish (s):
	
	
	s = s + ' '
	WordTwo = ''
	w = ''
	
	for run in s:
		
		if run != ' ':
			
			w = w+run
			
		elif run == ' ':
			piglatin = word2(w)+' '
			
			WordTwo = WordTwo + piglatin
			
			w=''
	
	StringLength = len(WordTwo)-1
	
	WordThree = WordTwo[:StringLength]
	
	return(WordThree)
