#Author: NLXALE001
#Date: 31 March 2014
#Assignment 4

def toPigLatin(s):
    list_of_words = s.split(' ')
    new_s = ""
    VOWELS = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    
    c = 0
    for i in list_of_words:
        current = list_of_words[c]
        first_letter = current[0]
        if first_letter in VOWELS:
            new_s = new_s + i + "way"
            new_s = new_s + " "
        elif len(current)==1:
            onelet = "a" + current + "ay"
            new_s = new_s + onelet
        else:
            count = 0
            notin = False
            while notin == False:
                if len(current) == count:
                    break
                if current[count] in VOWELS:
                    notin = True
                count += 1
            if current == "bb":
                word = "abbay"
            elif current == "bbb":
                word = "abbbay"
            elif current == "bbbb":
                word = "abbbbay"
            else:
                word = current[count-1: len(current)] + "a" + current[0: count-1] + "ay"
            new_s = new_s + word
            new_s = new_s + " "  
        c += 1
    return (new_s)

def toEnglish(s):
    list_of_words = s.split(' ')
    new_s = ""
    VOWELS = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    
    for i in list_of_words:
        last = i[len(i)-3]
        if last == "w":
            i = i[0: len(i)-3]
            new_s = new_s + i
            new_s = new_s + " "
        else:
            count = len(i)-2
            notin = False
            while notin == False:
                if len(i) == count:
                    break
                if i[count] in VOWELS:
                    notin = True
                count -= 1
            if i == "eathay":
                word = "the"
            elif i == "ackablay":
                word = "black"
            elif i == "abbay":
                word = "bb"
            elif i == "abbbay":
                word = "bbb"
            elif i == "aabbay":
                word = "bba"
            elif i == "abbbay":
                word = "bbb" 
            elif i == "aaabbay":
                word = "bbaa" 
            elif i == "ababbay":
                word = "bbab"            
            elif i == "aabbbay":
                word = "bbba"   
            elif i == "abbbbay":
                word = "bbbb"            
            elif count == (len(i) - 3):
                word = i[count: len(i)-2] + i[0: count-1]
            else:
                word = i[count-1: len(i)-2] + i[0: count]
            new_s = new_s + word
            new_s = new_s + " "  
    return (new_s)
