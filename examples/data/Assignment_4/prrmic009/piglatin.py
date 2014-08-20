def toEnglish(s):
    s = s + " "
    sentence = ""
    word = ""
    for i in (s):
        if i != " ":
            word += i
        else:
            if word[-3::] == "way":
                new_word = word[:-3]
                sentence += new_word + " "
                word = ""
                new_word = ""
            else:
                c = ""
                new_word = word[:-2]
                counter = 0
                for i in (new_word[::-1]):
                    if i != "a":
                        counter += 1
                        c += i
                    else:
                        counter += 1
                        new_word = c[::-1] + new_word[:-(counter)]
                        sentence += new_word + " "
                        new_word = ""
                        word = ""
                        break
    return sentence

def vowel(a):
    for i in ('a','e','i','o','u','A','E','I','O','U'):
        if a==i:
            return True        
    return False

def toPigLatin(s):
    string = s 
    substring = ''
    x = 0
    result = ''
    words = string.split(' ')

    for i in range(len(words)):
        if vowel(words[i][0]) : result += (words[i]+'way ')
        else: 
            substring = ''
            x = 0
            for a in words[i]:
                if vowel(a):
                    result += (words[i][x:len(words[i]):1] + 'a'+substring+'ay ')
                    break
                else:
                    substring = substring + a
                x += 1
            else:
                result += 'a'+substring+'ay'
    return result