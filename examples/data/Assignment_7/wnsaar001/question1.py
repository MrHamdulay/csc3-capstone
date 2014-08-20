"""30 April 2014
Aaron Weinstein
print distinct inputs"""

lista=[]
count=0
word=input("Enter strings (end with DONE):\n")
while (word !="DONE"):
   if word not in lista:
      lista.append(word)
   word=input()
print("\nUnique list:")
for i in lista:
   print(i)