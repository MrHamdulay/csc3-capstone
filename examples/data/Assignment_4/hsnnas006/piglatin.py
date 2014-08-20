'''module to convert english to piglatin and back
by nasreen
23/04/14'''

#function to convert english to piglatin
def toPigLatin(s):
    english_list = s.split(' ') # splits sentence into list
    new_list = []
    for word in english_list:
        if word[0] in 'aeiou': # do if first letter is a vowel
            pl_word = word+'way'
        else: # do if word begins with consonant[s]
            word = word + 'a' # add 'a' to end of word, before loop
            for i in range(len(word)):
                if word[0] in 'bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXyYzZ':
                    word = word+str(word[0]) # append i to end of word, if i is a consonant
                    word = word[1:] # delete first letter of word, if it has been appended
            pl_word = word + 'ay'    # add 'ay' to word, after loop
        new_list.append(pl_word) # add piglatin word to list
    pig_latin = ' '.join(new_list) # merge list into sentence
    return pig_latin

#function to convert piglatin to english
def toEnglish(s):
    piglatin_list = s.split(' ')
    new_list = []
    for word in piglatin_list:
        if word[len(word)-3] == 'w':
            eng_word = word[:(len(word)-3)] #remove 'way' from end of word
        else:
            word = word[:(len(word)-2)] #remove 'ay' from end of word
            reverse_word = word[::-1] #reversing word makes it easier to work with
            for i in range(len(reverse_word)):
                if reverse_word[0] in 'bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVWxXyYzZ':
                    reverse_word = reverse_word+str(reverse_word[0])
                    reverse_word = reverse_word[1:]     
            reverse_word = reverse_word[1:] #removes 'a' from start of reverse_word
            eng_word = reverse_word[::-1]
            
        new_list.append(eng_word)
    english = ' '.join(new_list)
    return english