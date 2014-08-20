"""voting program
Thiolan Prevan Naidoo
NDXTHI031
25 april 2014"""


#initialise
strings=[]


string=input("Enter strings (end with DONE):\n")
while string !="DONE":
    strings.append(string)
    string=input("")
a=0

for string in strings:
    b=len(string)
    if b>a:
        x=b
      
print("\nRight-aligned list:")
for string in strings:
   
    print(" "*(x-len(string)),string, sep="")
    

