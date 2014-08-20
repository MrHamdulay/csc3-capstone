def toPigLatin(s):
    z=s.split() # split string into substrinngs
    c=len(z)  #get length of string
    f=[] #create empty list
    for j in range(c):  # loop through each word in list
        d=z[j]
        

        if d[0]=='a' or d[0]=='e' or d[0]=='i' or d[0]=='o' or d[0]=='u':
           a=d+'way'
           e=a
        else:
            n=len(d)
            for i in range(n):
                if d[i]== 'a' or d[i]=='e' or d[i]=='i' or d[i]=='o' or d[i]=='u' :break
                i=i+1
#modify word according to rule of piglatin and append each word to new list f
            consonantmod='a'+d[0:i]+'ay'

            e=d[i:n]+consonantmod

        f.append(e)
        g=" ".join(f) #join each word in list to form a string
    return g    #return string


def toEnglish(s):
    z=s.split()
    c=len(z)
    f=[]
    for j in range(c):
        d=z[j]
        if d[-3] =='w':
            n=len(d)
            e=d[0:n-3] # give string without last three characters

        else:
            n=len(d)
            d2=d[:n-2]
            x=d2.rfind('a') # find first occurence of 'a' from right in d2
            h=d[n-3:x:-1]
            e=h[::-1]+d[:x]

        f.append(e)
        g=" ".join(f) #join each word in list to form a string
    return g    #return string
