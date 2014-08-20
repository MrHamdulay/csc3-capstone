"""A program to convert English to Pig latin and reverse
ByFadzai Mupfunya
04 April 2014"""

def toPigLatin(s):
        sent=""
        for i in s.split():
                a=i[:1]
                if a == 'a' or a=='e' or a=='i' or a=='o' or a=='u':
                        b=i+"way "
                        sent+=b
        
                elif a not in "aeiou":
                                for j in range(len(i)):
                                        if i[j] in 'aeiou':
                                                cons=i[:j]
                                                cons2=i[j:]
                                                p=cons2+'a'+cons+'ay '
                                                sent+=p
                                                break
        return sent
                                               
                                
                                        
               
                                
                                
                                         
                                         
toPigLatin("lazy dude")
    