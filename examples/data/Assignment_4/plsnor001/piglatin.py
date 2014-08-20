#-------------------------------------------------------------------------------
# Name:        piglatin
# Purpose: converts between pig_latin and english
# Author:      Pilusa
# Created:     02-04-2014
# Copyright:   (c) Pilusa 2014
#-------------------------------------------------------------------------------


def toPigLatin(s):
    convert=s.split(' ')  # splits sentence into words
    #convert=[word.lower() for word in convert] #converts words to lowercase
    new=[] #creates empty list to store converted words
    space=' '
    for word in convert: #converts vowel words to latin
        if word[0]=='a'or word[0]=='e'or word[0]=='i'or word[0]=='o'or word[0]=='u':
            p=word+'way'
            new.append(p)

        elif word[0]!='a'or word[0]!='e'or word[0]!='i'or word[0]!='o'or word[0]!='u': #converts consonant words to latin
            t=[] #empty string for new consonant word
            l=''
            for i in word: #checks every letter in consonant word to slice it and add to t
                if i=='a'or i=='e'or i=='i'or i=='o'or i=='u':
                    break
                else:
                    t.append(i)
            t=l.join(t)
            new_word=word[len(t):]+'a'+word[:len(t)]+'ay' #takes first consonant to the end of word the concatenates with ay

            new.append(new_word) # adds new consonant to new


    return space.join(new) #joins converted words together to form a new sentence

def toEnglish(s):
    #s='eathay uickaqay ackablay oxafay umpsajay overway eathay azyalay appleway'
    blend1=['bl','br','ch','cl','cr','dr','fl','fr','gl','gr','pl','pr','sc','sh','sk','sl','sm','sn','sp','st','th','tr']
    blend2=['sch','scr','shr','sph','spl','spr','squ','str','thr']
    vowels=['a','e','i','o','u']
    e=' '
    list=s.split(' ')   #split given sentence into words
    english=[]
    for word in list:
        if word.endswith('way'):     #converts vowel words piglatin back to english
            english.append(word[:-3])
        elif word.endswith('ay'):    #converts consonant words piglatin back to english

            if word[-5:-2] in blend2:
                english.append(word[-5:-2]+word[:-5])

            elif word[-4:-2] in blend1:
                english.append(word[-4:-2]+word[:-5])

            else:
               if word.startswith('a') and 'bb' in word:
                    english.append(word[-3:0:-1])
               else: english.append(word[-3]+word[:-4])

    final=e.join(english)
    #print(final)
    return final



if __name__ == '__main__':
    toEnglish('eathay uickaqay ackablay oxafay umpsajay overway eathay azyalay appleway aaabbay')

