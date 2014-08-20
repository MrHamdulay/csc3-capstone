# Luke Henkeman, HNKLUK001
# CSC1015F, Assignment 4, Q3
# 1 April 2014


def toPigLatin(s):
    split = s.split()
    spaces = s.count(" ")
    pigsent = ""
    for i in range(spaces+1):
        length = len(split[i])
        if split[i][0] in 'aeiou' or split[i][0] in 'AEIOU':
            pigsent += split[i]+"way "
        elif length == 1: 
                pigsent += "a"+split[i]+"ay "
        else:
            for j in range(1,length):
                if split[i][j] in 'aeiou' or split[i][j] in 'AEIOU':
                    pigsent += split[i][j::]+"a"+split[i][0:j]+"ay "
                    break
                elif split[i][2] in 'aeiou' or split[i][2] in 'AEIOU':
                    pigsent += split[i][2::]+"a"+split[i][0:2]+"ay "
                    break
                else:
                    pigsent += "a"+split[i]+"ay "
                    break
        i +=1
    return pigsent

def toEnglish(s):
    split = s.split()
    spaces = s.count(" ")
    engsent = ""
    for i in range(spaces+1):
        length = len(split[i])
        if split[i][:length-4:-1] == "yaw" or split[i][:length-4:-1] == "YAW":
            engsent += split[i][:length-3]+" "
            continue
        elif split[i][:length-3:-1] == "ya" or split[i][:length-3:-1] == "YA":
            a = split[i][2:length-3].find("a") or split[i][2:length-3].find("A")
            engsent += split[i][2+a+1:length-2]+split[i][:2+a]+" "
            continue
        i+=1
    return engsent