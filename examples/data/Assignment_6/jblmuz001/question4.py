#question4
marks=[]
print("Enter a space-separated list of marks:")
mark=input("")
marks=mark.split(" ")
m=[]


def cat(a):
    if a>=75:
        return "1"
    elif a>=70 and a<75:
        return "2+"
    elif a>=60 and a<70:
        return "2-"
    elif a>=50 and a<60:
        return "3"
    elif a<50:
        return "F"
countFirst=0
countP=0
countN=0
countT=0
countF=0
for i in range(len(marks)):
    m.append(eval(marks[i]))
    category=cat(m[i])
    count=0
    if category=="1": 
        countFirst+=1
    elif category=="2+":
        countP+=1
    elif category=="2-":
        countN+=1
    elif category=="3":
        countT+=1
    elif category=="F":
        countF+=1
        
print("1"," |","X"*countFirst,sep="")
print("2+","|","X"*countP,sep="")
print("2-","|","X"*countN,sep="")    
print("3"," |","X"*countT,sep="")
print("F"," |","X"*countF,sep="")   
        
    
    





