"""Program that prints a list of inputed string. 
Tafadzwa Moyo-MYXTAF004
27 April 2014"""

#Get list of string
strlis=[]
a=input("Enter strings (end with DONE):\n")
while a!="DONE":
    strlis.append(a)
    a=input()

#Prints the list of string
print()
print("Unique list:")
pristr=[] #list of printed string
for i in strlis:
    if not i in pristr:
        print(i)
        pristr.append(i)
    