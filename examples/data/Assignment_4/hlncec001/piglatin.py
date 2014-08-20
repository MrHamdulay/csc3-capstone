def toPigLatin(s):
    s+=' '
    pig=''
    while s!='':
        space= s.find(' ')
        sn= s[:space]
        i=1
        if sn[0:1] in ('a','e','i','o','u'):
            pig+= sn+ 'way' + ' '
        elif sn[0:1] not in ('a','e','i','o','u'):
            while sn[0:1] not in ('a','e','i','o','u'):
                sn=sn[1::]+ 'a'*i+ sn[0:1]
                i=0
            pig+= sn+'ay' +' '
        s= s[space+1:]
    return pig
        
def toEnglish(s):
    s+=' '
    pig=''
    while s!='':
        space= s.find(' ')
        sn= s[:space]
        if sn[-3::1]=='way':
            pig+= sn[:-3:1] +' '
        elif sn[-3::1]!='way':
            sn=sn[:-2:1]
            n=sn[::-1].find('a')
            pig+= sn[:-n-1:-1][::-1] + sn[::-1][n+1::1][::-1] +' '
        s= s[space+1:]
    return pig