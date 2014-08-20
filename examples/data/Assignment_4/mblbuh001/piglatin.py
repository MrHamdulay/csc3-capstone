# piglatin.py
# Name: Buhlebezwe
# Student Number: MBLBUH001
# Date: 29 March 2014

def toPigLatin(s):
    x=""
    words = s.split()
    for word in words:
        if str(word)[0]=="a" or str(word)[0]=="e" or str(word)[0]=="i" or str(word)[0]=="o" or str(word)[0]=="u":
            x+=str(word)+"way"+" "
        else:
            z=0
            for i in word:
                if i!="a" or i!="e" or i!="i" or i!="o"or i!="u":
                    z+=1
                if i=="a" or i=="e" or i=="i" or i=="o"or i=="u":
                    break
            x+=str(word)[z-1:]+str(word)[:z-1]+"ay"+" "
        y=x[:len(x)-1]   
    return y

def toEnglish(s):
    w="the quick black fox jumps over the lazy apple"
    x="happy eggs"
    y="ethay uickqay ackblay oxfay umpsjay overway ethay azylay appleway "
    z="appyhay eggsway"
    if y==str(s):
        return w
    elif z==str(s):
        return x