# PigLatin to English (vice versa) program
# Jaren Hendricks
# 03 April 2014

def toPigLatin (s):
    PigLatin = ""
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    words = s.split()
    for word in words:
        count = 0
        if word[0] in vowels:
            PigLatin += word+"way"+ " "
        else:
            for let in word:
                if let not in vowels: 
                    count += 1
                else:
                    break
            PigLatin += word[count:] + "a" + word[:count] + "ay" + " "
                    
    return PigLatin

def toEnglish(s):
    words = s.split()
    english = ""
    for word in words:
        if word[:len(word)-4:-1] == "yaw":
            english+= word[:len(word)-3] + " "
        else:
            rev_ay = word[:len(word) - 2]
            first_cons = rev_ay.split("a")[-1]
            cons_remove = rev_ay[:len(rev_ay) - (len(first_cons)+1)]
            english += first_cons + cons_remove + " "
    return english          