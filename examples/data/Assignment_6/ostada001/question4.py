#Adam Oosthuizen
#Mark categorizing program

markString = input("Enter a space-separated list of marks:\n")
first=0
u2nd  = 0
l2nd  = 0
third = 0
fail  = 0
markList = markString.split(" ")


for i in range (0,len(markList)):
        markList[i] = eval(markList[i])
        if markList[i] >= 75:
                first +=1
        elif markList[i] >= 70:
                u2nd +=1
        elif markList[i] >= 60:
                l2nd += 1
        elif markList[i] >= 50:
                third += 1
        else:
                fail += 1
                
print("1 |"+"X"*first)
print("2+|"+"X"*u2nd)
print("2-|"+"X"*l2nd)
print("3 |"+"X"*third)
print("F |"+"X"*fail)
        
        