def toEnglish(s):     
    s=s.split(" ")
    empty = ""
    empty2 = ""
    empty3 = ""     
    for i in (s):
        if "way" in (i):
            wordlength = len(i)
            wordlength2 = wordlength-3
            remainder = (i[0:wordlength2])
            empty = empty+remainder
            empty = empty+" "
        else:
            wordlength = len(i)
            wordlength2 = wordlength-2
            slice1 = (i[0:wordlength2])
            slice1 = (slice1[-1::-1])
            for j in slice1:
                if j != "a":
                    empty2 = empty2+j
                else:
                    break
            empty2 = empty2[-1::-1]
            longword = len(empty2)
            slice1 = (slice1[-1:longword:-1])
            empty = empty+empty2+slice1+" "
            empty2 = ""
            slice1 = ""                                                        
    return(empty)


def toPigLatin(s):
    s=s.split(" ")
    empty = ""
    empty2 = ""
    empty3 = ""    
    vowels = "aeiou"
    for i in (s):
        for j in i[0]:
            if j in vowels:
                empty = empty+i+"way"+" "   
            else:
                for j in i:
                    if j not in vowels:
                        empty2 = empty2+j
                    else:
                        break
                a=len(empty2)
                empty3 = empty3+i[a:]
                empty = empty+empty3+"a"+empty2+"ay"+" "
                empty2 = ""
                empty3 = ""
    return(empty)
                    