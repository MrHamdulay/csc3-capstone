'''Write a Python program where the user can enter a list of strings
followed by the sentinel "DONE"
the list of strings is then printed out 
right-aligned with the longest string.
Sinead Urisohn
19 April 2014
'''

#Get input
lstring=input("Enter strings (end with DONE):\n")
#Set input to max
max=lstring
#create list variable
list=[]
#loop until sentinel enteredStuart

while lstring!="DONE":
    #add input to list if & only if it is not sentinel
    list.append(lstring)
    #compare length of string entered to that of max
    if len(lstring)>len(max):
        #if string bigger than max length make max the string
        max=lstring
    #ask for input again
    lstring=input()
#get length of longest item
longestLen=len(max)

#print the output using string formating to right align the output with length 
#of longest item
print("\nRight-aligned list:")
txt=txt="{0:>"+str(longestLen)+"}"
for i in range(len(list)):
    print(txt.format(list[i]))
        

        
    