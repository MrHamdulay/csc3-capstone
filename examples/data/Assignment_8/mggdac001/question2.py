count=0
def alphaPairCount(k):
    m=k.split()
    s=''.join(m)    
    global count
    #print(s)
    if (len(s))==0:
        print('Number of pairs:',((count)//2),end='')
   
    elif s[0] in s[1:]:
        count+=1
        return alphaPairCount(s[1:])
    
    else:
        return alphaPairCount(s[1:])

k=input('Enter a message:\n')
alphaPairCount(k)
