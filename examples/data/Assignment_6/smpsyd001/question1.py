#Enter String of words and Allign
#4/21/2014
#Sydney Simpson

#Get List
lst=[] 
string=1
print("Enter strings (end with DONE):\n")
while string !="DONE":
    string=input()
    if string!="DONE":
        lst.append(string)
#print (lst)
    
#Find longest string
a=0
for word in lst:
    if len(word)>a:
        a=len(word)
    else:
        continue
#print(a)
    

#Print out List, right alligned
print("Right-aligned list:")
for words in lst:
    b=len(words)
    c=a-b
    print(" "*c, words, sep='')