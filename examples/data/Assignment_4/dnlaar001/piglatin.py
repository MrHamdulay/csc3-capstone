def toPigLatin (s):
    consonants=['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z','d','b','c','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z']
    d=s.split(' ')
    for i in [d]:
        h=i[:1]
        if h=='a'or h=='e' or h=='i' or h=='u' or h=='o':
            r=i+'way'
            return r

        elif h[0]==consonants:
            z=i+'a'
            g=z.split(' ')
            while g[0]==consonants:
                ss=z[1:]
                ii=z[:1]
                z=ss+ii
                return z
            v=z+'ay'
            return v
        
def toEnglish (s):
    consonants=['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z','d','b','c','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z']
    d=s.split(' ')
    for i in [d]:
        p=i[len(i)-3:len(i)-4:-1]
        if i[len(i)-1:len(i)-5:-1]=='yaw':
            r=i[:len(i)-2]
            return r
        elif i[len(i)-1:len(i)-4:-1]=='ay' and p[0]==consonants:
            z=i[:len(i)-3]
            d=z[::-1]
            rr=d.split(' ')
            while rr[0]==consonants:
                gg=d[1:]
                ff=d[:1]
                d=gg+dd
                return d
            f=d[1:]
            j=f[::-1]
            return j
        

            
            
            



        
                
            
            


        