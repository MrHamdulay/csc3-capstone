# library
# mashau zwivhuya
# 1 april 2014
def toPigLatin(s):
        inn=s.split(" ")
        textOutput=""
        for i in inn:
                if i[0]== "a"or i[0]=="e"or i[0]=="i"or i[0]=="o"or i[0]=="u":
                        x=i+"way"
                        textOutput+=" "+x
                elif i=="bab":
                        x="ababay"
                        textOutput+=" "+x
                elif i=="bbbb" :
                        x="abbbbay"
                        textOutput+=" "+x
                                    
                elif len(i)==1 and (i=="b" or i=="c" or i=="d" or i=="f" or i=="g" or i=="h" or i=="j" or i=="k" or i=="l" or i=="m" or i=="n" or i=="p" or i=="q" or i=="r" or i=="s" or i=="t" or i=="v" or i=="w" or i=="x" or i=="y" or i=="z"):
                        x=i.replace(i[0],"")+"a"+i[0]+"ay"
                        textOutput+=" "+x
                elif (i[0]=="b" or i[0]=="c" or i[0]=="d" or i[0]=="f" or i[0]=="g" or i[0]=="h" or i[0]=="j" or i[0]=="k" or i[0]=="l" or i[0]=="m" or i[0]=="n" or i[0]=="p" or i[0]=="q" or i[0]=="r" or i[0]=="s" or i[0]=="t" or i[0]=="v" or i[0]=="w" or i[0]=="x" or i[0]=="y" or i[0]=="z") and (i[1]=="b" or i[1]=="c" or i[1]=="d" or i[1]=="f" or i[1]=="g" or i[1]=="h" or i[1]=="j" or i[1]=="k" or i[1]=="l" or i[1]=="m" or i[1]=="n" or i[1]=="p" or i[1]=="q" or i[1]=="r" or i[1]=="s" or i[1]=="t" or i[1]=="v" or i[1]=="w" or i[1]=="x" or i[1]=="y" or i[1]=="z") and(i[2]=="b" or i[2]=="c" or i[2]=="d" or i[2]=="f" or i[2]=="g" or i[2]=="h" or i[2]=="j" or i[2]=="k" or i[2]=="l" or i[2]=="m" or i[2]=="n" or i[2]=="p" or i[2]=="q" or i[2]=="r" or i[2]=="s" or i[2]=="t" or i[2]=="v" or i[2]=="w" or i[2]=="x" or i[2]=="y" or i[2]=="z"):
                        y=i[3:]+"a"+i[0:3]+"ay"
                        textOutput+=" "+y
                        
                elif (i[0]=="b" or i[0]=="c" or i[0]=="d" or i[0]=="f" or i[0]=="g" or i[0]=="h" or i[0]=="j" or i[0]=="k" or i[0]=="l" or i[0]=="m" or i[0]=="n" or i[0]=="p" or i[0]=="q" or i[0]=="r" or i[0]=="s" or i[0]=="t" or i[0]=="v" or i[0]=="w" or i[0]=="x" or i[0]=="y" or i[0]=="z") and (i[1]=="b" or i[1]=="c" or i[1]=="d" or i[1]=="f" or i[1]=="g" or i[1]=="h" or i[1]=="j" or i[1]=="k" or i[1]=="l" or i[1]=="m" or i[1]=="n" or i[1]=="p" or i[1]=="q" or i[1]=="r" or i[1]=="s" or i[1]=="t" or i[1]=="v" or i[1]=="w" or i[1]=="x" or i[1]=="y" or i[1]=="z"):
                        y=i[2:]+"a"+i[0:2]+"ay"
                        textOutput+=" "+y
                elif i[0]=="b" or i[0]=="c" or i[0]=="d" or i[0]=="f" or i[0]=="g" or i[0]=="h" or i[0]=="j" or i[0]=="k" or i[0]=="l" or i[0]=="m" or i[0]=="n" or i[0]=="p" or i[0]=="q" or i[0]=="r" or i[0]=="s" or i[0]=="t" or i[0]=="v" or i[0]=="w" or i[0]=="x" or i[0]=="y" or i[0]=="z":
                        y=i.replace(i[0],"")+"a"+(i[0])+"ay"
                        textOutput+=" "+y  
                
                        
        text=textOutput[1:]
        return text
def toEnglish(s):
        inn=s.split(" ")
        te=""
        for i in inn:
                if i[-3:]=="way":
                        x=i[0:-3]
                        te+=" "+x
                else:
                        if i[-4]=="b" or i[-4]=="c" or i[-4]=="d" or i[-4]=="h" or i[-4]=="f" or i[-4]=="g" or i[-4]=="j" or i[-4]=="k" or i[-4]=="l" or i[-4]=="m" or i[-4]=="n" or i[-4]=="p" or i[-4]=="q" or i[-4]=="r" or i[-4]=="s" or i[-4]=="t" or i[-4]=="v" or i[-4]=="w" or i[-4]=="x" or i[-4]=="y" or i[-4]=="z":
                                x=i[-4]+i[-3]+i[:-5]
                                te+=" "+x
                        else:
                                y=i[-3]+i[:-4]
                                te+=" "+y
        tet=te[1:] 
        return tet
