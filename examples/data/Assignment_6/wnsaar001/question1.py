"""
right aligning list program
Aaron Weinstein
21 April 2014
"""
word= input("Enter strings (end with DONE):\n")
words=[]
while word != "DONE":
    words.append(word)    
    word= input("")
print("")
length=len(words)

print("Right-aligned list:")
if length>0:
    size = len(max(words, key=len))
    for item in words:
        print (str.rjust(item, size))     