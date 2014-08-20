'''Q1 of Assignment 6: Right Aligning string list
Patrick Boroughs
21 April 2014'''


print("Enter strings (end with DONE):")
#Initial input
string=input()
list=[]
maxlen=0

#Loop to add input to list
while string!="DONE":
    
    list.append(string)
    
    #Finding maximum string length
    if len(string)>maxlen:
        maxlen=len(string)
        
    #Receiving new input
    string=input()
    
print('\nRight-aligned list:')

#Print out list
for string in list:
    #align by longest string
    print((maxlen-len(string))*" "+string) 