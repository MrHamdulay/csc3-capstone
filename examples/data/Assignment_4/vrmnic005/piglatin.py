vowels = set("aeiouAEIOU")

def toPigLatin(s):
    words = s.split()
    for i in range(len(words)):
        if words[i][0] in vowels:
            words[i] += "way"
        else:
            c = 1
            while c < len(words[i]) and words[i][c] not in vowels:
                c += 1
            words[i] = words[i][c:] + "a" + words[i][:c] + "ay"
    return " ".join(words)

def toEnglish(s):
    words = s.split()
    for i in range(len(words)):
        if words[i].endswith("way"):
            words[i] = words[i][:-3]
        else:
            c = 1
            while words[i][-c-3] != "a":
                c += 1
            words[i] = words[i][-c-2:-2] + words[i][:-c-3]
    return " ".join(words)

if __name__ == "__main__":
    assert toPigLatin("the quick black fox jumps over the lazy apple") == "eathay uickaqay ackablay oxafay umpsajay overway eathay azyalay appleway"
    assert toEnglish("eathay uickaqay ackablay oxafay umpsajay overway eathay azyalay appleway") == "the quick black fox jumps over the lazy apple"
