# Pig Latin conversions
# Kristin Kinmont
# 30 March 2014

def toPigLatin(s):
    PigLatin = ""
    for i in s.split(" "):
        if i[0] in "aeiou":
            PigLatin += i+"way"+" "
        
        else:
            constanents = ""
            count = 0
            for j in i:
                if j in "aeiou": break
                else:
                    constanents += j
                    count += 1
            PigLatin += i[count:]+'a'+i[0:count]+"ay"+" "
    return PigLatin
            

def toEnglish(s):
    English = ""
    for i in s.split(" "):
        if i[-1:-4:-1]=="yaw":
            English += i[0:-3]+" "
        else:
            prefix = i[0:-2]
            reverse = prefix[::-1]
            count = 0
            for j in reverse:
                if j == "a": break
                count +=1
            English += prefix[count*(-1):]+prefix[:(-count-1)]+" "
    return English


#s="the quick black fox jumps over the lazy apple"
#print(toPigLatin(s))
#print('-'*15)
#print(toEnglish(toPigLatin(s)))
