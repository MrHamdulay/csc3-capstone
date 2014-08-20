def toPigLatin (s):
    if s[:1] in "aeiou":
        s+="way"
    
    if s[:1] in "bcdfghjklmnpqrstvwxyz" and s[1:2] in "bcdfghjklmnpqrstvwxyz" and s[2:3] in "bcdfghjklmnpqrstvwxyz":
        consonant = s[:3]
    elif s[:1] in "bcdfghjklmnpqrstvwxyz" and s[1:2] in "bcdfghjklmnpqrstvwxyz":
        consonant = s[:2]
    elif s[:1] in "bcdfghjklmnpqrstvwxyz":
        consonant = s[:1]
    
    s = s.replace(consonant,"")
    
    s = s + "a" + consonant + "ay"
    
    return s

