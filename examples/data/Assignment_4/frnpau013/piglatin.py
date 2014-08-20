def toPigLatin(s):
    s = s.split(" ")
    answer = ""
    for i in s:
        s = i[0]
        if s in "aeiou" or s in "AEIOU":
            i += "way"
            answer += i + " "
        else:
            con_string = ""
            for y in i:
                if y not in "aeiou":
                    con_string += y
                else:
                    break
            i = i[len(con_string)::] + "a" + con_string + "ay"
            answer += i + " "
    answer = answer[0: len(answer) - 1]
                    
    return answer

def toEnglish(s):
    s = s.split(" ")
    answer = ""
    for i in s:
        if i[len(i) - 3] == 'w':
            i = i[0:len(i) - 3]
            answer += i + " "
        else:
            i = i[0:len(i) -2]
            s = ""
            con_string = ""
            count = 1
            while s != "a":
                s = i[len(i) - count]
                count += 1
                con_string += s
                if len(i) - count == 0:
                    if s == "a":
                        break
                    s = i[len(i) - count]
                    con_string += s
                    break
           
            con_string = con_string[::-1]
            
            if len(con_string) - count == 0: # had to add this if-else as otherwise would be getting unwanted 'a' in output due to how 'i[0:len(i) - count + 1]' resolves in such a case
                            con_string = con_string[1: len(con_string)]
                            i = con_string
                            answer += i + " "            
            else:
                if len(con_string) != 1: # had to add this if-else as wierdly if  the initial con_string is two letters (e.g. "ab") and then reversed via con_string = con_string[::-1] then it gives only the last letter (e.g. "b"), so "con_string = con_string[1: len(con_string)]" would make con_string = "")
                    con_string = con_string[1: len(con_string)]
                    i = con_string + i[0:len(i) - count + 1] 
                    answer += i + " "
                else:
                    answer += con_string + " "
            
            
    answer = answer[0: len(answer) - 1]
            
            
    return answer