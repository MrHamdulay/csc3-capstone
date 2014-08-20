"""right aligning a group of names
Roger Cox 
4/22/2014"""


list_of_words=[]
size=[]
word=input ("Enter strings (end with DONE):\n")
# input list
while word!="DONE":
   list_of_words.append(word)
   wordz=str(word)
   word=input ("")
   #wordz=str(word)
   word_len=len(wordz)
   size.append(word_len)
#make two lists one of names other of name legnths
#Biggest_number=max(size)
print()
print("Right-aligned list:")
if list_of_words !=[] :
   #find longest legnth
   Biggest_number=max(size)
   for i in list_of_words:
      #format
      si= "{:>"+str(Biggest_number)+"}"
      print(si.format(i))
   
   #wordz=word.isalpha(word)
   #size+=len(word)