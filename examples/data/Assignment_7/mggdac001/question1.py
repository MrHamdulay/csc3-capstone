def words():
    word_i=input('Enter strings (end with DONE):\n')
    word_l=[]
      
    while word_i !="DONE":
        if word_i=="DONE":
                break          
        if not word_i in word_l:
            word_l.append(word_i)
        word_i=input('')
    
    print()
    print('Unique list:')
    for word in word_l:
        print(word)
words()            
        