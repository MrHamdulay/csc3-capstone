#MSRGRA002
#Grant Meeser
#03/04/2014

def isVowel(a):
	if a in 'AEIOUaeiou':
		return True
	else:
		return False

def pigLatinWord(s):

	i=0
	sub=''

	if isVowel(s[0]) :
		return s+'way'
	else:
		try:
			while not isVowel(s[i]):
				sub+=s[i]
				i+=1
		except:
			i=i
	return s[i:len(s):1]+'a'+sub+'ay'

def toPigLatin(s):
	words = s.split(' ')
	s=''
	for i in range(len(words)):
		s+=pigLatinWord(words[i])+' '
		s.strip()
	return s


def englishWord(s):
	s=s[::-1]
	sub=''
	i=2
	if s[0]=='y' and s[1]=='a' and s[2]=='w' :
		s= s[::-1]
		return s[0:len(s)-3:1]

	else: 
		while not isVowel(s[i]):
			sub+=s[i]
			i+=1
		s=s[i+1::1]+sub
		return s[::-1]
		

def toEnglish(s):
	words = s.split(' ')
	s=''
	for i in range(len(words)):
		s+=englishWord(words[i])+' '
		s.strip()
	return s

#print(toPigLatin(input('sentence->')))
