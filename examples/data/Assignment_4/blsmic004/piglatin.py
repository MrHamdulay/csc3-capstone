# PigLatin

   
def toPigLatin(b):
    sen = ''
    b = b.split(' ')
    for i in b:
        if i[0] in ('a','e','i','o','u'):
            voword = i + 'way '
            sen = sen + voword
        else:
            for j in range(len(i)):
                if i[j] not in ('a','e','i','o','u'):
                    coword = i[j+1:] + 'a' + i[0:j+1] + 'ay '
                    if j==(len(i)-1):
                       sen = sen + coword 
                else:
                    sen = sen + coword
                    break
           
    return sen

def toEnglish(a):
    a = a.split(' ')
    sen = ''
    for i in a:
        if i[-3:]=='way':
            sen = sen + i[:-3] + ' '
        else:
            n = -3
            word = ''
            while True:
                if i[n]=='a':
                    word = word + i[:n] + ' '
                    break
                else:
                    word = i[n] + word
                    n = n-1
            sen = sen + word
    return sen