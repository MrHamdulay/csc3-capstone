# question 3
# assignment 4
# nelisile mkhwebane

def toPigLatin (s):
    message=s.split()
    i=1
    state=''
    for word in message:
        vowel=word[0]
        if (vowel=="a") or (vowel=="e") or (vowel=="i") or (vowel=="o") or (vowel=="u"):
            state+=word+"way"+" "
        elif vowel=="w" or vowel=="W":
            word=word[1::]+'a'*i+ word[0:1]
            state+=word+"ay"+" "
        elif vowel==word[1]:
            word="a"+vowel+word[1]
            state+=word+"ay"
        elif vowel not in ('a','e','i','o','u'):
            while word[0] not in ('a','e','i','o','u'):
                word=word[1::]+'a'*i+ word[0:1]
                #i=0
            state+=word+'ay'+" "
    return state
    #print(word)
#toPigLatin()

def toEnglish(s):
    s=s.split()
    okay=""
    for word in s:
        if word[-3::1]=="way":
            okay += word[:-3]+" "
        elif word[-3::1]!= "way":
            remove=word[:-2:]
            posn=remove[::-1].find("a")
            okay += (remove[-(posn):]+remove[:-(posn)-1]) +" "
    return okay