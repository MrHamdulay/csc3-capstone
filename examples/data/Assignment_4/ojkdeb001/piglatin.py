vowels=('AEIOUaeiou')

def toPigLatin(s):
    phrase = s.split(" ")
    pig = ""
    for s in phrase:
        if s[0] in vowels:
            pig += s + "way" + " "
        else:
            v_index = 0
            for let in s:
                if let not in vowels: 
                    v_index += 1
                    continue
                else: 
                    break
            pig += s[v_index:] + "a" + s[:v_index] + "ay" + " "
    return pig[:len(pig) - 1]
#toPigLatin(s)    





def toEnglish(s):
    phrase2 = s.split(" ")
    eng = ""
    for s in phrase2:
        if s[:len(s) - 4:-1] == 'yaw':
            eng += s[:len(s) - 3] + " "
        else:
            index_2 = -3
            
            for let in reversed(s[:-3]):
                if let not in'a':
                    index_2-=1
                    continue
                else:
                    break
            eng +=  s[index_2:-2] + s[:index_2-1] + " "
    return eng
#toEnglish("aaaaway aaabway aabaway aabbway abaaway ababway abbaway abbbway aaaabay aababay abaabay abbabay aaabbay ababbay aabbbay abbbbay")#