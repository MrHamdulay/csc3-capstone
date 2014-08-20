vowels = 'aeiouAEIOU'
lettera = "a"
def CountVowels(word):
        counter = 0
        for j in word:
                if j in vowels:
                        counter+= 1
        return counter
        
def  Firstvowelpos(word):
        for j in word:
                if j in vowels:
                        pos =word.index(j)  
                        return pos
def Findcon(word):
        for k in word:
                if k in lettera:
                        pos = word.index(k)
                        return pos
                
def toPigLatin(s):       
        individual = ""
        sentence = ""   
        newword = "" 
        word = s.split(" ")
        for i in s.split():
                individual += i[0]
        for i in range(len(individual)):   
                if individual[i] == "a" or individual[i] == "A" or individual[i] == "e" or individual[i] == "E" or individual[i] == "i" or individual[i] == "I" or individual[i] == "o" or individual[i] == "O" or individual[i] == "u" or individual[i] == "U":
                        newword = word[i]+"way "
                        sentence += newword
                else:
                        if CountVowels(word[i]) == 0:
                                newword = "a" +word[i] + "ay "
                                sentence += newword
                        else: 
                                point = Firstvowelpos(word[i])
                                newword = word[i][point:]+"a"+ word[i][:point] +"ay "
                                sentence += newword

        return sentence
def toEnglish(s):
        a= 0
        sentence = ""   
        newword = "" 
        sep = s.split(" ")
        word = ""
        for i in s.split():
                word = i
                identifier = word[-3:]
                secondidentifier = word[-2:]
                if identifier == "way":
                        newword = word[:-3]+" "
                        sentence += newword
                else:
                        noay = word[:-2]
                        reverse = noay[::-1]
                        point = Findcon(reverse)
                        newword = reverse[:point][::-1]+reverse[point+1:][::-1]+ " " 
                        sentence += newword
        return sentence
        

      
 






