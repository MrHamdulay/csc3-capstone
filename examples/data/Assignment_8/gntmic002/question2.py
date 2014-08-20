#Assignment 8.2
#Michael Gant
#05/05/2014

def Pairs(sText):
    if len(sText) < 2:
        return 0
    elif len(sText) == 2:
        if sText[0] == sText[1]:
            return 1
        else:
            return 0
    elif sText[0]==sText[1] :
        return 1 + Pairs(sText[2:])
    else: 
        return Pairs(sText[1:])

sInput = input("Enter a message:\n")
print("Number of pairs: " + str(Pairs(sInput)))