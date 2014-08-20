# Assignment 4
# A program to translate English to Pig Latin and vice versa
# Frans van Hoek
# 3 April 2014


def toPigLatin (s):
    
    #variables
    count = 0
    temp = "a"
    
    # Split the sentence into a list of the words
   
    word = s.split(" ")
    
    # Loops through for each word in the sentence
    for i in word:
        
        if i[0] == 'a' or i[0] == 'e' or i[0] == 'i' or i[0] == 'o' or i[0] == 'u':
            word[count] = word[count] + "way"
            
        else:
            
            for j in i:
                
                if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
                    break
                
                else:
                    temp+= j
                    word[count] = i[len(temp)-1:] + temp + "ay"
                    
        temp = "a"
        # So that it goes to the next word in the sentence
        count+= 1
        
    return " ".join(word)
    
           
def toEnglish (s):
    
    count = 0
    word = s.split(" ")
    
    # Runs through each word in list
    for i in word:
        
        temp = ""
        
        if i.count("w") > 0:
            word[count] = word[count][:len(i)-3]
            
        else:
            word[count] = (word[count][:len(i)-2])[::-1]
            
            # Runs through letters in word i
            for j in word[count]:
                if j == 'a': break
                
                else:
                    temp += j
                    
            word[count] = ((word[count])[len(temp)+1:])[::-1]
            
            temp = temp[::-1]
            word[count] = temp + (word[count])
                
        
        temp = ""                
        count+=1
            
          
    return " ".join(word)