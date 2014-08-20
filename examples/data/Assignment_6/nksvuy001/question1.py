"""program to print out list of names right alligned
vuyolwethu nkosi
23 april 2014"""

#create empty list
string=[]
#get list from user
strings=input("Enter strings (end with DONE):\n")
while strings!="DONE":
    string.append (strings)
    strings=input("")
#convert every string to its lengths
#create list of lengths
string_1=[]
for i in range(len(string)):
    string_1.append (len(string[i]))
#print(string_1)
print("\nRight-aligned list:")
if string_1==[]:
    print()
else:
    x=max(string_1) #getting maximum length
for i in string:
    y=" "*(x-(len(i))) #print spaces equivalent to the maximum word length minus the word being used
    print(y,i,sep="") #print spaces and then word
           
    
          
    