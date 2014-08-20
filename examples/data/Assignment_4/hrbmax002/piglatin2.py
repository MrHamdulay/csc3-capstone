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
            hold = hold + "a"
            while hold[0].upper() not in ["A","E","I","O","U"]:
                hold = hold[1:] + hold[0]
            hold = hold + "ay "
        ans = ans + hold
    ans = ans[0:len(ans)-1]
    return ans

def toEnglish(s):
    if s[len(s)-1] != " ":
        s = s + " "
    ans = ""    
    while len(s)>0:
        hold = s[0:s.index(" ")]
        s = s[s.index(" ")+1:]        
        if hold[-3:]=="way":
            ans = ans + " " + hold[0:-3]
        else:
            hold = hold[0:-2]
            while hold[-1] != "a":
                hold = hold[-1] + hold[0:-1]
            ans = ans + " " + hold[0:-1]
    return ans[1:]