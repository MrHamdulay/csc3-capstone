#question1

def check(word,ii,pairs):
    length=len(word)
    if ii>length-2:
        return ""
    else:
        if word[ii]==word[ii+1]:
            ii=ii+2
            pairs=pairs+1
            pairs=int(pairs)
            return str(pairs) + check(word,ii,pairs)
        else:
            ii=ii+1
            return str(pairs) + check(word,ii,pairs)
        
msg=input("Enter a message:\n")

if check(msg,0,0)[-1]<check(msg,0,0)[-2]:    
    print("Number of pairs: ",check(msg,0,0)[-2],check(msg,0,0)[-1],sep="")
else:
    print("Number of pairs:",check(msg,0,0)[-1])

