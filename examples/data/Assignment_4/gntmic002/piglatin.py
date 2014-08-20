#assignment4.3

def toPigLatin(s):
    if s[len(s)-1] != " ":
        s = s + " "
    ans = ""
    while len(s)>0:
        hold = s[0:s.index(" ")]
        s = s[s.index(" ")+1:]
        if hold[0].upper() in ["A","E","I","O","U"]:
            hold = hold + "way "
        else:
            while hold[0].upper() not in ["A","E","I","O","U"]:
                hold = hold[1:] + hold[0]
            hold = hold + "ay "
        ans = ans + hold
    ans = ans[0:len(ans)-1]
    return ans

def toEnglish(s):
    Common2 = ["th", "bl"]
    if s[len(s)-1] != " ":
        s = s +" "
    ans = ""
    while len(s)>0:
        hold=s[0:s.index(" ")]
        hold2 = hold
        s = s[s.index(" ")+1:]
        if hold.find("way") != -1:
            hold = hold[0:-3] + " " 
        else:
            hold = hold[0:len(hold)-2]
            if hold[len(hold)-2:] in Common2:
                hold = hold[-2] + hold[-1] + hold[0:-2] + " "
            else:
                while toPigLatin(hold) != hold2:
                    hold = hold[len(hold)-1] + hold[0:len(hold)-1]
                    hold = hold + " "
        ans = ans + hold
    ans = ans [0:len(ans)-1]
    return ans