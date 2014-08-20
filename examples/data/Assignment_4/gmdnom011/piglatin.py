# Program to convert English into Pig Latin and back
# Nomsa Gamedze
# 31 March 2014

def toPigLatin(s):
    #s = input("Enter an English sentence:"'\n')
    words = s.split()
    # print("Pig-Latin:")
    translation1 = ""
    for i in range(len(words)):
        if words[i]:
            word1 = words[i]
            output = ""
            vowel = False
            done = False
            for c in word1:
                if c in "aeiou":
                    vowel = True         
                    break
                if not vowel:
                    output += c
            if output:
                x = len(output)
                word2 = word1[x:]
                translation1 += " " + word2 + "a" + output + "ay"
                done = True
                continue
            if not done:
                translation1 += " " + word1 + "way" 
                continue
    translation1 = translation1[1:]
    return translation1
            

                
                
def toEnglish(s):
    # s = input("Enter a Pig Latin sentence:"'\n')
    words =  s.split()
    done = False
    # print("English:")
    translation2 = ""
    for i in range(len(words)):
        if words[i]:
            word1 = words[i]
            output = ""
            x = len(word1)
            word1 = word1[:x-2]
            word2 = word1[::-1]
            done = False
            for c in word2:
                if c == "w":
                    word2 = word2[1:]
                    word2 = word2[::-1]
                    translation2 += " " + word2
                    done = True
                    continue
                if c in "aeiou":
                    break
                else:
                    output += c
            if output and not done:
                y = len(output)+1
                word2 = word2[y:]
                word2 = word2[::-1]
                prefix = output[::-1]
                translation2 += " " + prefix + word2
                continue
    translation2 = translation2[1:]
    return translation2