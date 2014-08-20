"""Assignment 4, question 3
Jadon Thomson
2 April 2014"""

def toPigLatin(s):
     #if __name__=='__main__':
          s = s + ' '
          final_sentence = ''
          word = ''
          for i in (s):
               if i != ' ':
                    word += i 
               elif i == ' ':
                    dabble = word
                    word = ''
                    if dabble[0] in ("aeiouAEIOU"):
                         final_sentence += start_vowel(dabble) + ' '
                    else:
                         final_sentence += start_consonant(dabble) + ' '
          return final_sentence
    
    
def start_vowel(a):
     #if __name__=='__main__':
          new_vowel_word = ''
          a = a + 'way'
          new_vowel_word += a
          #return new_vowel_word
          return new_vowel_word
    
def start_consonant(a):
     #if __name__=='__main__':
          new_consonant_word = ''
          consonant = ''
          for i in a:
               if i in ("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRHSTVWXYZ"):
                    consonant += i
               else:
                    break
               new_consonant_word = a[len(consonant)::] + 'a' + consonant + 'ay'
          return new_consonant_word
    
    
    
    
#final_sentance += word
#print(final_sentence)
            

    
    
def toEnglish(s):
     #if __name__=='__main__':
          s = s + ' '
          final_sentence = ''
          word = ''
          for i in (s):
                    if i != ' ':
                              word += i
                              #print(word)
                    else:
                              if word[-3::] == 'way':
                                        new_word = word[:-3]
                                        final_sentence += new_word + ' '
                                        word = ''
                                        new_word = ''
                              else:
                                        consonants = ''
                                        new_word = word[:-2]
                                        counter = 0
                                        for i in (new_word[::-1]):      #sorting word backwards 
                                                  if i != 'a':               #using 'a' as a flag
                                                            counter += 1
                                                            consonants += i
                                                  else:
                                                            counter += 1
                                                            new_word = consonants[::-1] + new_word[:-(counter)]
                                                            final_sentence += new_word + ' '
                                                            new_word = ''
                                                            word = ''
                                                            break
                                                           #adding a string of constants
                                                              
          return final_sentence
                #print(new_word)
                
         
