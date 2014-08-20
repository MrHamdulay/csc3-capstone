# Emmalene Naicker
# Assignment 8
# Programme to count the number of pairs of repeated characters in a string

number=0
def double_number(word,number):
    
    if len(word)==1 or len(word)==0: # return how many doubles if only one letter is left 
        return number
    
    elif word[0]==word[1]:# slice letters if there are consecutive letters  
        number+=1 # add 1 to count
        return double_number(word[2:],number)
    
    else: # remove the first letter
        return double_count(word[1:],number)
    
if __name__=='__main__':
    word=input('Enter a message:\n')
    print('Number of pairs:',double_number(word,number))