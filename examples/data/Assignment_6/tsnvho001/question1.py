#Program to print out right-aligned strings 
#Tsanwani Vhonani
#20 April 2014

strings=[]

#get string from user
print("Enter strings (end with DONE):")
string=""
longest=0

#While user is not done,get more strings from user
while  string!='DONE':
   string=input("")
   if string!='DONE': #While the user is not done,the string must be appended to the list of strings already entered
      strings.append(string)
      if len(string) > longest: #If the string entered is longer than the longest thus far,make the entered string the longest
         longest=len(string)
#print the list of strings aligned with the longest string      
print("\nRight-aligned list:")
for string in strings:
   print (("{:>"+str(longest)+"}").format(string))

