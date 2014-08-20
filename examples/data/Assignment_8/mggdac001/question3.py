en_message=''
def encription(s):
    global en_message
    if s!=s.upper:
        if len(s)==0:
            print('Encrypted message:\n',en_message,sep='')
        elif ((ord(s[0]))<122) and (s[0] !=' ') and (s[0] !='.'):
            en_message+=chr((ord(s[0])+1))
            return encription(s[1:])
        elif s[0] =='.' or s[0] in ('!.@#$%^&*()') or s[0]==' ':
            en_message+=s[0]
            return encription(s[1:])
        else:
            en_message+=chr((ord(s[0]))-25)
            return encription(s[1:])
    else:
        print('Encrypted message:\n',s,sep='')
s=input('Enter a message:\n')
encription(s)
