#quincy cele
#piglatin. py
#04 april 2014

def toPigLatin(s):
    changed_string=[]
    string=s.split()
    for i in range((len(string))):
        word1 =string[i]
        if word1[:1] in "aeiou":
            changed_string.append(word1+"way")
        else:
            count = 0
            for i in word1:
                if i not in "aeiou":
                    if count==len(word1)-1:
                        changed_string.append("a"+word1+"ay")
                    count +=1
                else:
                    changed_string.append(word1[count:]+"a"+word1[:count]+"ay")
                    break
                
    new_string=" ".join(changed_string)
    return new_string

def toEnglish(s):
    new_word=[]
    string=s.split()
    for i in range(len(string)):
        word1=string[i]
        if word1[-3:]== "way":
            new_word.append(word1[:len(word1)-3])
        else:
            word2= word1[:len(word1)-2]
            find_a=word2.rfind('a')
            new_word.append(word2[find_a+1:]+word2[:find_a])
            
    new_string= " ".join(new_word)
    return new_string
            
            
                
            