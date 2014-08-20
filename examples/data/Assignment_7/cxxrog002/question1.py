""" return a list of names in same order without duplicates
Roger Cox
29/04/2014"""
norepeat_words=[]
words=[]
word = input("Enter strings (end with DONE):\n") 
while word!="DONE" :
    
    if not word in words :
        norepeat_words.append(word)
    words.append(word)
    
    word=input("")
    
print()
print("Unique list:")
for word_1_st in norepeat_words :
        
    print (word_1_st)