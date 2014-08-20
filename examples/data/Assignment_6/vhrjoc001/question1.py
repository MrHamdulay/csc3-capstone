#assignment 6 question 1
#vhrjoc001
#making an input of words to be right aligned to the longest word
stringlist=[]  #list of input words
strings=input("Enter strings (end with DONE):\n")
while strings!="DONE":      #as long as input doesnt = done it will add the words to the list

   stringlist.append(strings)
   strings=input()    #continues input
   

if stringlist==[]:
   print("\nRight-aligned list:")
else:
   largeststr=max(stringlist, key=len) # finding the largest string
   maxlength=len(largeststr)

   print("\nRight-aligned list:")   #right aligning 
   for i in range(len(stringlist)):   
      output="{0:>{1}}".format(stringlist[i], maxlength) #formatting string to print aligned
   
      print(output)
  
  
  
  

         

   

   
