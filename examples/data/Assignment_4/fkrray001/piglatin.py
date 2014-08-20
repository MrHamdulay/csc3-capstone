# Rayaan Fakier FKRRAY001
# 02 - 04 - 2014
# Program to convert an english sentence to PigLatin and vice-versa

def toPigLatin(s):
    list1 = []
    i = 0
    for x in s:
        if s[0] == "a" or s[0] == "e" or s[0] == "i" or s[0] == "o" or s[0] == "u":
            while s[i] != " ":
                i+=1
                continue
            wrd = s[:i] + "way"
            global wrd
    #else:
        #j = 0
        #while s[j] == "a" or s[j] == "e" or s[j] == "i" or s[j] == "o" or s[j] == "u":
            #j += 1
            #continue
        #wrd2 = s[:j]
    sen = wrd
    return sen
    #for j in list1:
        #print(j, end="")
        #if j == "a" or j == "e" or j == "i" or j == "o" or j == "u":
            
    #return list1
        
        #if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            #break
    #print(s + "way")
    #else: 
        #for i in sen:
            #pos = sen.index(i)
            #if lowsen[pos] != "a" or lowsen[pos] == "e" or lowsen[pos] == "i" or lowsen[pos] == "o" or lowsen[pos] == "u":
                #print(sen[pos:0:-1])
            
      