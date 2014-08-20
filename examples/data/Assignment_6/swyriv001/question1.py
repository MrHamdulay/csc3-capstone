"""Program that prints the names right-alighened to the longest name provided
   Rivoningo Seweya
   23 April 2014"""
#create an empty list
strings=[]
#ask for strings from the user
string=input("Enter strings (end with DONE):\n")
#create a loop with a sentinal
while string!= "DONE" :
    strings.append(string)
    string=input("") 
print("")
#determine the longest string in the list
for i in strings:
    maxi=len(strings[0])
    x=len(i)
    if x>maxi:
        maxi=x    
#print out the right-alighened list
print("Right-aligned list:")
for i in strings:   
    y=str(maxi)
    print(("{0:>"+y+"}").format(i)) 