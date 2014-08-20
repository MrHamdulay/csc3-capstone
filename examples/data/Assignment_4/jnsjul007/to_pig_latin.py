vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

def to_pig_latin(x):
    for xStr in (x.split (" ")):
        for i in xStr:
            if x[0] == vowels:  
                print (x + "ay")
            if x[0,1] not in vowels:
                print(x[2,len(str(x))] + 'a' + x[1,2]+'ay')
to_pig_latin('and')