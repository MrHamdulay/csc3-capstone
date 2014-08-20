#Translates between piglatin and english
#Adam Kaliski
#2014-03-31
def toPigLatin(s):
    words = s.split(' ')
    ans = ''
    count = 0
    cnt=0
    cons = ''
    while count < len(words):
        for i in words[count]:
            if (i in 'aeiou') and cnt==0:
                ans += words[count]+'way'+' '
                break
            elif (i in 'aeiou'):
                ans += words[count][cnt:] +'a'+ cons+'ay'+' '
                break
            elif cnt == (len(words[count])-1):
                ans += 'a'+words[count]+'ay'+' '
            cons+=i     
            cnt+=1
        count+=1
        cnt=0
        cons=''
    return ans[:len(ans)-1]
def toEnglish(s):  
    words = s.split(' ')
    ans = ''
    count = 0
    cnt=0
    while count < len(words):      
        for i in words[count][::-1]:
            if i == 'w':
                ans += words[count][:len(words[count])-cnt-1]+' '
                break
            elif cnt > 2 and i == 'a':
                x = words[count][:len(words[count])-cnt-1]
                y = words[count][len(words[count])-cnt:len(words[count])-2]
                ans += y+x+' '
                break
            cnt+=1
        count+=1
        cnt=0
    return ans[:len(ans)-1]       
if __name__ == '__main__':
    print(toPigLatin('aaa aab aba abb baa bab bba bbb'))
   # print(toEnglish('aaabway aabbay'))