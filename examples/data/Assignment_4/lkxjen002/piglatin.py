def toPigLatin(s):
    result=""
    for word in s.split():
        suf=""
        count=0
        if word[0] in 'aeiou':
            k=word+"way"+" "
        else:
            for i in word:
                l=len(word)
                if i=='a' or i=='e' or i=='i' or i=='o' or i =='u':
                    break
                else:
                    count+=1
                suf+=i
                k=word[count:l:1]+"a"+suf+"ay"+" "
        result+=k
    return result

def toEnglish(s):  
    result=""
    for word in s.split():
        if 'w'in word:
            h=word.find('w')
            k=word[:h:1]+" "
        else:
            pref=""
            count=0
            p=len(word)
            g=p-2
            r=word[:g:1]
            m=len(r)
            s=r[::-1]
            for i in (s):
                if i=='a' or i=='e' or i=='i' or i=='o' or i =='u':
                    break
                else:
                    count+=1
                pref+=i
                q=(m-count-1)
            k=pref[::-1]+ r[:q:1]+" "
        result+=k
    return result