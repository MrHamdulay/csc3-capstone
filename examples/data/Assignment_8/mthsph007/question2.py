""" Sphiwe Muthembi
MTHSPH007
Assignment 8 - Question 2"""

#=======================================
#String to calculate the number of repeated characters in a string.
# Character pair cannot overlap.

#=======================================
sent = input('Enter a message:\n')

#=======================================

def count_pairs(sentence):
    count = 0
    if len(sentence) < 2:
        return count
    elif sentence[0] == sentence[1]:
        count+=1
        return count + count_pairs(sentence[2:])
    else:
        return count + count_pairs(sentence[1:])


print('Number of pairs:',count_pairs(sent))        
    
    

