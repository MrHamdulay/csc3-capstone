#Assignment 4
#Question 3 piglatin
#Shaheen Karodia
#KRDSHA003
#2014-04-02
s=("The dumb upid dog")
vowels= ["a", "e", "i", "o", "u"]
consonants=["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n","p", "q", "r", "s", "t","v", "x", "y", "z"]

s=s.split(" ")
sentence=""

for i in s:
        if i[0] in vowels:
                
                sentence=sentence+(i)+("way")+(" ")
        if i[0] in consonants:
                b=0
                middle=""                
                for j in i:
                        if i[b] in vowels:
                                sentence=sentence+ i[b:]+ middle+ ("ay") + (" ") 
                                break

                        else:
                                middle=middle+j
                                b=b+1
                        
 
                                        
                                
print(sentence)
                        
                        
                        
        
                
                
                
                
        



    

