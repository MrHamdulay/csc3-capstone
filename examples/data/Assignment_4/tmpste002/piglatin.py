__author__ = 'stephen'
__date__ = '2014/03/31'

def toPigLatin(s):
    words = s.split(' ')
    new_words = []
    for word in words:
        if word[0].lower() == 'a' or word[0].lower() == 'e' or word[0].lower() == 'i' or word[0].lower() == 'o' or word[0].lower() == 'u':
            new_words.append(word + 'way')
        else:
            temp = ''
            for i in range(0, len(word)):
                if not (word[i].lower() == 'a' or word[i].lower() == 'e' or word[i].lower() == 'i' or word[i].lower() == 'o' or word[i].lower() == 'u'):
                    temp += word[i]
                else:
                    new_words.append(word[i:] + 'a' + temp + 'ay')
                    break
            else:
                new_words.append('a' + word + 'ay')
    return ' '.join(new_words)


def toEnglish(s):
    words = s.split(' ')
    new_words = []
    for word in words:
        if word[-3:-2] == 'w':
            new_words.append(word[:-3])
        else:
            temp = ''
            for i in range(-3, -len(word), -1):
                if word[i].lower() == 'a':
                    new_words.append(word[i+1:-2] + word[0:i])
                    break
            else:
                new_words.append(word[1:-2])
    return ' '.join(new_words)