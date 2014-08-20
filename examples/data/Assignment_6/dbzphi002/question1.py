#Thembekile Dubazana
#dbzphi002
#April 2014
#Assignment 6:Q1

"""Program to print list with right alignment with longest string"""

#The input and variables
strlist=[]
string=input("Enter strings (end with DONE):\n")
Max=0
#Loop for string entries
while string!="DONE":
    strlist.append(string)
    string=input()

#Check for longest string    
for a in strlist:
    if len(a) > Max:
        Max=len(a)
        
#Print right aligned list
print()
print("Right-aligned list:")
for b in range(len(strlist)):
    print("{0:>{1}}".format(strlist[b],Max))
    
          
    


        
        
        
    

