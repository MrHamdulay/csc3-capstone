#program to omit repeated words in a list of strings
#F.J.Chigwaza
#01 May 2014

def words():
    word = input('Enter strings (end with DONE):\n')
    s=[]
    
    while word!='DONE':
        if word not in s:
            s.append(word)
        word=input('')
    print('\nUnique list:')        
    for word in s:
        print(word)
    
words()    