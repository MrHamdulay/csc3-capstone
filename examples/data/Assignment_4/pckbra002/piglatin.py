#module for PigLatin Conversions
#Assignment 4 Question 3
#2014/03/29
def findVowel(s):
    vowel = " a e i o u A E I O U"    
    for i in range(len(s)):#itterates through the length of the word
        if s[i] in vowel:#checks whether or not the current charactar is a vowel
            return i
    else:return -1
def toPigLatin(s):
    newS = ""
    vowel = " a e i o u A E I O U"
    for i in s.split():#splits the sentence
        if i[0] in vowel:#i is each word in the split sentence, checks if the first letter of the word i is a vowel
            i+="way"
            newS += i + " "#builds the new piglatin string
        else:#i.e. consonant 
            pos = findVowel(i)#finds the position of the vowel in the word using the findvowel def above
            if pos==-1: newWord= "a"+i+"ay"
            else:
                newWord = i[pos:]+"a"+i[:pos]+"ay"#builds the piglatin word by running from the vowel to the end of the word, then adding the beginning back with ay right at the end, as well as adding an 'a' as a sort of seperator
            newS+=newWord+" "
    return newS
def toEnglish(s):
    newS = ""
    vowel = " a e i o u A E I O U"
    for i in s.split():#splits the sentence
        if i[len(i)-3:] == "way":#checks if the last three letters are way
            newS += i[:(len(i)-3)] + " "#builds the new english string from the beginning to the part just before 'way'
        else:
            word = i[:len(i)-2]#removes 'ay' from the end of the string
            tempWord = word[::-1]#reverses the word to find the position of the vowel 'a' which determines how the sentence is translated back to English
            pos = len(word)-(findVowel(tempWord)+1)#because the position is of the reversed string, the position must be one more and then minused from the string length
            newS += word[pos+1:]+word[:pos]+" "#builds the correct English string
    return newS


