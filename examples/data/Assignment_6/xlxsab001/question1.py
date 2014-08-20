word=""
wordlist=[]
word=input("Enter strings (end with DONE):\n")
if word!="DONE":
        wordlist.append(word)
while word != "DONE":
        word=input("")
        if word!= "DONE":
                wordlist.append(word)
    
listlength=len(wordlist)

maximum=0

for (i) in range(listlength):
        if len(wordlist[i])>maximum:
                maximum=len(wordlist[i])
                positionmax=i
#print(positionmax, maximum)
gap=" "
print()
print("Right-aligned list:")
for i in range(listlength):
        spacelength=(maximum-len(wordlist[i]))
        
        print(spacelength*gap,wordlist[i],sep="")
        
        



