#question one assignment 7
#vhrjoc001
stringlist=[]                 #creating two lists one for input and one that will be the sifted list
final_list=[]
string=input("Enter strings (end with DONE):\n")
while string!="DONE":
   stringlist.append(string)     # add input to list until sentinal word is used being done
   string=input()
   
else:
   for i in stringlist:         #once done is used we place the non elements into the new string
      if i not in final_list:
         final_list.append(i)
print("\nUnique list:")
for i in final_list:
   print(i)   
   

   