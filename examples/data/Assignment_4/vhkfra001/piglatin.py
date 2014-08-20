# Assignment 4
# A program to translate English to Pig Latin and vice versa
# Frans van Hoek
# 3 April 2014


def toPigLatin (s):
    
    #variables
    count = 0
    temp = "a"
    
    # Split the sentence into a list of the words
   
    items = s.split(" ")
    
    # Loops through for each word in the sentence
    for i in items:
        
        if i[0] == 'a' or i[0] == 'e' or i[0] == 'i' or i[0] == 'o' or i[0] == 'u':
            items[count] = items[count] + "way"
            
        else:
            
            for j in i:
                
                if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
                    break
                
                else:
                    temp+= j
                    items[count] = i[len(temp)-1:] + temp + "ay"
                    
        temp = "a"
        # So that it goes to the next word in the sentence
        count+= 1
        
    return " ".join(items)
    
           
def toEnglish (s):
    
    count = 0
    items = s.split(" ")
    
    # Runs through each word in list
    for i in items:
        
        temp = ""
        
        if i.count("w") > 0:
            items[count] = items[count][:len(i)-3]
            
        else:
            items[count] = (items[count][:len(i)-2])[::-1]
            
            # Runs through letters in word i
            for j in items[count]:
                if j == 'a': break
                
                else:
                    temp += j
                    
            items[count] = (items[count])[len(temp)+1:]
            items[count] = (items[count])[::-1]
            temp = temp[::-1]
            items[count] = temp + items[count]
            
        temp = ""
        count+=1
            
            
    return " ".join(items)