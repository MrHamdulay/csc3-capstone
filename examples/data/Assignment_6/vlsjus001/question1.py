#question 1 assignment 6
#list of names
#justin valsecchi
#2014/04/24


values=[] #creating an empty list
strings=input("Enter strings (end with DONE):\n") #getting values for our list 
    
while strings != 'DONE':
        values.append(strings) #adding strings to our list
        strings= input("")
if values != []:
        max_title_width = max(len(strings) for strings in values) #determining the max len of strings
print("\nRight-aligned list:")
for i in values:
        print("{0:>{leng}}".format(i,leng=max_title_width)) #formating the strings, to be right aligned
        
        
                

                