# Tashiv Sewpersad
# Assignment 4 - Question 3
# 30 - 3 - 2014

def toPigLatin(sSentence):
	sVowels = ["a","e","i","o","u"]
	sSentence = sSentence + " "
	sResult = ""
	iPos = sSentence.find(" ")
	while iPos > -1:
		sWord = sSentence[0:iPos]
		if sWord[0] in sVowels:
			sWord += "way"
		else:
			iLen = len(sWord)
			iLoc = iLen
			for i in range(iLen):
				if sWord[i] in sVowels:
					iLoc = i
					break		
			sWord = sWord[iLoc::1] + "a" + sWord[0:iLoc] + "ay"
		sResult += sWord + " "
		sSentence = sSentence[iPos+1::1]
		iPos = sSentence.find(" ")
	return sResult[0:len(sResult)-1]	

def toEnglish(sSentence):
	sVowels = ["a","e","i","o","u"]
	sSentence = sSentence + " "
	sResult = ""
	iPos = sSentence.find(" ")
	while iPos > -1:
		sWord = sSentence[0:iPos]
		if sWord.find("way") > -1:
			sWord = sWord[0:len(sWord)-3]
		else:
			sWord = sWord[0:len(sWord)-2]
			iLoc = 0
			sRange = sWord[::-1]
			iLen = len(sRange)
			for i in range(iLen):
				if sRange[i] in sVowels:
					iLoc = iLen-i-1
					break
			sWord = sWord[iLoc+1:iLen] + sWord[0:iLoc]		
		sResult += sWord + " "
		sSentence = sSentence[iPos+1::1]
		iPos = sSentence.find(" ")
	return sResult[0:len(sResult)-1]	