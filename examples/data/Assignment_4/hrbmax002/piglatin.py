def toPigLatin(s):
    if s[len(s)-1] != " ":
        s = s + " "
    answer = ""
    while len(s)>0:
        temp = s[0:s.index(" ")]
        s = s[s.index(" ")+1:]
        if temp[0].upper() in ["A","E","I","O","U"]:
            temp = temp + "way "
        else:
            temp = temp + "a"
            while temp[0].upper() not in ["A","E","I","O","U"]:
                temp = temp[1:] + temp[0]
            temp = temp + "ay "
        answer = answer + temp
    answer = answer[0:len(answer)-1]
    return answer

def toEnglish(s):
    if s[len(s)-1] != " ":
        s = s + " "
    answer = ""    
    while len(s)>0:
        temp = s[0:s.index(" ")]
        s = s[s.index(" ")+1:]        
        if temp[-3:]=="way":
            answer = answer + " " + temp[0:-3]
        else:
            temp = temp[0:-2]
            while temp[-1] != "a":
                temp = temp[-1] + temp[0:-1]
            answer = answer + " " + temp[0:-1]
    return answer[1:]