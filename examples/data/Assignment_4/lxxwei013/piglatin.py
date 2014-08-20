def toPigLatin(s):
    #eng=input("Enter an English sentence:\n")
    vowel="aeiou"
    #print("Pig-Latin:")
    engword=s.split()
    string1=""
    for word in engword:
        if word[0] in vowel:
            string1+=word+"way"+" "
        else:
            count=0
            for i in word:
                if i not in vowel:
                    count+=1
                    if count==len(word):
                        string1+="a"+ word+ "ay" +" "
                    vowel_index=0
                else:
                    vowel_index+=word.find(str(i))
                    index=vowel_index
                    string1+=word[index:]+"a"+word[:index]+"ay"+" "
                    break
    return string1
                
    
def toEnglish(s):
    #pig=input("Enter a Pig Latin sentence:\n")
    #print("English:")
    string2=""
    index=0
    for word in s.split(): 
        if word[:-4: -1]=="yaw":
            string2+=word[:len(word)-3]+" "
        else:
            for i in range(len(word)-3,-1,-1):
                if word[i]=="a":
                    index=i
                    break
            string2+=word[index+1:-2]+word[:index]+" "
                    
    return string2
    