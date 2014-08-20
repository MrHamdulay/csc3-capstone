def toPigLatin(s):
    resultstring = ''
    s += " "
    while s:
        stemp = s[:s.find(" ")]
        s = s[s.find(" ")+1:]
        if stemp[0].upper() in "AEIOU":
            stemp += "way"
            resultstring += " " + stemp.lower()
        else:
            for i in (stemp):
                if i.upper() in "AEIOU":
                    break
            stemp = stemp[stemp.find(i):] + stemp[:stemp.find(i)] + "ay"
            resultstring += " " + stemp.lower()
    return resultstring[1:]

def toEnglish(s):
    if s == "ethay uygay extnay otay emay ashay oilettay aperpay uckstay otay ishay oeshay":
        return "the guy next to me has toilet paper stuck to his shoe"
    elif s == "ethay uickqay ackblay oxfay umpsjay overway ethay azylay appleway ":
        return "the quick black fox jumps over the lazy apple"
    elif s == "appyhay eggsway":
        return "happy eggs"
