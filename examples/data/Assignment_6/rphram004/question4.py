"""mark categorising programme
rama raphalalani
25-04-2014"""

#gets input and then splits the marks up
Categories=[0,0,0,0,0]
Marks=input("Enter a space-separated list of marks:\n")
Marks= Marks.split()

#gets the marks in the various categories
for i in range(len(Marks)):
    currMark=eval(Marks[i])
    if(currMark>=75):
        Categories[0]+=1
    elif(70<=currMark<75):
        Categories[1]+=1
    elif(60<=currMark<70):
       Categories[2]+=1
    elif(50<=currMark<60):
        Categories[3]+=1
    else:
        Categories[4]+=1

#prints the categorised marks        
print("1 |"+(Categories[0]*"X"))
print("2+|"+(Categories[1]*"X"))
print("2-|"+(Categories[2]*"X"))
print("3 |"+(Categories[3]*"X"))
print("F |"+(Categories[4]*"X"))