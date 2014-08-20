#assignment 6 question 4
#vhrjoc001
# tallying results into catagories of fail, pass,ect.
classification=[0,0,0,0,0] # array used for identifying whch catagory mark falls into
marks=input("Enter a space-separated list of marks:\n").split(" ")
for i in range(len(marks)):
    if eval(marks[i])<50:
        classification[0]+=1
    elif 50<=eval(marks[i])<60:
        classification[1]+=1
    elif 60<=eval(marks[i])<70:
        classification[2]+=1
    elif 70<=eval(marks[i])<75:
        classification[3]+=1
    elif eval(marks[i])>=75:
        classification[4]+=1
print("1 |","X"*classification[4], sep="")
print("2+|","X"*classification[3], sep="")
print("2-|","X"*classification[2], sep="")
print("3 |","X"*classification[1], sep="")
print("F |","X"*classification[0], sep="")

        
        
