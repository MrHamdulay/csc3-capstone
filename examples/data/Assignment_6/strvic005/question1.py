"""A program to right justify a list of words
Vicky Stark
23 april 2014"""

list_=[]  # create empty string

#get a list of strings with a sentinel of 'DONE'
word=input("Enter strings (end with DONE):\n")

while word!='DONE':
    list_.append(word)
    word=input('')
  
#Once user has typed in "DONE", iterate through the list to find the length of the longest word 
longest=0
for word in list_:
    if len(word)> longest:
        longest=len(word)
        
#right justify all words
print("\nRight-aligned list:")
for word in list_:
    print(word.rjust(longest))
    
    
    