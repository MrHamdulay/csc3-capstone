"""Aligning strings to the right.
22 april 2014
Yoyo (Yuan-Yow) Wu"""

x =  []
width = 0
print("Enter strings (end with DONE):\n")
single = 0
while True:
    single = input ()
    if single.lower() == "done":
        break
    x.append(single)
   
    if len(single) > width:
        width = len(single)
       
if single != 0:
    print("Right-aligned list:")
    for i in range(len(x)):
    #print('{:<{width}}'.format(x[i]) ) #trouble for days. How do I do it? value for width is not working. 
    #formatting doesn't seem to work apparently. trying a different approach
        print(" "*( width- len( x[i] ) ),x[i],sep="")
 
    