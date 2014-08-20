"""program to print right-aligned list of strings
emma jordi
20 april 2014"""

#create empty list
list_names = []

#get list of strings
#while not DONE
string=input("Enter strings (end with DONE):\n")
while string!= "DONE":
     #CHECKED
    #add strings to list
    list_names.append(string)
    string=input("")
    

#find longest string in the list
maxlength=0
for name in list_names:
    length=len(name)
    if length> maxlength:
        maxlength= length #checked
#format width = maxlength
print()
print("Right-aligned list:")
for name in list_names:
    f= "{0:>"+str(maxlength)+"}"
    formatted_name=f.format(name)#***
    #print right-aligned list 
    print(formatted_name)

