def toPigLatin(s):
    """return the Pig Latin string for a given English string"""
    words=len(s.split())    
    pig=""    
    for i in range(0,words):
        currWord=s.split()[i]
        if(currWord[0]=='a' or currWord[0]=='e' or currWord[0]=='i' or currWord[0]=='u' or currWord[0]=='A' or currWord[0]=='E' or currWord[0]=='I' or currWord[0]=='O' or currWord[0]=='U' or currWord[0]=='o'):
            pig= pig+currWord+"way "
        else:
            for x in range(0,len(currWord)):
                if(currWord[x]=='a' or currWord[x]=='e' or currWord[x]=='i' or currWord[x]=='u' or currWord[x]=='A' or currWord[x]=='E' or currWord[x]=='I' or currWord[x]=='O' or currWord[x]=='U' or currWord[x]=='o'):
                    pig = pig + currWord[x:]+"a"+currWord[0:x]+"ay "
                    break
                else:
                    pig = pig + "a"+currWord+"ay "
                    break
    return pig

def toEnglish(s):
    word = s.split()
    space = ""
    for h in range(len(word)):
        wrd = word[h]
        if wrd[:-4:-1] == "yaw":
            wrd = wrd[:-3]
        else:
            wrd = wrd[:-2]
            acc = 0
            for m in wrd[::-1]:
                if m=='a':
                    wrd=wrd[len(wrd)-acc:]+wrd[:len(wrd)-acc-1]
                    break
                else:
                    acc+=1
        space += wrd+' '
    return space[:-1]

    