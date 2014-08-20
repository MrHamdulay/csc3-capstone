def toPigLatin(s):
    l = s.split()
    for x in range(len(l)):
        l[x] = str(l[x]).strip()     
    for x in range(len(l)):
        if any(str(l[x])[0] == str(y) for y in ['a','e','i','o','u','A','E','I','O','U']):
            l[x] = str(l[x]+"way")
        else:
            t = 0
            while t <len(str(l[x])) and str(l[x])[t] not in ['a','e','i','o','u','A','E','I','O','U'] :
                t = t+1
            l[x] = str(l[x])[t:len(l[x])]+"a"+str(l[x])[0:t]+"ay"
    r = ""
    for q in l:
        r =r+str(q)+" "
    return ( r)
                
def toEnglish(s):
    l = s.split()
    for x in range(len(l)):
        l[x] = str(l[x]).strip()
    for x in range(len(l)):
        if "way" in str(l[x]):
            l[x]=l[x].replace("way","")
        else:
            l[x] = str(l[x])[0:-2]
            t = str(l[x]).rfind("a")
            l[x] = str(l[x])[t+1:]+str(l[x])[0:t]
    r = ""
    for q in l:
        r =r+str(q)+" "
    return ( r)
            
