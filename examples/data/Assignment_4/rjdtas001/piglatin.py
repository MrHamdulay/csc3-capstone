def toPigLatin(s):
    vowel="aeiou"
    eng=s.split()
    temp=0
    answer=""
    for words in eng:
        if words[0] in vowel:
            answer+=words+"way"+" "
        else:
            temp=0
            for i in words:
                if i not in vowel:
                    temp+=1
                    if temp==len(words):
                        answer+="a"+ words+ "ay" +" "
                    vowel_index=0
                else:
                    vowel_index+=words.find(str(i))
                    index=vowel_index
                    answer+=words[index:]+"a"+words[:index]+"ay"+" "
                    break
    return answer
                

def toEnglish(s):
    answer2= ""
    pos = 0
    for words in s.split():
        if words[:-4: -1]=="yaw":
            answer2+=words[:len(words)-3]+" "        
        else:
            for i in range(len(words) - 3, -1, -1):
                if words[i] =="a":
                    pos=i
                    break
            answer2+=words[pos+1:-2]+words[:pos]+" "   
    return answer2


    