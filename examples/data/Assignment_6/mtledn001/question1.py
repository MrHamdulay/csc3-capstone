'''Take in list until user enters done
Edencia Matlapeng
19 April 2014'''
#The String
word =input('Enter strings (end with DONE):\n')
#The list to store the words
words=[]
#The loop
while word.lower()!='done':
    words.append(word)
    word = input('')
#Finding the maximum length
long = 0
for k in words:
    if(len(k)>long):
        long = len(k)
print('\nRight-aligned list:')
for i in ((words)):
    #print(i+str(len(i)))
    space = long-len(i)
    print(' '*space,i,sep='')
    #print("{0}.{0:>leng}".format(i))
#print(words)
    
