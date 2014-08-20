"""Right-aligned list 
Yamkela Venfolo
23 April 2014"""

xString=input("Enter strings (end with DONE):\n")
dString=""
dictionary={}
n=0
#Keeps on telling the user to enter more names until he/she enters DONE
while(xString != "DONE"):
   dString=dString+"#$"+xString  #Store the names that are entered and seperate them by a space
   xString=input("")
#Create an array by splitting  the variable d by a spaces   
Array=dString.split("#$")
Array=Array[1:]
high=0
for i in range(len(Array)):
#Find the name in the array that has longest len  
      if(len(Array[i])> high):
         high=len(Array[i])
         
print("\nRight-aligned list:")
for i in range(len(Array)):
#Count how many spaces align should the name be   
   space=high-len(Array[i])
   print(space*" ",Array[i],sep="")
   